#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:51:41 2025

Código para preparar o arquivo CSV para o CatBoost

@author: caio
"""
import pandas as pd


# Variáveis "Universais"
data = pd.read_csv('/home/caio/github/previsao-vendas-sazonais/data/data_limpa.csv')
colunas_categoricas = ['Cidade', 'Tipo de Cliente', 'Gênero', 'Linha de Produto',"Hora",
                       'Pagamento', 'Turno', 'Estação']


# Tratamento Categórico: DROP
data_drop = data.drop(columns=colunas_categoricas)
data_drop.to_csv('data/data_drop.csv', index=False)
print(data_drop.dtypes)


