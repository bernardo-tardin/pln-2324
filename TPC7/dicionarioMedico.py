from flask import Flask, render_template, request, redirect, url_for
import json

file = open("/Users/bernardomoraes/Documents/GitHub/pln2324/TPC5/conceitos_trad.json","r", encoding="utf-8")
conceitos=json.load(file)


app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route("/conceitos")
def listarConceitos():
    return render_template("conceitos.html", conceitos=conceitos)

@app.route("/conceitos/<designacao>")
def consultarConceitos(designacao):
    if designacao not in conceitos:
        return render_template("error.html")
    descr = conceitos[designacao]['descricao']
    traduc = conceitos[designacao]['traducao']
    return render_template("descricao.html",descricao=descr, traducao=traduc, designacao=designacao)

@app.route("/adicionar_traducao/<designacao>", methods=["GET", "POST"])
def adicionarTraducao(designacao):
    if request.method == "POST":
        idioma = request.form["idioma"]
        traducao = request.form["traducao"]
        
        conceitos[designacao]["traducao"][idioma] = traducao
        
        with open("/Users/bernardomoraes/Documents/GitHub/pln2324/TPC5/conceitos_trad.json", "w", encoding="utf-8") as file:
            json.dump(conceitos, file, ensure_ascii=False, indent=4)
        
        return redirect(url_for("consultarConceitos", designacao=designacao))
    
    return render_template("adicionar_traducao.html", designacao=designacao)

@app.route("/editar_descricao/<designacao>", methods=["GET", "POST"])
def editarDescricao(designacao):
    descricao = conceitos[designacao]["descricao"]
    if request.method == "POST":
        descricao = request.form["descricao"]
        
        conceitos[designacao]["descricao"] = descricao
        
        with open("/Users/bernardomoraes/Documents/GitHub/pln2324/TPC5/conceitos_trad.json", "w", encoding="utf-8") as file:
            json.dump(conceitos, file, ensure_ascii=False, indent=4)
        
        return redirect(url_for("consultarConceitos", designacao=designacao))
    
    return render_template("editar_descricao.html", designacao=designacao, descricao=descricao)

@app.route("/adicionar_conceito", methods=["GET", "POST"])
def adicionarConceito():
    global conceitos
    if request.method == "POST":
        designacao = request.form["designacao"]
        descricao = request.form["descricao"]
        traducao = {}

        conceitos[designacao] = {"descricao": descricao, "traducao": traducao}

        if "idioma" in request.form:
            idioma = request.form["idioma"]
            traducao = request.form["traducao"]
            conceitos[designacao]["traducao"][idioma] = traducao
        
        conceitos = dict(sorted(conceitos.items(), key=lambda x: x[0].lower()))
        
        with open("/Users/bernardomoraes/Documents/GitHub/pln2324/TPC5/conceitos_trad.json", "w", encoding="utf-8") as file:
            json.dump(conceitos, file, ensure_ascii=False, indent=4)
        
        return redirect(url_for("listarConceitos"))
    
    return render_template("adicionar_conceito.html")

@app.route("/conceitos/<designacao>", methods=["POST", "GET"])
def apagarConceito(designacao):
    global conceitos

    if request.method == "POST":
        del conceitos[designacao]

    with open("/Users/bernardomoraes/Documents/GitHub/pln2324/TPC5/conceitos_trad.json", "w", encoding="utf-8") as file:
        json.dump(conceitos, file, ensure_ascii=False, indent=4)
    
    return redirect(url_for("listarConceitos"))

@app.route("/conceitos", methods=["POST"])
def pesquisarConceito():
    termo = request.form.get("search","")
    resultados = []
    resultados = [conceito for conceito in conceitos if termo.lower() in conceito.lower()]
    if resultados != []:
        return render_template("conceitos.html", resultados=resultados, conceitos=conceitos)
    else:
        return render_template("error.html")

@app.route("/table")
def data_table():
    return render_template("table.html", conceitos=conceitos)

@app.route("/pesquisa", methods=["POST","GET"])
def pesquisa():
    termo = request.form.get("search","")
    resultados = {}
    for conceito in conceitos:
        if termo.lower() in conceito.lower() or termo.lower() in conceitos[conceito]["descricao"].lower():
           resultados[conceito]= conceitos[conceito]
    if resultados == {}:
        return render_template("error.html")
    else:
        return render_template("pesquisa.html", resultados=resultados)

app.run(host="localhost",port=4002,debug=True)


