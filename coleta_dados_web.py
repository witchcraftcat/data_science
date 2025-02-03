#Declarando a variável e importando o que preciso

import requests as rq
from bs4 import BeautifulSoup


url = "https://wiki.python.org.br/AprendaMais"

#fazendo os requests:

request = rq.get(url) #"puxando o endereço da web."

sopa = BeautifulSoup(request.text, features='html.parser') #pegando o que foi puxado e arrumando para ser exibido

#vamos agora fazer um for que puxará todas as linhas do site e verá se existe um h2:

for linha_texto in sopa.find_all("h2"): 
    titulo_h2 = linha_texto.text.strip()
    print("Título: ", titulo_h2)

# fazer um for para contar quantos h2 e p tçen no documento:

contar_titulos = 0  #devemos sempre declarar as variáveis
contar_paragrafo = 0 

for linha_texto in sopa.find_all(["h2","p"]):
    if linha_texto.name == "h2":
        contar_titulos += 1
    elif linha_texto.name == "p":
        contar_paragrafo += 1

print(f'O número de títulos h2 é: {contar_titulos}')
print(f'O número de parágrafos é: {contar_paragrafo}')

for linha_texto in sopa.find_all(["h2","p"]):
    if linha_texto.name == "h2":
        titulo = linha_texto.text.strip()
        print(f'Título: {titulo}')
    elif linha_texto.name == "p":
        paragrafo = linha_texto.text.strip()
        print(f'Parágrafo: {paragrafo}')

#Tags alinhadas: uma dentro da outra 

for linha_texto in sopa.find_all("h2"):
    print(f'Título: {linha_texto.text.strip()}')
    for link in linha_texto.find_next_siblings("p"):
        for a in link.find_all("a", href = True):
            print(f'Link: {a.text.strip()} | URL: {a["href"]}')