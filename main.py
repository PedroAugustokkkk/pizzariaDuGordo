from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cardapio')
def cardapio():
    # Aqui só passo dados (nome, descricao e o NOME DO ARQUIVO de imagem)
    pizzas = [
        {"nome": "Pepperoni", "descricao": "Molho, mussarela e pepperoni.", "img_file": "pepperoni.jpg"},
        {"nome": "4 Queijos", "descricao": "Molho, mussarela, gorgonzola, parmesão e cheddar.", "img_file": "4queijos.jpg"},
        {"nome": "Marguerita", "descricao": "Molho, mussarela, tomate e manjericão.", "img_file": "marguerita.jpg"},
        {"nome": "Carne", "descricao": "Molho, mussarela e carne desfiado.", "img_file": "carne.jpg"}
    ]
    return render_template('cardapio.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)
