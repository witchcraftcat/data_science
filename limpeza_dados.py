import pandas as pd

df = pd.read_csv("clientes.csv")

pd.set_option("display.width", None)
print(df.head())

#Remover dados
df.drop(labels="pais", axis=1, inplace = True) #removerá a coluna (axis 1) que chama país
df.drop(labels=2, axis=0, inplace=True)

#Normalizar campos de texto
df["nome"] = df["nome"].str.title()
df["endereco"] = df["endereco"].str.lower()
df["estado"] = df["estado"].str.upper()

#Converter tipos de dados
df["idade"] = df["idade"].astype(int)

#Tratar valores nulos
df_fillna = df.fillna(0)
df_dropna = df.dropna()
df_dropna4 = df.dropna(thresh=4) #dropa valores que tenham mais do que 4 valores nulos
df = df.dropna(subset=["cpf"]) #reove registros com o subset. Por ex meplo, removerá as linhas com cpf nulo

print("Valores nulos:\n ", df.isnull().sum())
print("Quantidade de registros nulos com fillna: ", df_fillna.isnull().sum().sum())
print("Quantidade de registros nulos com dropna: ", df_dropna.isnull().sum().sum())
print("Quantidade de registros nulos com dropna4: ", df_dropna4.isnull().sum().sum())
print("Quantidade de registros nulos de CPF: ", df.isnull().sum().sum())

df.fillna(value={"estado": "Desconhecido"}),
df["endereco"] = df["endereco"].fillna("endereço não informado"),
df["idade_corrigida"] =df["idade"].fillna(df["idade"].mean())

#Tratar formato de dados. è importante fazer
df["data_corrigida"] = pd.to_datetime(df["data"], format='%d/%m/%Y', errors="coerce")

#Tratar dados duplicados
print("Quantidade de registros atual: ", df.shape[0]) #linha ou coluna. Linha =0, coluna =1

df.drop_duplicates()
df.drop_duplicates(subset="cpf", inplace = True)
print("Quantidade de registros removendo as duplicadas: ",df.shape[0]) #ou pode usar lend(df)

print("Dados limpos: \n", df)

#salva dataframe
df["data"] = df["data_corrigida"]
df["idade"] = df["idade_corrigida"]

df_salvar = df["nome", "cpf", "idade", "data", "endereco", "estado"]
df_salvar.to_csv("clientes_limpeza.csv", index=False)

print("Novo dataframe: \n", pd.read_csv("clientes_limpeza.csv"))

