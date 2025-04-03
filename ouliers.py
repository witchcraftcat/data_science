import pandas as pd
from scipy import stats

pd.set_option("display.width", None)

df = pd.read_csv("clientes.csv")

df_filtro_basico = df[df["idade"] > 100]

print("Filtro básico: \n", df_filtro_basico[["nome", "idade"]])

#identificar os outliers com Z-score
z_scores = stats.zscore(df["idade"].dropna())
outliers_z = df[z_scores >=3]
print("Outliers pelo Z-score: \n", outliers_z)

#Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df["idade"]) < 3)]

#Identificar outliers com IQR
q1 = df["idade"].quantile(0.25)
q3 = df["idade"].quantile(0.75)
iqr = q3 - q1

limite_baixo = q1 - 1.5 * iqr
limite_alto = q3 + 1.5 * iqr

print(f'Limites IQR: \n Baixo: {limite_baixo}\nAlto: {limite_alto}')

#Aqui está mostrando os outliers
outliers_iqr = df[(df["idade"] < limite_baixo) | (df["idade"]> limite_alto)]
print("Outliers pelo IQR:\n", outliers_iqr)

#Filtrar outliers com IQR (aqui vai tirar os valores de Outliers)
df_iqr = df[(df["idade"] >= limite_baixo) & df(["idade"] <= limite_alto)]

#Tratar campos de texto
df["nome"] = df["nome"].apply (lambda x: "Nome invalido" if isinstance(x, str) and len(x) > 50 else x)
print("Quantidade de registros com nome grandes:\n", df)

df["endereco"] = df["endereco"].apply(lambda x: "Endereço inválido" if len(x.split("\n")) < 3 else x)

print("Dados com outliers tratados:\n", df)

