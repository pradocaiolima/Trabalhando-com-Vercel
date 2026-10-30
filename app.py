from flask import Flask, render_template, abort
import json
import os

app = Flask(__name__)

# Função segura para carregar os dados dos veículos do arquivo JSON
def carregar_veiculos():
    caminho_json = os.path.join(os.path.dirname(__file__), 'veiculos.json')
    if os.path.exists(caminho_json):
        with open(caminho_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Rota da Página Inicial (Home)
@app.route('/')
def home():
    return render_template('home.html')

# Rota do Catálogo de Veículos (Listagem e Filtros)
@app.route('/veiculos')
def listar_veiculos():
    veiculos = carregar_veiculos()
    return render_template('veiculos.html', veiculos=veiculos)

# Rota de Detalhes do Veículo por ID
@app.route('/veiculo/<int:id>')
def detalhe(id):
    veiculos = carregar_veiculos()
    # Procura o veículo correspondente ao ID fornecido
    veiculo = next((v for v in veiculos if v['id'] == id), None)
    
    if veiculo is None:
        abort(404)
        
    return render_template('detalhe.html', veiculo=veiculo)

if __name__ == '__main__':
    app.run(debug=True)