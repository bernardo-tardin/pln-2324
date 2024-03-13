import json
import re

file = open('termos_traduzidos.txt', encoding='utf-8')
texto = file.read()

portugues_ingles = re.findall(r'(.+)@(.+)', texto)
dicionario = {x[0].strip(): x[1].strip() for x in portugues_ingles}

file_out = open('conceitos_ingles.json', 'w')
json.dump(dicionario, file_out,indent=4,ensure_ascii=False)
file_out.close()