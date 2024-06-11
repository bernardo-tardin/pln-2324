from flask import Flask, render_template, request, redirect, url_for
import json
import re
import string

app = Flask(__name__)

o = open("docs_auxiliares\\anatomia_pratica.json", "r", encoding="utf-8")
ossos = json.load(o)

d = open("docs_auxiliares\\doencas.json", "r", encoding="utf-8")
doencas = json.load(d)

g = open("docs_auxiliares\\glossario.json", "r", encoding="utf-8")
glossario = json.load(g)

c = open("docs_auxiliares\\categorias_ordenadas.json", "r", encoding="utf-8")
categorias = json.load(c)

categorias_glossario = ['Acidentes e Violência', 'Administração e Planejamento em Saúde', 'Alimentação e Nutrição', 'Ambiente e Saúde', 'Atenção à Saúde', 'Ciência e Tecnologia em Saúde', 'Ciências Sociais em Saúde', 'Comunicação em Saúde', 'Demograﬁ a', 'Direito Sanitário', 'Drogas de Uso Terapêutico e Social', 'Economia da Saúde', 'Epidemiologia', 'Eqüidade em Saúde e Social', 'Ética e Bioética', 'História da Saúde Pública', 'Medicamentos, Vacinas e Insumos', 'Políticas Públicas e Saúde', 'Promoção e Educação em Saúde', 'Recursos Humanos em Saúde Pública', 'Saúde Animal', 'Vigilância em Saúde']

dic_ossos ={}
for sistema in ossos:
    for cat in ossos[sistema]:
        for osso in ossos[sistema][cat]:
            dic_ossos[osso] = ossos[sistema][cat][osso]

alfabeto = list(string.ascii_uppercase)

#Averiguar, para cada letra do alfabeto, qual a primeira doença que se inicia pela mesma e armazenamento numa lista
primeiros_termos = []
for letra in alfabeto:
    for doenca in doencas:
        if doenca.lower().startswith(letra.lower()):
            primeiros_termos.append(doenca.lower())
            break 

#Averiguar, para cada letra do alfabeto, qual a primeira categoria que se inicia pela mesma e armazenamento numa lista
primeiras_categorias = []
for letra in alfabeto:
    for categoria in categorias:
        if categoria.lower().startswith(letra.lower()):
            primeiras_categorias.append(categoria.lower())
            break 

#Home Page
@app.route('/')
def home():
    return render_template("home.html")

#Listagem de todas as categorias em estudo
@app.route('/categorias')
def varias_Categorias():
    return render_template("categorias.html", categorias = categorias, alfabeto = alfabeto, primeiras_categorias = primeiras_categorias)

#Página específica para uma dada categoria presente na listagem anterior
@app.route('/categorias/<categoria>')
def categoriaEspecifica(categoria):
    definicao = categorias[categoria]["Descrição"]

    return render_template("categoria_especifica.html", categoria = categoria, definicao = definicao)

#Listagem dos ossos e músculos presentes no doc Anatomia na Prática
@app.route('/conceitos/ossos')
def listar_Categorias_Ossos():
    novo_ossos={}

    for sistema in ossos:
        novo_ossos[sistema]={}
        for cat in ossos[sistema]:
            novo_ossos[sistema][cat]= dict(sorted(ossos[sistema][cat].items(), key=lambda x:x[0].lower()))

    return render_template("ossos.html", ossos = novo_ossos)

#Listagem das doenças de A a Z
@app.route('/conceitos/doencas')
def listar_Doencas(): 
    res = dict(sorted(doencas.items(), key= lambda x:x[0].lower()))
    return render_template("doencas.html", doencas = res, alfabeto = alfabeto, primeiros_termos = primeiros_termos)

#Listagem dos termos presentes no glossário, filtrados por categoria
@app.route('/conceitos/gloss/')
def listar_Glossario():
    c = request.args.get("c")
    novo_glossario = {}
   
    if c != None:
        if c != "todos":
            for termo in glossario:
                if c in glossario[termo]["Categoria"]:
                    novo_glossario[termo] = glossario[termo]
        else:
            novo_glossario = glossario
    else:
        novo_glossario = glossario
    
    res_gloss = dict(sorted(novo_glossario.items(), key = lambda x:x[0].lower()))
    return render_template("glossario.html", glossario = res_gloss, categorias_glossario = categorias_glossario)

#Página específica para cada conceito em análise
@app.route('/conceitos/<designacao>')
def termo(designacao):
    if designacao in dic_ossos:
        desc = dic_ossos[designacao]["Definição"]
        trad = dic_ossos[designacao]["Tradução"]
        cat = dic_ossos[designacao]["Categoria"]

    elif designacao in glossario:
        desc = glossario[designacao]["Definição"]
        trad = glossario[designacao]["Tradução"]
        cat = glossario[designacao]["Categoria"]
    
    elif designacao in doencas:
        desc = doencas[designacao]["Definição"]
        trad = doencas[designacao]["Tradução"]
        cat = doencas[designacao]["Categoria"]
    
    else:
        return render_template("nao_encontrado.html", termo = designacao)

    return render_template("termo.html", descricao = desc, traducao = trad, categoria = cat, termo = designacao)
        
