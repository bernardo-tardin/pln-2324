import re
import json

f = open("glossario_medico/categorias/categorias.xml", "r", encoding="utf-8")
texto = f.read()
texto = re.sub(r"</?text.*?>\d+</text>", r"", texto) #retirar numeração das páginas
texto = re.sub(r"</?text.*?>", r"", texto)
texto = re.sub(r"</?page.*?>", r"", texto)

texto = re.sub(r"\n", r" ", texto)
texto = re.sub(r"- ", r"", texto)
texto = re.sub(r"  ", r" ", texto)
f.close()

categorias = re.findall("<b>(.+?)</b>([^<]+)", texto)

file_categorias = open("glossario_medico/misc/misc.json", "r", encoding="utf-8")
termos_categoria = json.load(file_categorias)
file_categorias.close()

dic_categorias = {}
for k in categorias:
    categoria = k[0].lower()
    if "Doenças" in k[0]:
            dic_categorias[k[0]] = {"Descrição": k[1], "Termos": termos_categoria["doenças"]}
    elif categoria in termos_categoria:
        dic_categorias[k[0]] = {"Descrição": k[1], "Termos": termos_categoria[categoria]}
    else:
        dic_categorias[k[0]] = {"Descrição": k[1]}


file_out = open("glossario_medico/categorias/categorias.json", "w", encoding="utf-8")
json.dump(dic_categorias, file_out, indent=4, ensure_ascii=False)
file_out.close()