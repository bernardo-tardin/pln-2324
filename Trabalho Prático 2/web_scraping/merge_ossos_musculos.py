import json

with open('TP2/musculos.json', 'r') as f:
    musculos = json.load(f)

with open('TP2/ossos_uniao.json', 'r') as g:
    dicionario = json.load(g)

musculos_list = []


for musculo in musculos:
    musculo = musculo.lower()
    for parte in dicionario:
        for espec in dicionario['SISTEMA MUSCULAR']:
           for categoria in dicionario['SISTEMA MUSCULAR'][espec]:
            for m in dicionario['SISTEMA MUSCULAR'][espec][categoria]:
                if type(m) != dict:
                    musculo_lw = m.lower()
                    if musculo in musculo_lw:
                        i = dicionario['SISTEMA MUSCULAR'][espec][categoria].index(m)
                        if musculos[musculo]['DESC'] != "Sem descrição":
                            dic = {}
                            dic[m] = musculos[musculo]['DESC']
                            dicionario['SISTEMA MUSCULAR'][espec][categoria][i] = dic
                    
                    
with open('TP2/ossos_uniao.json', 'w') as f:
    json.dump(dicionario, f, indent=4, ensure_ascii=False)

                       

