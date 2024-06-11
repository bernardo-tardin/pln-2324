import json

with open('doencas_cuf.json', "r", encoding='utf-8') as f:
    doencas_cuf = json.load(f)

with open('dicionario_doencas.json', "r", encoding='utf8') as f:
    doencas_dic = json.load(f)

with open('traduções_doenças.json', "r", encoding='utf-8') as f:
    traducoes =json.load(f)

i=0
doencas = {}
for doenca in doencas_cuf.keys():
    i+=1
    doencas[doenca] = {'Definição':doencas_cuf[doenca], 'Categoria':['Doenças']}

for d in doencas_dic:
    if d not in doencas:
        i+=1
        doencas[d] = {'Definição': doencas_dic[d],'Categoria':['Doenças']}
print(i)

with open('glossario.json', "r", encoding='utf8') as f:
    doencas_glossario = json.load(f)

for termo in doencas_glossario.keys():
    i+=1
    if 'Categoria' in doencas_glossario[termo]:
        if 'Doenças' in doencas_glossario[termo]['Categoria'] and termo not in doencas:
            doencas[termo] = {'Definição':doencas_glossario[termo]['Definição'], 'Categoria':['Doenças']}

for doenca in doencas:
    if doenca in traducoes:
        doencas[doenca]['Tradução'] = traducoes[doenca]
    else:
        doencas[doenca]['Tradução'] = 'Sem tradução'

lista = list(doencas.keys())
lista.sort()
dic_doencas = {i: doencas[i] for i in lista}

print(i)
with open('doencas_uniao.json', "w", encoding='utf-8') as out:
    json.dump(doencas, out, ensure_ascii=False, indent=4)