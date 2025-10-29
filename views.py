from main import *

# rotas
@app.route ("/")
def homepage():
    # return "<h1>Meu Site Flask</h1>"
    nome = "Pizzaria duGordo"
    sabores = ["Pepperoni", "4 Queijos", "Marguerita"]
    return render_template ("index.html", nome=nome, sabores=sabores)

# localhost:5000/user/daniel
@app.route ("/user/<name>")
def user(name):
    return render_template ("user.html", name=name)