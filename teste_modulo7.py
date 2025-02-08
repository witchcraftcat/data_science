import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
#print(requisicao.text[:2000])

extracao = BeautifulSoup(requisicao.text, features= "html.parser")
print(extracao.prettify()[:2000])

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for linha_texto in extracao.find_all("article"):
    tag_h3 = linha_texto.find("h3")    
    if tag_h3:
        titulo = tag_h3.text.strip()
        print("Título: ", titulo)
    tag_p = linha_texto.find ("p", class_="price_color")
    if tag_p:
        preco = tag_p.text.strip()
        print("Preço: ", preco)
    livro ={"Título": titulo, "Preço": preco}
    print(livro)

    catalogo.append(livro)

print(catalogo)


for linha_texto in extracao.find_all("article"):
    tag_h3 = linha_texto.find("h3")    
    if tag_h3:
       contar_livros += 1
       
print(f'O total de livros é: {contar_livros}')
