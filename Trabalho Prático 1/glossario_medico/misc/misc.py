import re
import json

f = open("glossario_medico/misc/misc.xml", "r", encoding="utf-8")
texto = f.read()
texto = re.sub(r"</?text.*?>\d+</text>", "", texto) #retirar numeração das páginas
f.close()

texto = re.sub(r'\n<text .*? left="500" .*?>', r'', texto)
texto = re.sub(r'\n<text .*? left="138" .*?>', r'', texto)
texto = re.sub(r'\n<text .*? left="193" .*?>', r'', texto)
texto = re.sub(r'\n<text .*? left="444" .*?>', r'', texto)

texto = re.sub(r"</?text.*?>", r"", texto)
texto = re.sub(r"</?page.*?>", r"", texto)
texto = re.sub(r"- ", r"", texto)
texto = re.sub(r"  ", r" ", texto)

texto = re.sub(r"</?i.*?>", r"", texto)
texto = re.sub(r"\n{2,}", r"\n", texto)
texto = re.sub(r"([^>])\n([^<])", r"\1,\2", texto)

categorias = re.findall(r"<b>(.+?)</b>\n([^<]+)\n", texto)
dic_categorias = {}
for c in categorias:
    dic_categorias[c[0].lower()] = c[1].split(",")

file_out = open("glossario_medico/misc/misc_limpo.xml", "w", encoding="utf8")
file_out.write(texto)
file_out.close()

file_out = open("glossario_medico/misc/misc.json", "w", encoding="utf8")
json.dump(dic_categorias, file_out, indent=4, ensure_ascii=False)
file_out.close()