from flask import Flask, render_template, request # redirect, url_for
from model import Pessoa, pessoas,add_pessoa

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