import re
import json

file = open('Minidicionario_de_Cardiologista/cardiologia.xml', 'r', encoding="utf8")
lines = file.readlines()


# Limpeza de linhas vazias
for i, line in enumerate(lines):
    if re.search(r'font="8"> <.*', line):
        lines.pop(i)


#Marcar o início dos termos
previous_line = ""

for i,line in enumerate(lines):
    if 'font="7"><b>' in line and ('font="7"><b>' not in previous_line and 'font="11"><b>' not in previous_line):
        line = re.sub(r'font="7"><b>(.+?)(</b>.*)',r'font="7"><b>@\1\2', line)
        lines[i] = line

    if 'font="13"><b>' in line and 'font="13"><b>' not in previous_line:
        line = re.sub(r'font="13"><b>(.+?)(</b>).*',r'font="13"><b>@\1\2', line)
        lines[i] = line
        
    previous_line = line

#Marcar o final dos termos

for i,line in enumerate(lines):
    next_line = lines[i+1] if i+1 < len(lines) else ""
    if 'font="8"' in next_line:
        if 'font="7"><b>' in line in line:
            line = re.sub(r'font="7"><b>(.+?)(</b>.*)',r'font="7"><b>\1@\2', line)
            lines[i] = line
        if 'font="13"><b>' in line:
            line = re.sub(r'font="13"><b>(.+?)(</b>.*)',r'font="13"><b>\1@\2', line)
            lines[i] = line

# Selecionar os termos
text = ''.join(lines)
termos = re.findall(r'(<b>@[^@]+@</b>)', text)
lista_termos = []
for t in termos:
    termo = ""
    result = re.findall(r'<b>(.*?)</b>', t)
    for res in result:
        termo += res
    termo = termo[:-1]
    termo = termo.strip()
    termo = termo.replace('@','')
    if termo[-1] == '–':
        termo = termo[:-1]
    termo = termo.strip()
    lista_termos.append(termo)


# Marcar o ínicio das traduções
    
previous_line = ""

for i,line in enumerate(lines):
    if 'font="8">' in line and ('font="8">' not in previous_line and 'font="14">'not in previous_line):
        line = re.sub(r'font="8">(.+?)(.*)',r'font="8">@\1\2', line)
        lines[i] = line
    previous_line = line

# Marcar o final das traduções

for i,line in enumerate(lines):
    next_line = lines[i+1] if i+1 < len(lines) else ""
    if 'font="8"' in line:
        if 'font="8"' not in next_line and 'font="14">' not in next_line:
                line = re.sub(r'font="8">(.+?)(.*)</text>',r'font="8">\1\2@</text>', line)
                lines[i] = line
        
# Selecionar as traduções
                
text = ''.join(lines)
traducoes = re.findall(r'(font="8">@[^@]+@</text>)', text)
lista_traducoes = []
for trad in traducoes:
    traducao = ""
    result = re.findall(r'>(.*)</text>', trad)
    for res in result:
        if "@" in res:
            res = res.replace('@','')
        traducao += res
    traducao = traducao.strip()
    lista_traducoes.append(traducao)

# Divisão em sublists
en_pt_termos = lista_termos[:(len(lista_termos)//2)+1]
en_pt_traducoes = lista_traducoes[:(len(lista_termos)//2)+1]
pt_en_termos = lista_termos[(len(lista_termos)//2)+1:]
pt_en_traducoes = lista_traducoes[(len(lista_termos)//2)+1:]

# Dicionário de traduções

dic_traduc = {'ingles-portugues': {}, 'portugues-ingles': {}}

for i in range(len(en_pt_termos)):
    dic_traduc['ingles-portugues'][en_pt_termos[i]] = en_pt_traducoes[i]

for i in range(len(pt_en_termos)):
    dic_traduc['portugues-ingles'][pt_en_termos[i]] = pt_en_traducoes[i]

# Salvar o dicionário em um arquivo json
file = open('Minidicionario_de_Cardiologista/dic_traduc.json', 'w', encoding='utf-8')
json.dump(dic_traduc, file, indent=4, ensure_ascii=False)