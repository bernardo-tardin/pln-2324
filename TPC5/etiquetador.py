import json
import re

file_conceitos = open('conceitos.json')
file_livro = open('livro.txt')
file_ingles = open('conceitos_ingles.json')

texto = file_livro.read()
conceitos = json.load(file_conceitos)
termos_ingles = json.load(file_ingles)

conceitos_min = {chave.lower():conceitos[chave] for chave in conceitos}

black_list = ['a','o','e','de','da','do','em','um','uma','para','com','por','na','no','nas','nos','ao','à','às','aos','que','se','não','mas','ou','como','quando','onde','porque','para','quem','qual','quais','qualquer','quanto','quanto','quanta','quantos','quantas','este','pelo']

def etiquetador(matched):
    palavra = matched[0]
    if palavra.lower() not in black_list:
        if palavra.lower() in termos_ingles and palavra.lower() in conceitos_min:
            ingles = termos_ingles[palavra.lower()]
            descricao = conceitos_min[palavra.lower()]
            etiqueta = f"<a href='' title='(en: {ingles}) {descricao}'>{palavra}</a>"
            return etiqueta
        elif palavra.lower() in conceitos_min:
            descricao = conceitos_min[palavra.lower()]
            etiqueta = f"<a href='' title='{descricao}'>{palavra}</a>"
            return etiqueta
        else:
            return palavra
    else:
        return palavra

expressao = r'[\wáãéíóçêúôâõà]+'
texto = re.sub(expressao,etiquetador,texto, flags=re.IGNORECASE)
texto = re.sub(r'\n','<br>',texto)
texto = re.sub(r'\f','<hr/>',texto)

file_out = open('livro_etiquetado.html','w')
file_out.write(texto)



    