#Apagar um determinado conceito
@app.route("/conceitos/<designacao>", methods=["POST", "GET"])
def apagarConceito(designacao):
    if request.method == "POST":
        for sistema in ossos:
            for cat in ossos[sistema]:
                if designacao in ossos[sistema][cat]:
                    del ossos[sistema][cat][designacao]
                    with open("docs_auxiliares\\anatomia_pratica.json", "w", encoding="utf-8") as file:
                        json.dump(ossos, file, ensure_ascii=False, indent=4)
                    
                    
        if designacao in dic_ossos:
            del dic_ossos[designacao]
            return redirect(url_for("listar_Categorias_Ossos"))
        
        elif designacao in doencas:
            del doencas[designacao]
            with open("docs_auxiliares\\doencas.json", "w", encoding="utf-8") as file:
                json.dump(doencas, file, ensure_ascii=False, indent=4)
    
            return redirect(url_for("listar_Doencas"))

        elif designacao in glossario:
            del glossario[designacao]
            with open("docs_auxiliares\\glossario.json", "w", encoding="utf-8") as file:
                json.dump(glossario, file, ensure_ascii=False, indent=4)
    
            return redirect(url_for("listar_Glossario"))
    
#Editar a descrição de um conceito
@app.route("/editar_descricao/<designacao>", methods=["GET", "POST"])
def editarDescricao(designacao):
    if request.method == "POST":
        definicao = request.form["descricao"]
        
        for sistema in ossos:
            for cat in ossos[sistema]:
                if designacao in ossos[sistema][cat]:
                    ossos[sistema][cat][designacao]["Definição"] = definicao
                    with open("docs_auxiliares\\anatomia_pratica.json", "w", encoding="utf-8") as file:
                        json.dump(ossos, file, ensure_ascii=False, indent=4)
        
        if designacao in dic_ossos:
            dic_ossos[designacao]["Definição"] = definicao
            return redirect(url_for("termo", designacao = designacao))

        elif designacao in doencas:
            doencas[designacao]["Definição"] = definicao
            with open("docs_auxiliares\\doencas.json", "w", encoding="utf-8") as file:
                json.dump(doencas, file, ensure_ascii=False, indent=4)
            return redirect(url_for("termo", designacao = designacao))
        
        elif designacao in glossario:
            glossario[designacao]["Definição"] = definicao
            with open("docs_auxiliares\\glossario.json", "w", encoding="utf-8") as file:
                json.dump(glossario, file, ensure_ascii=False, indent=4)
            return redirect(url_for("termo", designacao = designacao))
            
    else:
        for sistema in ossos:
            for cat in ossos[sistema]:
                if designacao in ossos[sistema][cat]:
                    definicao = ossos[sistema][cat][designacao]["Definição"] 
        
        if designacao in dic_ossos:
            definicao = dic_ossos[designacao]["Definição"]
        
        elif designacao in doencas:
            definicao = doencas[designacao]["Definição"]
        
        elif designacao in glossario:
            definicao = glossario[designacao]["Definição"]
    
    return render_template("editar_descricao.html", designacao=designacao, descricao=definicao)

#Adicionar a tradução a um determinado conceito
@app.route("/adicionar_traducao/<designacao>", methods=["GET", "POST"])
def adicionarTraducao(designacao):
    if request.method == "POST":
        traducao = request.form["traducao"]
        
        for sistema in ossos:
            for cat in ossos[sistema]:
                if designacao in ossos[sistema][cat]:
                    ossos[sistema][cat][designacao]["Tradução"] = traducao
                    with open("docs_auxiliares\\anatomia_pratica.json", "w", encoding="utf-8") as file:
                        json.dump(ossos, file, ensure_ascii=False, indent=4)
        
        if designacao in dic_ossos:
            dic_ossos[designacao]["Tradução"] = traducao
            return redirect(url_for("termo", designacao = designacao))

        elif designacao in doencas:
            doencas[designacao]["Tradução"] = traducao
            with open("docs_auxiliares\\doencas.json", "w", encoding="utf-8") as file:
                json.dump(doencas, file, ensure_ascii=False, indent=4)
            return redirect(url_for("termo", designacao = designacao))
        
        elif designacao in glossario:
            glossario[designacao]["Tradução"] = traducao
            with open("docs_auxiliares\\glossario.json", "w", encoding="utf-8") as file:
                json.dump(glossario, file, ensure_ascii=False, indent=4)
            return redirect(url_for("termo", designacao = designacao))
        
    else:
        for sistema in ossos:
            for cat in ossos[sistema]:
                if designacao in ossos[sistema][cat]:
                    traducao = ossos[sistema][cat][designacao]["Tradução"] 

        if designacao in dic_ossos:
            traducao = dic_ossos[designacao]["Tradução"]

        elif designacao in doencas:
            traducao = doencas[designacao]["Tradução"]

        elif designacao in glossario:
            traducao = glossario[designacao]["Tradução"]
    
    return render_template("adicionar_traducao.html", designacao=designacao, traducao = traducao)

