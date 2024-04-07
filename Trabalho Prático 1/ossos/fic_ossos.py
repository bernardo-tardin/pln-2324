import re
import json

file = open("ossos/ossos.xml", "r", encoding = "utf-8")
text = file.read()

#Remoção de tags
text = re.sub(r"<text.+font=\"4\"><b>A</b></text>([\s\S]*?)<text[^>]*font=\"5\"><b>o</b></text>", r"", text) #menu vertical
text = re.sub(r".+<a.+\n.+", r"", text) #repetição de SUMÁRIO
text = re.sub(r"</page>\n<page.+>(\n)+", r"", text) 
text = re.sub(r".+<b>\d+</b>.+\n+", r"", text) #números das páginas
text = re.sub(r"</?text.*?>", r"", text) 

#Correção de anomalias
text = re.sub(r"(</b>\n<b>([ÂA-Z:]))+", r"\2", text) #descrições que continuavam numa nova linha
text = re.sub(r"(\d\.\d?)\s\n<b>(.+)", r"<b>\1 \2", text) #subsecções sem estarem a bold
text = re.sub(r"</b>\n<b>(\((C7)\).+)", r"\1", text) #continuação da descrição de VÉRTEBRAS CERVICAIS ATÍPICAS encontrava-se numa nova linha
text = re.sub(r"\n<i>(.+)</i>", r"\1", text) #remoção das tags itálico como em Fascia Transversalis
text = re.sub(r"\s([a-z]\))", r"\n\1", text) #linha que possuía duas alíneas: a segunda alínea passou para nova linha
text = re.sub(r"\n(\d\.\d+\.?.+)\n([A-Z]+)", r"\n<b>\1\2</b>", text) #subsecções que não se encontravam a bold e a descrição continuava numa nova linha

text = re.sub(r"\n(\d\.\d+\.?.+)", r"\n<b>\1</b>", text) #subsecções que não se encontravam a bold e estavam apenas numa linha
text = re.sub(r"\nj\s", r"\nj) ", text) #alínea j não tinha um parênteses a delimitar
text = re.sub(r"\n((<b>)?(?![a-z]\))([a-záí\s\(\)\.]+)(</b>)?)", r"\3", text) #terminologias cuja descrição continuava numa nova linha e podiam estar a bold ou não (fibulares e tíbia)
text = re.sub(r"\n<b>1.25.+</b>", r"", text) #remoção de 1.25 e 1.26 que não possuem gabarito
text = re.sub(r"([a-z]\s\))", r"\n\1", text) #alíneas, do tipo letra+espaço, numa mesma linha como em oblíquaf ) Corpo
text = re.sub(r"([a-z\)])(([a-z]\d)\))", r"\1\n\2", text) #alíneas, do tipo letra + número, numa mesma linha como em Músculo Procerod1) ...

#Sintaxe de extração definida
text = re.sub(r"\n(([a-z]\s?\))|(([a-z][0-9])\s?\))|([A-Z]\s?\)))", r"\n@", text) #terminologias
text = re.sub(r"<b>([^\d]+)</b>", r"&\1", text) #títulos principais
text = re.sub(r"<b>\d\.?\s?([A-Z\sÂÓÁÉÊÔÚÇ]+)</b>", r"%\1", text) #secções
text = re.sub(r"<b>\d\.\d\.\d\.?\s?(.+)</b>", r";\1", text) #subsecções de subsecções
text = re.sub(r"<b>\d\.\s?\d+\.?\s?(.+)</b>", r"#\1", text) #subsecções

titulos = re.findall(r"&(.+)", text)
seccoes = re.findall(r"%(.+)", text)
subseccoes = re.findall(r"#(.+)", text)
sub_subseccoes = re.findall(r";(.+)", text)

teste = open("ossos/novo.txt", "w", encoding = "utf-8")
teste.write(text)
file.close()
teste.close()

#Criação de dicionário
dic = {}
cur_titulo = None
cur_seccao = None
cur_subseccao = None
cur_sub_subseccao = None

f = open("ossos/novo.txt", "r", encoding = "utf-8")
content = f.read()
content = content.split("\n")

for line in content:
    if line[1:].strip() in titulos:
        cur_titulo = line[1:].strip()
        dic[cur_titulo] = {}
    
    elif line[1:].strip() in seccoes:
        cur_seccao = line[1:].strip()
        dic[cur_titulo][cur_seccao] = {}

    elif line[1:].strip() in subseccoes:
        cur_subseccao = line[1:].strip()
        dic[cur_titulo][cur_seccao][cur_subseccao] = []

    elif line[1:].strip() in sub_subseccoes:
        cur_sub_subseccao = line[1:].strip()
        if cur_sub_subseccao not in dic[cur_titulo][cur_seccao][cur_subseccao]:
            dic[cur_titulo][cur_seccao][cur_subseccao] = {cur_sub_subseccao: []}

    elif line.startswith("@"):
        if cur_titulo in dic and cur_seccao in dic[cur_titulo] and cur_subseccao in dic[cur_titulo][cur_seccao]:
            if isinstance(dic[cur_titulo][cur_seccao][cur_subseccao], list):
                dic[cur_titulo][cur_seccao][cur_subseccao].append(line[1:].strip())
            elif isinstance(dic[cur_titulo][cur_seccao][cur_subseccao], dict):
                dic[cur_titulo][cur_seccao][cur_subseccao][cur_sub_subseccao].append(line[1:].strip())

final = open("ossos/dicionario.json", "w", encoding="utf-8")
json.dump(dic, final, indent=4, ensure_ascii=False)
final.close()

