import re
import json

f = open("glossario_medico/glossario/glossario.xml", "r", encoding="utf-8")
texto = f.read()
texto = re.sub(r"</?text.*?>\d+</text>", r"", texto) #retirar numeração das páginas
texto = re.sub(r"</?text.*?>\w</text>", r"", texto) #retirar header de nova letra 
texto = re.sub(r"(</?text.*?></text>\n){2,4}</page>", r"", texto) #para eliminar os conceitos que aparecem no header de cada página
texto = re.sub(r"</?text.*?>", r"", texto)
texto = re.sub(r"</?page.*?>", r"", texto)
texto = re.sub(r"</?fontspec.*?>", r"", texto)
texto = re.sub(r"</?i.*?>", r"", texto)

texto = re.sub(r"Economia de Saúde", r"Economia da Saúde", texto)
texto = re.sub(r"Economia em Saúde", r"Economia da Saúde", texto)

texto = re.sub(r"\n", r" ", texto)
texto = re.sub("- ", "", texto)
texto = re.sub("  ", " ", texto)
texto = re.sub(r"</b> <b>", r"", texto)
texto = re.sub("Categoria :", "Categoria:", texto)
f.close()

cfile = open("glossario_medico/categorias/categorias.json", "r", encoding="utf8")
categorias = json.load(cfile)
cfile.close()

for categoria in categorias:
    texto = re.sub(categoria, "@"+categoria+"@", texto)

texto = re.sub("@Epidemiologia@ descritiva", "Epidemiologia descritiva", texto)
texto = re.sub("Categoria: Doenças", "Categoria: @Doenças@", texto)
texto = re.sub("@  Doenças", "@ @Doenças@", texto)
texto = re.sub("  ", " ", texto)
texto = re.sub("@ @", " & ", texto)

termos_referência = re.findall("<b>([^<]+)</b> (Ver [^<]+)", texto)
termos = re.findall("<b>([^<]+?)</b> Categoria: @(.+?)@([^<]+)", texto)
dic_termos = {}
for termo in termos:
    categorias = termo[1].split("&")
    dic_termos[termo[0]] = {"Categoria": categorias, "Definição": termo[2]}

for termo in termos_referência:
    dic_termos[termo[0]] = termo[1]


chaves = list(dic_termos.keys())
chaves.sort()
dic_ordenado = {c: dic_termos[c] for c in chaves}

file_out = open("glossario_medico/glossario/glossario_limpo.xml", "w", encoding="utf8")
file_out.write(texto)
file_out.close()


file_out = open("glossario_medico/glossario/glossario.json", "w", encoding="utf8")
json.dump(dic_ordenado, file_out, indent=4, ensure_ascii=False)
file_out.close()



