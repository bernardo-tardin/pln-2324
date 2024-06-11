from bs4 import BeautifulSoup
import requests
import json
import re

html = requests.get('https://pt.wikipedia.org/wiki/Lista_de_músculos_do_corpo_humano')


musculos = {}
soup = BeautifulSoup(html.text, 'html.parser')
content_div = soup.find('div', class_='mw-body-content')
musc = content_div.find_all('li')
for m in musc:
    if m.find('a'):
        musculo = m.find('a').text
        if musculo[0] == "m":
            musculo_dic = {}
            url = m.find('a')['href']
            html2 = requests.get('https://pt.wikipedia.org' + url)
            soup2 = BeautifulSoup(html2.text, 'html.parser')
            if soup2.find('div', class_='mw-content-ltr mw-parser-output'):
                text = soup2.find('div', class_='mw-content-ltr mw-parser-output')
                paragraphs = text.find_all('p')

                #Correção de anomalias

                m_parents = []
                for p in paragraphs:
                    parents = []
                    for parent in p.parents:
                        parents.append(parent.name)
                    m_parents.append(parents)
                for elem in m_parents:
                    if elem[0] == "div":
                        i = m_parents.index(elem)
                        break
                
                if musculo == "músculo transverso profundo do períneo":
                    i = 1
                
                if musculo == "músculo extensor do dedo mínimo":
                    i = 4

                desc = paragraphs[i].text.strip()
                desc = desc.replace('\n', '')
                desc = re.sub(r'\[.*?\]', '', desc)
                desc = re.sub(r'[;:]', '.', desc)


            else:
                desc = "Sem descrição"
            musculo_dic['DESC']=desc
            musculos[musculo] = musculo_dic


with open('TP2/musculos.json', 'w') as f:
    json.dump(musculos, f, indent=4, ensure_ascii=False)

