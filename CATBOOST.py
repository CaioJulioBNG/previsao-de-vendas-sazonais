#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:29:04 2025

@author: caio
"""

# Importação das bibliotecas necessárias
import pandas as pd  # Manipulação de dados
import numpy as np  # Operações numéricas
import optuna  # Otimização de hiperparâmetros
from catboost import CatBoostRegressor  # Modelo de regressão CatBoost
from sklearn.metrics import mean_squared_error  # Para calcular o erro quadrático médio
from sklearn.model_selection import cross_val_score, KFold  # Validação cruzada
from sklearn.model_selection import train_test_split  # Divisão de dados em treino e teste

# Carregamento dos dados
# Lê o arquivo CSV com os dados pré-processados
data = pd.read_csv('/home/caio/github/previsao-vendas-sazonais/data/data_drop.csv')

# A coluna 'Receita Bruta' é separada como variável alvo (target)
target = data.pop('Receita Bruta')
# O restante das colunas são características (features) do modelo
feature = data

# Separando os dados em treino e teste (80% para treino, 20% para teste)
feature_treino, feature_teste, target_treino, target_teste = train_test_split(
    feature, target, test_size=0.2, random_state=42)  # Divide os dados de forma aleatória

# Função objetivo para o Optuna
# A função recebe um objeto 'tentativa' do Optuna e sugere os hiperparâmetros do modelo.
def objetivo(tentativa):
    parametros = {
        'depth': tentativa.suggest_int('depth', 4, 10),  # Profundidade das árvores de decisão
        'learning_rate': tentativa.suggest_float('learning_rate', 0.01, 0.3),  # Taxa de aprendizado
        'l2_leaf_reg': tentativa.suggest_float('l2_leaf_reg', 1.0, 10.0),  # Regularização L2
        'iterations': tentativa.suggest_int('iterations', 100, 1000),  # Número de iterações
        'random_seed': 42,  # Semente para reprodutibilidade
        'allow_writing_files': False,  # Impede o uso de cache interno no CatBoost
        'verbose': 0  # Desativa a saída de texto durante o treino do modelo
    }
    
    # Criação e treino do modelo CatBoost com os parâmetros sugeridos
    modelo = CatBoostRegressor(**parametros)
    
    # K-Fold cross-validation: divide o treino em 4 dobras
    kf = KFold(n_splits=4, shuffle=True, random_state=69)
    
    # Calcula a validação cruzada com o erro médio quadrático (RMSE negativo)
    scores = cross_val_score(modelo, feature_treino, target_treino,
                             cv=kf, scoring='neg_root_mean_squared_error')
    
    # Retorna o RMSE médio negativo (pois o Optuna minimiza a função de objetivo)
    return -np.mean(scores)

# Criando e rodando o estudo do Optuna
# O Optuna irá tentar otimizar os parâmetros do modelo para minimizar o RMSE
estudo = optuna.create_study(direction="minimize")
estudo.optimize(objetivo, n_trials=5)  # O Optuna tentará 5 configurações diferentes

# Exibindo os melhores parâmetros encontrados e o erro (RMSE)
print("Melhores parâmetros encontrados:", estudo.best_params)
print(f"RMSE médio validado: {estudo.best_value:.4f}")

# Treinando o modelo final com os melhores parâmetros encontrados
melhor_modelo = CatBoostRegressor(**estudo.best_params, random_seed=42, verbose=0)
melhor_modelo.fit(feature_treino, target_treino)  # Ajustando o modelo aos dados de treino

# Avaliando o modelo final no conjunto de teste
previsao = melhor_modelo.predict(feature_teste)  # Fazendo previsões com o modelo treinado

# Calculando o RMSE (Raiz do erro quadrático médio) no conjunto de teste
rmse_final = np.sqrt(mean_squared_error(target_teste, previsao))
print(f"RMSE no teste: {rmse_final:.4f}")  # Exibindo o resultado final do RMSE
