import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'
produto = input('Digite o produto que deseja buscar: ')

response = requests.get(url_base + produto)

site = BeautifulSoup(response.text, 'html.parser')

itens = site.findAll('li', attrs={'class':'ui-search-layout__item'})

for item in itens:
    titulo = item.find('h3', attrs={'class':'poly-component__title-wrapper'})
    preco = item.find('span', attrs={'class':'andes-money-amount andes-money-amount--cents-superscript'})
    link =  item.find('a', attrs={'class':'poly-component__title'})['href']

    print('Nome :' , titulo.text)
    print('Preço :' , preco.text)
    print('Link :' , link)
    print('\n\n\n')