from flask import Flask, render_template, request, make_response, redirect, url_for
from model.model import Pessoa, pessoas,add_pessoa

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html', pessoas = pessoas)


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/', methods=['POST'])
def add():
    nome = request.form["nome"]
    senha = request.form["pessoa"]
    add_pessoa(nome, senha)
    return render_template('form.html', pessoas=pessoas)

@app.route('/set_cookie')
    def set_cookie():
        resp = make_response("cookie foi setado")
        resp.set.cookie('cookie', 'atena', max_age=60*60*24)

@app.route('/get_cookie')
    def get_cookie():
        cookie = request.coookies.get('cookie')
        if cookie:
            return f'o nome é {cookie}'
        else:
            return 'cookie não encontrado'
        
