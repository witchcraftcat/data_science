import pandas as pd

df = pd.read_csv("clientes.csv")

#Verificar os primeiros e últimos registros
print(df.head().to_string())

print(df.tail().to_string())

#verificar quantidade de linhas e colunas
print("Quantidade: ", df.shape)

#Verificar tipos de dados
print("Tipagem de dados: \n", df.dtypes)

#Checar valores nulos
print("Valores nulos: \n", df.isnull().sum())