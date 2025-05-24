# Projeto de Limpeza, Análise e Previsão de Vendas Sazonais com CatBoost

Este projeto tem como objetivo a limpeza, o pré-processamento e a previsão de vendas sazonais utilizando **CatBoost** para a construção de um modelo de previsão. O foco inicial foi a transformação dos dados e a análise para prever a **Receita Bruta** com base em variáveis temporais e características de vendas.

Além disso, a biblioteca **Optuna** foi utilizada para otimizar os hiperparâmetros do modelo, e a validação cruzada foi aplicada para garantir que o modelo tenha boa capacidade de generalização. A **métrica RMSE** foi utilizada para avaliar o desempenho do modelo.

## Descrição do Projeto

O dataset utilizado contém informações de vendas em diferentes filiais de uma empresa, incluindo dados como tipo de cliente, gênero, linha de produto, preço unitário, quantidade, impostos, totais e dados temporais de cada transação.

O projeto inclui os seguintes passos principais:

### 0. **Análise, Criação de KPI's e Dashboard Interativo com Power BI**

Você pode ver o relatório final clicando no link abaixo:

[📄 Ver apresentação em PDF](https://github.com/CaioJulioBNG/previsao-de-vendas-sazonais/blob/main/Presentation.pdf)

Esse relatório contém uma analise descritiva e exploratória de vendas, contendo diversos fatores, como temporais, sazonalidade,análise geográfica etc...
Além das análises realizadas, foi realizado um planos de ação baseados em dados

### 1. **Limpeza e Preparação dos Dados**

- **Renomeação das colunas**: As colunas foram renomeadas para tornar os dados mais legíveis, traduzindo os nomes das colunas para o português.
- **Tratamento de Dados**:
    - **Conversão de tipos de dados**: A coluna **Data** foi convertida para o formato `datetime`, e novas colunas como **ano**, **mês** e **dia** foram extraídas.
    - **Tratamento de hora**: A hora de cada transação foi processada para categorizar o momento da compra em 'manhã', 'tarde' ou 'noite'.
    - **Tradução de valores**: Valores em inglês em colunas categóricas, como **Tipo de Cliente**, **Gênero**, **Linha de Produto** e **Pagamento**, foram traduzidos para o português.
    - **Criação de variáveis adicionais**: A coluna **Estação** foi criada com base no mês da transação, classificando as vendas em uma das quatro estações do ano (Primavera, Verão, Outono e Inverno).
    - **Remoção de colunas irrelevantes**: Algumas colunas, como **ID da Fatura** e **Filial**, foram removidas por não agregarem valor à análise.

### 2. **Tratamento das Colunas Categóricas**

As colunas categóricas, como **Cidade**, **Tipo de Cliente**, **Gênero**, **Linha de Produto**, **Pagamento**, **Turno** e **Estação**, passaram por duas abordagens:

- **One-Hot Encoding**: Foi inicialmente testado o **One-Hot Encoding** para tratar as variáveis categóricas, mas essa abordagem não gerou bons resultados, levando a um desempenho inferior do modelo.
- **Remoção das Colunas Categóricas**: Optou-se por **remover as colunas categóricas** do modelo, o que resultou em melhor desempenho.

### 3. **Modelo CatBoost e Otimização de Hiperparâmetros com Optuna**

O modelo **CatBoostRegressor** foi utilizado para realizar a previsão da **Receita Bruta**. A otimização dos hiperparâmetros foi feita com a biblioteca **Optuna**, ajustando os seguintes parâmetros:

- **depth**: A profundidade das árvores.
- **learning_rate**: A taxa de aprendizado.
- **l2_leaf_reg**: A regularização L2 para evitar overfitting.
- **iterations**: O número de iterações (ou árvores) no modelo.

A otimização foi realizada usando **validação cruzada** (com 4 divisões de **KFold**) para garantir uma boa generalização do modelo e evitar overfitting. A métrica **RMSE** (Root Mean Squared Error) foi utilizada para avaliar a precisão do modelo.

### 4. **Validação Cruzada e Métrica RMSE**

A **validação cruzada** foi usada para garantir que o modelo tivesse uma boa capacidade de generalização, validando a performance em diferentes subconjuntos dos dados. O erro de previsão foi medido pela métrica **RMSE**, que forneceu uma indicação da precisão do modelo.

### 5. **Resultados e Conclusões**

Após a otimização dos parâmetros e a validação cruzada, os melhores parâmetros foram utilizados para treinar o modelo final. A avaliação do modelo foi feita com base na métrica **RMSE**, que mostrou a precisão do modelo em prever a **Receita Bruta** das vendas.


## Tecnologias Utilizadas

- **Python**
- **Pandas** - Manipulação de dados
- **NumPy** - Operações numéricas
- **Optuna** - Otimização de hiperparâmetros
- **CatBoost** - Algoritmo de regressão baseado em boosting
- **Scikit-learn** - Validação cruzada e métricas de avaliação

## Contribuições

Sinta-se à vontade para fazer **fork**, **pull requests** ou **issues** para contribuir com melhorias ou relatar problemas.

