from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def carregar_veiculos():
    # Lê os dados diretamente do arquivo veiculos.json na pasta do projeto
    caminho_json = os.path.join(os.path.dirname(__file__), 'veiculos.json')
    if os.path.exists(caminho_json):
        with open(caminho_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/veiculos")
def listar_veiculos():
    veiculos = carregar_veiculos()
    return render_template("veiculos.html", veiculos=veiculos)

@app.route("/veiculo/<int:id_veiculo>")
def detalhe_veiculo(id_veiculo):
    veiculos = carregar_veiculos()
    veiculo_encontrado = next((v for v in veiculos if v['id'] == id_veiculo), None)
    
    if veiculo_encontrado:
        return render_template("detalhe.html", veiculo=veiculo_encontrado)
    else:
        return f"<h3>Veículo com ID {id_veiculo} não encontrado!</h3><br><a href='/veiculos' class='btn'>Voltar para a lista</a>", 404

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, abort
import json

app = Flask(__name__)

def carregar_veiculos():
    with open('veiculos.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/veiculo/<int:id>')
def detalhe(id):
    veiculos = carregar_veiculos()
    # Busca o veículo pelo ID
    veiculo = next((v for v in veiculos if v['id'] == id), None)
    
    if veiculo is None:
        abort(404)
        
    return render_template('detalhe.html', veiculo=veiculo)