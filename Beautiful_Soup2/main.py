import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')
content = response.content
site = BeautifulSoup(content, 'html.parser')

#HTML da Notícia
noticias = site.findAll('div', attrs={'class':'feed-post bstn-item-shape type-materia'})

for noticia in noticias:
    
    #Título da Notícia
    titulo = noticia.find ('a', attrs={'class':'feed-post-link'})

    #Subtitulo da Notícia
    subtitulo = noticia.find('a', attrs={'class':'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})
    
    #print(titulo.text)
    #print(titulo['href'])
    if(subtitulo):
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '',titulo['href']])
        
news = pd.DataFrame(lista_noticias, columns=['Título','Subtítulo','Link'])

news.to_csv('noticias.xlsx', index=False)
        
#print(news)