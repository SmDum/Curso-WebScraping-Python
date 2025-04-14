import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_acao = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get('https://investidor10.com.br/acoes/', headers=headers)

if response.status_code != 200:
    print(f"Erro ao acessar o site: {response.status_code}")
    exit()

content = response.content
site = BeautifulSoup(content, 'html.parser')


acoes = site.findAll('div', attrs={'class': 'actions-card'})

for acao in acoes:
    # Buscar o nome da empresa dentro de cada 'acao'
    nome_company = acao.find('h3', attrs={'class': 'actions-title'})
    nome_company = nome_company.text.strip() if nome_company else 'Nome da empresa não encontrado'

    # Buscar os indicadores dentro de cada 'acao'
    indicadores = acao.findAll('div', attrs={'class': 'actions-codes indicators'})
    
    # Verificar se há indicadores e extrair os valores corretamente
    if indicadores:
        spans = indicadores[0].findAll('span')
        pl = spans[1].text.strip() if len(spans) > 1 else 'P/L não encontrado'
        pvp = spans[3].text.strip() if len(spans) > 3 else 'P/VP não encontrado'
        dy = spans[5].text.strip() if len(spans) > 5 else 'DY não encontrado'
        roe = spans[7].text.strip() if len(spans) > 7 else 'ROE não encontrado'
    else:
        pl = pvp = dy = roe = 'Indicador não encontrado'
        
    #print('\n\n\n')
    #print(f"Empresa: {nome_company}")
    #print(f"P/L: {pl}")
    #print(f"P/VP: {pvp}")
    #print(f"DY: {dy}")
    #print(f"ROE: {roe}")
    # Adicionar os dados da ação à lista
    lista_acao.append([nome_company, pl, pvp, dy, roe])

acoes = pd.DataFrame(lista_acao, columns=['Empresa','P/L','P/VP','DY','ROE'])

acoes.to_excel('acoes.xlsx', index=False)
    
print(acoes)
