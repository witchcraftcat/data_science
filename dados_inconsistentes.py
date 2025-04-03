import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("clientes.csv")

print(df.head())

#Mascarar dados
df["cpf_mascara"] = df["cpf"].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2]}')

#corrigir datas
df["datas"] = pd.to_datetime(df["datas"], format="%Y-%m-%d", errors="coerce")

data_atual = pd.to_datetime("today")
df["data_atualizada"] = df["data"].where(df["data"] <= data_atual, pd.to_datetime("1900-01-01")) #se o valor for maior que data atual, ele troca para o que vem depois da vírgula
df["data_ajustada"] = data_atual.year - df["data_atualiada"].dt.year
df["idade_ajustada"] -=((data_atual.month <= df["data_atualizada"].dt.month) & (data_atual.day < df["data_atualizada"].dt.day)).astype(int)
df.loc[df["idade_ajustada"] > 100, "idade_ajustada"] = np.nan

#Corrigir campo com múltiplas informações
df["endereco_curto"] = df["endereco"].apply(lambda x: x.split("\n")[0].strip())
df["bairro"] = df["endereco"].apply(lambda x: x.split("\n")[1].strip() if len(x.split("\n")) > 1 else "Desconhecido")
df["estado_sigla"] = df["endereco"].apply(lambda x: x.split(" / ")[-1].strip() if len(x.split("\n")) > 1 else "Desconhecido")

#Verificando a formatação do endereço
df["endereco_curto"] = df["endfereco_curto"].apply(lambda x: "endereço inválido" if len(x) >50 or len(x) < 5 else x)


#Corrigir dados errôneos
df["cpf"] = df["cpf"].apply(lambda x: x if len(x) == 14 else "Cpf Inválido")

estados_br = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]
df["estado_sigla"] = df["estado_sigla"].str.upper.apply(lambda x: x if x in estados_br else "Desconhecido")

print("dados tratados: \n", df.head())

df["cpf"] = df["cpf_mascara"]
df["idade"] = df["idade_ajustada"]
df["endereco"] = df["endereco_curto"]
df["estado"] = df["estado_sigla"]

df_salvar = df[["nome", "cpf", "idade", "data", "endereço", "bairro", "estado"]]
df_salvar.to_csv("clientes2.csv", index=False)