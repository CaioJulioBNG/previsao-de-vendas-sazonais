import pandas as pd
import numpy as np

# Carregando o arquivo CSV contendo os dados
data = pd.read_csv("data/labrat.csv")

# Dicionário para renomear as colunas, traduzindo-as para o português
renomear_colunas = {
    'Invoice ID': 'ID da Fatura',
    'Branch': 'Filial',
    'City': 'Cidade',
    'Customer type': 'Tipo de Cliente',
    'Gender': 'Gênero',
    'Product line': 'Linha de Produto',
    'Unit price': 'Preço Unitário',
    'Quantity': 'Quantidade',
    'Tax 5%': 'Imposto 5%',
    'Total': 'Total',
    'Date': 'Data',
    'Time': 'Hora',
    'Payment': 'Pagamento',
    'cogs': 'Custo de Bens Vendidos',
    'gross margin percentage': 'Percentual de Margem Bruta',
    'gross income': 'Receita Bruta',
    'Rating': 'Avaliação'
}

# Renomeando as colunas de acordo com o dicionário definido
data.rename(columns=renomear_colunas, inplace=True)

# -------------------------------------------------------
# Tratamento Geral dos Dados

# Removendo a coluna 'ID da Fatura', pois não é relevante para a análise
data.drop(columns=['ID da Fatura'], inplace=True)

# Convertendo a coluna 'Data' para o tipo datetime
data['Data'] = pd.to_datetime(data['Data'])

# Criando novas colunas de Ano, Mês e Dia a partir da coluna 'Data'
data['Ano'] = data['Data'].dt.year
data['Mês'] = data['Data'].dt.month
data['Dia'] = data['Data'].dt.day

# Removendo a coluna 'Filial' (não usada após o renomeamento)
data.drop(columns=['Filial'], inplace=True)

# Removendo a coluna 'Data', pois já criamos as colunas Ano, Mês e Dia
data.drop(columns=['Data'], inplace=True)

# Removendo a coluna 'Ano' (não será mais necessária)
data.drop(columns=['Ano'], inplace=True)

# -------------------------------------------------------
# Tratamento das Horas

# Convertendo a coluna 'Hora' para datetime, criando uma nova coluna 'Hora2'
data['Hora2'] = pd.to_datetime(data['Hora'], format='%H:%M')  # Assumindo que o formato é 'HH:MM'

# Função para definir a parte do dia baseado na hora
def parte_do_dia(h):
    if h < 12: return 'manhã'
    elif h < 18: return 'tarde'
    else: return 'noite'

# Criando a coluna 'Hora_da_Compra' para armazenar a hora da compra
data['Hora_da_Compra'] = data['Hora2'].dt.hour

# Aplicando a função 'parte_do_dia' para criar a coluna 'Turno' (manhã, tarde, noite)
data['Turno'] = data['Hora_da_Compra'].apply(parte_do_dia)

# Removendo as colunas 'Hora2' e 'Hora_da_Compra', pois já temos as informações necessárias
data.drop(columns=['Hora2'], inplace=True)
data.drop(columns=['Hora_da_Compra'], inplace=True)

# -------------------------------------------------------
# Tradução das Colunas Categóricas

# Traduzindo os valores da coluna 'Tipo de Cliente'
data['Tipo de Cliente'] = data['Tipo de Cliente'].replace({
    'Member': 'Recorrente',
    'Normal': 'Ocasional'})

# Traduzindo os valores da coluna 'Gênero'
data['Gênero'] = data['Gênero'].replace({
    'Female': 'Feminino',
    'Male': 'Masculino'})

# Traduzindo os valores da coluna 'Linha de Produto'
data['Linha de Produto'] = data['Linha de Produto'].replace({
    'Health and beauty': 'Saúde e Beleza',
    'Electronic accessories': 'Acessórios Eletrônicos',
    'Home and lifestyle': 'Casa e Estilo de Vida',
    'Sports and travel': 'Viagens e Esportes',
    'Food and beverages': 'Comidas e Bebidas',
    'Fashion accessories': 'Acessórios de Moda',
})

# Traduzindo os valores da coluna 'Pagamento'
data['Pagamento'] = data['Pagamento'].replace({
    'Cash': 'Dinheiro',
    'Credit card': 'Crédito',
    'Ewallet': 'Carteira Eletrônica'})

# -------------------------------------------------------
# Função para atribuir a estação do ano baseada no mês
def estacao_mianmar_4(mes):
    if mes in [3, 4, 5]:
        return 'Primavera'
    elif mes in [6, 7, 8]:
        return 'Verão'
    elif mes in [9, 10, 11]:
        return 'Outono'
    else:
        return 'Inverno'

# Criando a coluna 'Estação' a partir do mês
data['Estação'] = data['Mês'].apply(estacao_mianmar_4)

# Exibindo os valores únicos da coluna 'Percentual de Margem Bruta' e informações do dataset
print(data['Percentual de Margem Bruta'].unique())
print(data.info())

# Salvando os dados tratados em um novo arquivo CSV
data.to_csv('data/data_limpa.csv', index=False)

# Exibindo as colunas categóricas (com valores do tipo 'object')
data_categorica = data.select_dtypes(include=['object']).columns
print("Colunas Categóricas:")
print(data_categorica)
