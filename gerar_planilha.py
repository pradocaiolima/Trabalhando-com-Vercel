import pandas as pd

# 1. Definir os dados iniciais para as colunas A, B, C e D
# Cada lista representa os valores das linhas para aquela coluna
dados = {
    'A': [2, 3, 5, 8],
    'B': [3, 2, 6, 1],
    'C': [4, 7, 4, 3],
    'D': [1, 2, 5, 10]
}

# 2. Criar o DataFrame do pandas com os dados
df = pd.DataFrame(dados)

# 3. Realizar o cálculo e popular a coluna E
# Fórmula: (A * B) + (C / D)
df['E'] = (df['A'] * df['B']) + (df['C'] / df['D'])

# 4. Salvar os dados em um arquivo Excel (.xlsx)
# index=False evita que o índice numérico (0, 1) do pandas seja salvo na planilha
nome_arquivo = 'resultado_calculos.xlsx'
df.to_excel(nome_arquivo, index=False)

print(f"Sucesso! O arquivo '{nome_arquivo}' foi criado na sua pasta.")