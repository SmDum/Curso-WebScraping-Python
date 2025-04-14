import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')
content = response.content
site = BeautifulSoup(content, 'html.parser')

#HTML da Notícia
noticia = site.find('div', attrs={'class':'feed-post bstn-item-shape type-materia'})

#Título da Notícia
titulo = noticia.find ('a', attrs={'class':'feed-post-link'})

#Subtitulo da Notícia
subtitulo = noticia.find('a', attrs={'class':'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})

print(noticia.prettify())
print(titulo.text)
print(subtitulo.text)
