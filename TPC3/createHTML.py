import re

f = open("dicionario_medico.txt", "r", encoding="utf-8")
texto=f.read()

texto=re.sub(r"\n\f",r" ",texto)
texto=re.sub(r"\n\n(.+)", r"\n\n@\1", texto)
texto=re.sub(r"@(.+)\n\n@", r"@\1\n", texto)
designacao_descricao = re.findall(r'@(.+)\n([^@]+)+',texto)


head = "<head>"
head += '<meta chartset="UTF-8">'
head += '<link rel=stylesheet href="style.css">'
head += "<title> Dicionário Médico </title>"


body = "<body>"

div_head = '<div class = "page-header">'
titulo = '<h3 class = "title"> Dicionário Médico </h3>'
descricao = '<p class="descricao"> O dicionário de termos médicos desenvolvidos na disciplina de SPLEB faz uma cobertura completa da terminologia médica. </p>'
div_head += titulo + descricao + "</div>"
body += div_head

for termo in designacao_descricao:
    div = '<div class="termo_descricao">'
    div += f'<h4 class="termo">{termo[0]}</h4>'
    div += f'<p class="desc">{termo[1]}</p>'
    div += "</div>"
    body += div
body += "</body>"
html = head + body

file_out=open("aula3.html","w",encoding='utf-8')
file_out.write(html)
file_out.close()
print(html)

