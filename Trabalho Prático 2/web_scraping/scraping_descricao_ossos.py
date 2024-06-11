from bs4 import BeautifulSoup
import requests
import json
import re

url_base = "https://pt.wikipedia.org/wiki/Lista_de_ossos_do_esqueleto_humano"

html_doc = requests.get(url_base)
soup = BeautifulSoup(html_doc.text, 'html.parser')

url_pages = []

div = soup.find("div", class_="mw-body-content")

li_elements = div.find_all("li")

for li in li_elements:
    if li.get("id") is None and li.get("class") is None:
        ancoras = li.find_all("a")
        for ancora in ancoras:
            if ancora != None:
                if ancora.text.strip() == "cuneiforme intermédio" or ancora.text.strip() == "cuneiforme lateral" or ancora.text.strip() == "cuneiforme medial":
                    link_final = "https://pt.wikipedia.org/wiki/Cuneiforme_(anatomia)"
                    url_pages.append(link_final)
                else:
                    link = ancora["href"]
                    link_final = "https://pt.wikipedia.org" + link
                    if link_final not in url_pages:
                        url_pages.append(link_final)

ossos_info = {}
c = 0
for l in url_pages:

    page_doc = requests.get(l)
    soup_page = BeautifulSoup(page_doc.text, 'html.parser')

    div_nome = soup_page.find("h1", class_="mw-first-heading")
    nome = div_nome.text.strip()

    if nome == "Cuneiforme (anatomia)":
        c+=1
        div_paragrafo = soup_page.find("div", class_="mw-parser-output")
        paragrafos = div_paragrafo.find_all("p")
        descricao = paragrafos[3].text.strip()
        if c == 1:
            ossos_info["Cuneiforme medial"]=descricao
        elif c == 2:
            ossos_info["Cuneiforme intermédio"]=descricao
        else:
            ossos_info["Cuneiforme lateral"]=descricao

    else:

        div_paragrafo = soup_page.find("div", class_="mw-parser-output")

        if div_paragrafo:
            paragrafos = div_paragrafo.find_all("p")
            
            for i in range(len(paragrafos)):
                if paragrafos[i].get_text() != "\n":
                    texto = paragrafos[i].get_text().strip()
                    texto = re.sub(r"\[[^\]]+\]", r" ", texto)
                    texto = re.sub(r"\n", r" ", texto)
                    if re.search(r"(.+):$", texto):
                        ul_topicos = div_paragrafo.find("ul")
                        topicos = ul_topicos.find_all("li")
                        for i in range(len(topicos)):
                            if i == (len(topicos)-1):
                                texto += topicos[i].a.text.strip()
                            else:
                                texto += topicos[i].a.text.strip() + " | "
                        break
                    else:
                        break

        ossos_info[nome] = texto

f = open("ossos_info.json", "w", encoding="utf-8")
json.dump(ossos_info, f, indent=4, ensure_ascii=False)
f.close()