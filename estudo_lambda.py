import pandas as pd

#Função para calcular cubo
def eleva_cubo(x):
    return x ** 3

#Lambda para calcular cubo. Usa-se o labda para funções 
# simples que podem ser incluídas no código em uma linha
eleva_cubo_lambda = lambda x: x ** 3
#Não precisa declarar assim, ams declaramos por fim de estudos

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({"numeros": [1,2,3,4,5,12,52]})

df["cubo_funcao"] = df["numeros"].apply(eleva_cubo)
df["cubo_lambda"] = df["numeros"].apply(lambda x: x **3)

print(df)