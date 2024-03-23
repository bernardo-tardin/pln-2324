import json
import re

file_pt = open('conceitos.json', encoding='utf-8')
file = open('termos_traduzidos.txt', encoding='utf-8')
texto = file.read()

conceitos=json.load(file_pt)

portugues_ingles = re.findall(r'(.+)@(.+)', texto)
dicionario = {x[0].strip(): x[1].strip() for x in portugues_ingles}

res = {}
for conceito in conceitos:
    if conceito in dicionario:
        res[conceito] = {"descricao": conceitos[conceito], "traducao": {"EN": dicionario[conceito]} }
    else:
        res[conceito] = {"descricao": conceitos[conceito], "traducao": {}}

file_out1 = open('conceitos_trad.json', 'w')
json.dump(res, file_out1,indent=4,ensure_ascii=False)
file_out1.close()

file_out2 = open('conceitos_ingles.json', 'w')
json.dump(dicionario, file_out2,indent=4,ensure_ascii=False)
file_out2.close()

