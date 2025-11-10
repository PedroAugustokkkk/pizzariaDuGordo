from flask import Flask, render_template
from views import init_app

def create_app():
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates')

    init_app(app)

    @app.errorhandler(Exception)
    def erro(e):
        code = getattr(e, "code", 404)
        mensagem = getattr(e, "description", str(e))

        return render_template("erro.html", codigo = code, mensagem=mensagem)


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
