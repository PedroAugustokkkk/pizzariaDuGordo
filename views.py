from main import *

# rotas
@app.route ("/")
def homepage():
    nome = "Pizzaria duGordo"
    sabores = ["Pepperoni", "4 Queijos", "Marguerita"]
    return render_template ("home.html", nome=nome, sabores=sabores)


@app.route ("/user/<name>")
def user(name):
    return render_template ("cardapio.html", name=name)