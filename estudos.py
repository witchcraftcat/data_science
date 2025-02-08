#Entendendo a função .text[]



#Suponhamos que temos este texto e esta lista


texto = "Mais comme dit le dicton: Plutôt qu’être seul mieux vaut être mal accompagné."

lista =list(range(1,20))



#Aqui, pega desde o começo até o caracter 11
subtexto = texto[:24]
print(subtexto)

sublista = lista[:11]
print(sublista)


#Aqui imprime desde o caracter 11 - contando espaços também - até o fim
subtexto = texto[11:]
print(subtexto)

sublista = lista[11:]
print(sublista)


#Imprime desde o 5
sublista = lista[5:] 
print(sublista)


#Aqui, imprime os últimos 5 caracteres


subtexto = texto[-51:]      
print(subtexto)

sublista = lista[-5:] 
print(sublista)

#entendendo BeautifulSoup

from bs4 import BeautifulSoup
import requests as req
import pandas as pd

nova_era = "https://www.novaerarpg.com/t6841p160-um-mundo-melhor-para-poucos"
response = req.get(nova_era)
print(response)
#print(response.text[:1000])

sopa = BeautifulSoup(response.text, features="html.parser")
#print(sopa.text[:1000])
print(sopa.prettify()[:1000])

url_nova = pd.read_html(nova_era)
print(pd.read_html(response.text))

#https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data/data