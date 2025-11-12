from flask import render_template

def init_app(app):
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/pedido')
    def cardapio():
        # Aqui só passo dados (nome, descricao e o NOME DO ARQUIVO de imagem)
        pizzas = [
            {"nome": "Pepperoni", "descricao": "Molho, mussarela e pepperoni.", "img_file": "pepperoni.jpg"},
            {"nome": "4 Queijos", "descricao": "Molho, mussarela, gorgonzola, parmesão e cheddar.", "img_file": "4queijos.jpg"},
            {"nome": "Marguerita", "descricao": "Molho, mussarela, tomate e manjericão.", "img_file": "marguerita.jpg"},
            {"nome": "Carne", "descricao": "Molho, mussarela e carne desfiado.", "img_file": "carne.jpg"},
            {"nome": "Champignon", "descricao": "Molho, mussarela, champignon e azeitona.", "img_file": "champignon.jpg"},
            {"nome": "Atum", "descricao": "Molho, mussarela, atum, cebola e azeitona.", "img_file": "atum.jpg"},
            {"nome": "Shitake", "descricao": "Molho, mussarela, shitake e azeitona.", "img_file": "shitake.jpg"},
            {"nome": "Chocolate", "descricao": "Molho, mussarela, chocolate.", "img_file": "chocolate.jpeg"},
        ]
        return render_template('pedido.html', pizzas=pizzas)