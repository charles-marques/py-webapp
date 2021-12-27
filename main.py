import pandas as pd
from flask import Flask, jsonify, render_template

# inicializando Flask
app = Flask(__name__)

# construir funcionalidades
@app.route('/')
def homepage():
    return 'Essa é a homepage do site'

@app.route('/contatos')
def contatos():
    return "contatos"

@app.route('/vendas')
def vendas():
    tabela = pd.read_csv('dados/vendas.csv',sep=',')
    total_vendas = tabela['Vendas'].sum()
    resultado = {'total_vendas': total_vendas}
    return jsonify(resultado)

@app.route('/images')
def images_index():
    return render_template('index.html', bg_color = None)

@app.route('/images/<bgcolor>')
def images_detail(bgcolor):
    return render_template('index.html', bg_color = bgcolor)

# start app
app.run(host='0.0.0.0')


# tabela = pd.read_csv('dados.csv',sep=',')
# print(tabela.head(3))
# total_vendas = tabela['Vendas'].sum()
# print(total_vendas)