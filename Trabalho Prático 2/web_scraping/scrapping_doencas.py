from bs4 import BeautifulSoup
import requests
import json
import random
import time


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
           'Referer': 'https://www.google.pt/'}
url = 'https://www.cuf.pt/saude-a-z'

def doenca(url_doenca, header):
    html = requests.get(url_doenca, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    nome_h1 = soup.find('h1', class_='field--name-field-title')
    nome=''
    if nome_h1:
        nome = nome_h1.get_text().strip()
    descricao_div = soup.find('div', class_='field--name-field-tabs')
    descricao = ''
    if descricao_div:
        descricao_paragrafo = descricao_div.p
        if '\u00A0' in descricao_paragrafo:
            next_sibling = descricao_paragrafo.next_sibling
            while next_sibling and next_sibling.name is None:  
                next_sibling = next_sibling.next_sibling
            if next_sibling:
                descricao = next_sibling.get_text().strip()
        else:
            descricao = descricao_paragrafo.get_text().strip()
    
    elif soup.find('div', class_='field--name-field-text-html'):
        descricao_paragrafo = soup.find('div', class_='field--name-field-text-html').p
        if '\u00A0' in descricao_paragrafo:
            next_sibling = descricao_paragrafo.next_sibling
            while next_sibling and next_sibling.name is None:  
                next_sibling = next_sibling.next_sibling
            if next_sibling:
                descricao = next_sibling.get_text().strip()
        else:
            descricao = descricao_paragrafo.get_text().strip()
    return (nome, descricao)

def pagina(url_pagina, headers):
    html = requests.get(url_pagina, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    links_div = soup.find_all('div', class_='views-row') 
    dicionario = {}
    for l in links_div:
        if l.div.span.a['href']:
            url_doenca = 'https://www.cuf.pt' + l.div.span.a['href']
            doencas = doenca(url_doenca, headers)
            dicionario[doencas[0]] = doencas[1]  
    return dicionario

def scrapper(url, headers):
    dicionario = pagina(url, headers=headers)
    i=1
    while i<17:
        print("%d/17" %i)
        delta = random.randint(0,5)
        time.sleep(delta)
        url_proximo = url + "/" + '?page=' + str(i)
        dicionario = dicionario | pagina(url_proximo, headers=headers)
        i+=1

    return dicionario

doencas = scrapper(url, headers=headers)
with open("doencas_cuf.json", "w", encoding='utf-8') as f:
    json.dump(doencas, f, indent=4, ensure_ascii=False)

