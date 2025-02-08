import pandas as pd

#Vamos fazer uma lista: coleção de elementos de qualquer tipo
lista_nomes = ["Oliver", "Lex", "Claude", "Dylan"]
print("Lista de nomes: \n", lista_nomes)
print("2º nome: ", lista_nomes[1])

for nome in lista_nomes:
    print(nome)

for i, nome in enumerate(lista_nomes, start=1):
    print(f'{i}º nome: {nome}')

dicionario_pessoa = {
    "Nome": "Pânico Moral",
    "Idade": "Tão velha quanto o mundo",
    "Poder": "Super inteligência"
}

print("Dicionário de uma pessoa: ", dicionario_pessoa)
print("Nome da pessoa no dicionário: ", dicionario_pessoa["Nome"], " Idade: ", dicionario_pessoa["Idade"])

#Colocar um dicionário dentro de uma lista

dados_completos = [
    {"nome": "Oliver", "idade": 16, "poder": "Super inteligência"},
    {"nome": "Lex", "idade": 17, "poder": "Aranha"},
    {"nome": "Dylan", "idade": 35, "poder": "Imortalidade"},
]

#Dataframe: como arrumar os dados de maneira BIDIMENSIONAL
df = pd.DataFrame(dados_completos)
print("Data frame: \n", df)

#podemos selecionar apenas uma coluna dentro dos dados do dataframe:
print(df["nome"])
print(df[["nome","idade"]])

#seleciona linhas pelo ÍNDICE:
print("Primeira linha: \n", df.iloc[0])

#Adiconar nova coluna:
df["cidade"] = ["National City", "Nova York", "International City"]

#Adicionar novo registro:
df.loc[len(df)] = {
    "nome": "Claude",
    "idade": 42,
    "poder": "ladrão",
    "cidade": "National City"
}

#remover coluna (usa axis. Se fosse linha: axis =0). inplace = True é que remove a coluna e já atribui,s em precisar fazer df = df.drop.... etc
df.drop(labels="cidade", axis = 1, inplace= True)

#filtrar dados: puxamos a coluna que queremos e comparamos com o valor
filtro_idade = df[df["idade"]>=30]
print(filtro_idade)

#Salvar em csv. Pode ser salvo em outros formatos
#df.to_csv(path_or_buf="herois.csv", index=False)

#ler o arquivo csv no dataframe 
df_lido = pd.read_csv("herois.csv")
print("CSV LIDO: \n", df_lido)