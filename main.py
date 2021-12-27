import pandas as pd
from flask import Flask, jsonify

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

# start app
app.run(host='0.0.0.0')


# tabela = pd.read_csv('dados.csv',sep=',')
# print(tabela.head(3))
# total_vendas = tabela['Vendas'].sum()
# print(total_vendas)