#Adicionar um conceito do doc Anatomia na Prática
@app.route('/conceitos/ossos', methods=["POST", "GET"])
def adicionar_conceitos_ossos():
    sistema = request.form.get('option_esq')
    categoria = request.form.get("option")

    if "traducao" in request.form:
        if request.form["traducao"] == "":
            en = "Sem Tradução"
        else:
            en = request.form["traducao"]

    else:
        en = "Sem Tradução"

    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")

    if designacao and descricao and categoria:
        file_out = open("docs_auxiliares\\anatomia_pratica.json", "w", encoding="UTF-8")
        if sistema == "SISTEMA ESQUELÉTICO E ARTICULAR":
            if designacao not in ossos[sistema][categoria]:
                ossos[sistema][categoria][designacao]={"Definição": descricao, "Categoria": ["Ossos"], "Tradução": en}
                ossos[sistema][categoria] = dict(sorted(ossos[sistema][categoria].items(), key=lambda x:x[0].lower()))
        
        else:
            if designacao not in ossos[sistema][categoria]:
                ossos[sistema][categoria][designacao]={"Definição": descricao, "Categoria": ["Músculos"], "Tradução": en}
                ossos[sistema][categoria] = dict(sorted(ossos[sistema][categoria].items(), key=lambda x:x[0].lower()))

        dic_ossos[designacao]= {"Definição": descricao, "Categoria": ["Músculos"], "Tradução": en}
        json.dump(ossos, file_out, indent=4, ensure_ascii=False)
        file_out.close()

    return render_template("ossos.html", ossos = ossos)

#Adicionar um conceito à listagem de conceitos do glossário
@app.route('/conceitos/gloss/', methods=["POST", "GET"])
def adicionar_conceitos_glossario():
    categoria = request.form.get("categorias")
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")

    if "traducao" in request.form:
        if request.form["traducao"] == "":
            en = "Sem Tradução"
        else:
            en = request.form["traducao"]

    else:
        en = "Sem Tradução"

    if categoria in categorias_glossario and designacao not in glossario:
        file_out = open("docs_auxiliares\\glossario.json", "w", encoding="UTF-8")
        glossario[designacao] = {"Definição": descricao, "Categoria": [categoria], "Tradução": en}
        glossario_novo = dict(sorted(glossario.items(), key= lambda x:x[0].lower()))
        json.dump(glossario_novo, file_out, indent=4, ensure_ascii=False)
        file_out.close()
    
    return render_template("glossario.html", glossario = glossario_novo, categorias_glossario = categorias_glossario)

#Adicionar um conceito à listagem das doenças de A a Z
@app.route('/conceitos/doencas', methods=["POST", "GET"])
def adicionar_conceitos_doencas():
    if "traducao" in request.form:
        if request.form["traducao"] == "":
            en = "Sem Tradução"
        else:
            en = request.form["traducao"]

    else:
        en = "Sem Tradução"

    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")
    categoria = request.form.get("categoria")

    if designacao and descricao and categoria and designacao not in doencas:
        file_out = open("docs_auxiliares\\doencas.json", "w", encoding="UTF-8")

        doencas[designacao]= {"Definição": descricao, "Categoria": [categoria], "Tradução": en}
        res = dict(sorted(doencas.items(), key=lambda x:x[0].lower()))
        json.dump(res, file_out, indent=4, ensure_ascii=False)
        file_out.close()

    
    else:
        res = doencas

    return render_template("doencas.html", doencas = res, alfabeto = alfabeto, primeiros_termos = primeiros_termos)
    
    
#Fazer highlight do termo pesquisado pelo utilizador
def highlight(text, term):
    return re.sub(re.escape(term), f"<mark>{term}</mark>", text, flags=re.IGNORECASE)

app.template_filter('highlight')(highlight)

#Pesquisar um determinado conceito 
@app.route('/conceitos/pesquisar', methods=["POST"])
def pesquisar_Conceito():
    termo = request.form.get("search")

    if termo:
        resultados = []
        for doenca in doencas:
            if termo.lower() in doenca.lower():
                resultados.append((doencas[doenca], doenca, "Doenças de A a Z"))
        
        for gloss in glossario:
            if termo.lower() in gloss.lower():
                resultados.append((glossario[gloss], gloss, "Glossário"))

        for osso in dic_ossos:
            if termo.lower() in osso.lower():
                dic_termo = dic_ossos[osso]
                resultados.append((dic_termo, osso, "Anatomia na Prática"))

        if len(resultados)!=0:
            return render_template("pesquisa.html", resultados = resultados, termo = termo)

        else:
            return render_template("nao_encontrado.html", termo = termo)
    
    else:
        return render_template("nao_encontrado.html", termo = termo)


app.run(host="localhost", port=4002, debug=True)