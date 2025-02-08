import requests as req
from bs4 import BeautifulSoup
import pandas as pd

#modulo para puxar informações de sites

pagina = 'https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/'



response = req.get(pagina) #aqui temos a requisição para pegar (get) as infos da página web
print(response.text[:200]) #falamos que queremos o texto e até qual caracter
print(response) #printa a requisição (se deu certo)


sopa = BeautifulSoup(response.text, features='html.parser')
print(sopa.prettify()[:200])

url_dados = pd.read_html(pagina)

print(url_dados[1].head(10))