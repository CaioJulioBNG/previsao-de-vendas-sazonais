import pandas as pd
import numpy as np

data = pd.read_csv("data/labrat.csv")

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

# Renomeando as colunas
data.rename(columns=renomear_colunas, inplace=True)

# TRatamento Gerais
data.drop(columns=['ID da Fatura'], inplace=True)
data['Data'] = pd.to_datetime(data['Data'])
data['Ano'] = data['Data'].dt.year
data['Mês'] = data['Data'].dt.month
data['Dia'] = data['Data'].dt.day
data.drop(columns=['Filial'], inplace=True)
data.drop(columns=['Data'], inplace=True)
data.drop(columns=['Ano'], inplace=True)


# Tratamento das Horas
data['Hora2'] = pd.to_datetime(data['Hora'], format='%H:%M')  # ou '%H:%M:%S' se tiver segundos

def parte_do_dia(h):
    if h < 12: return 'manhã'
    elif h < 18: return 'tarde'
    else: return 'noite'
    
data['Hora_da_Compra'] = data['Hora2'].dt.hour
data['Turno'] = data['Hora_da_Compra'].apply(parte_do_dia)
data.drop(columns=['Hora2'], inplace=True)
data.drop(columns=['Hora_da_Compra'], inplace=True)

# Tradução

data['Tipo de Cliente'] = data['Tipo de Cliente'].replace({
    'Member': 'Recorrente',
    'Normal': 'Ocasional'})

data['Gênero'] = data['Gênero'].replace ({
    'Female': 'Feminino',
    'Male': 'Masculino'})

data['Linha de Produto'] = data['Linha de Produto'].replace({
    'Health and beauty': 'Saúde e Beleza',
    'Electronic accessories': 'Acessórios Eletrônicos',
    'Home and lifestyle': 'Casa e Estilo de Vida',
    'Sports and travel': 'Viagens e Esportes',
    'Food and beverages': 'Comidas e Bebidas',
    'Fashion accessories': 'Acessórios de Moda',
    })

data['Pagamento'] = data['Pagamento'].replace ({
    'Cash': 'Dinheiro',
    'Credit card': 'Crédito',
    'Ewallet': 'Carteira Eletrônica'})

def estacao_mianmar_4(mes):
    if mes in [3, 4, 5]:
        return 'Primavera'
    elif mes in [6, 7, 8]:
        return 'Verão'
    elif mes in [9, 10, 11]:
        return 'Outono'
    else:
        return 'Inverno'

data['Estação'] = data['Mês'].apply(estacao_mianmar_4)
print(data['Percentual de Margem Bruta'].unique())
print(data.info())
data.to_csv('data/data_limpa.csv', index=False)


