import re
import json

f = open("glossario_medico/siglas/siglas.xml", "r", encoding="utf-8")
texto = f.read()
texto = re.sub(r"</?text.*?>\d+</text>", "", texto) #retirar numeração das páginas
texto = re.sub(r"</?text.*?>", r"", texto)
texto = re.sub(r"</?page.*?>", r"", texto)
texto = re.sub(r"</?fontspec.*?>", r"", texto)

texto = re.sub(r"\n", r" ", texto)
texto = re.sub(" –", "", texto)
texto = re.sub("  ", " ", texto)

siglas = re.findall("<b>(.+?)</b>([^<]+)", texto)

dic_siglas = dict(siglas)
del dic_siglas["Siglas"]

file_out = open("glossario_medico/siglas/siglas.json", "w", encoding="utf-8")
json.dump(dic_siglas, file_out, indent=4, ensure_ascii=False)
file_out.close()