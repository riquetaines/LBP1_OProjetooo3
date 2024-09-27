from flask import Flask, render_template, request # redirect, url_for
from model import classes, Carro, carro, carros, add_carros

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', carro = carro)


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/add', methods=['POST'])
def add():
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    ano = request.form["ano"]
    cor = request.form["cor"]
    add_carros(marca, modelo, ano, cor)
    return render_template('index.html', carros=carros)
