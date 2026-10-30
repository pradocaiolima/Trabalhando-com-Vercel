# 1. Dados estruturados
dados = [
    {"ID": "101", "Nome": "Caio Silva", "Cargo": "Desenvolvedor"},
    {"ID": "102", "Nome": "Mariana Oliveira", "Cargo": "Gerente de Projetos"},
    {"ID": "103", "Nome": "Lucas Santos", "Cargo": "Analista de Dados"}
]

# 2. Formatação manual em formato JSON (sem usar bibliotecas)
string_json = "[\n"
for i, item in enumerate(dados):
    string_json += "  {\n"
    chaves = list(item.keys())
    for j, chave in enumerate(chaves):
        virgula_campo = "," if j < len(chaves) - 1 else ""
        string_json += f'    "{chave}": "{item[chave]}"{virgula_campo}\n'
    virgula_objeto = "," if i < len(dados) - 1 else ""
    string_json += f"  }}{virgula_objeto}\n"
string_json += "]"

# 3. Escrita no arquivo
with open("dados.json", "w", encoding="utf-8") as arquivo:
    arquivo.write(string_json)

print("Arquivo 'dados.json' criado com sucesso!")