import csv

# Caminho para o arquivo
caminho_arquivo: str = "exemplo.csv"

# Inicializa lista vazia para armazenar dados
arquivo_csv: list = []

# Usa gerenciador de contexto 'with' para abrir e fechar arquivo 
with open(file=caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
    # Cria objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)

    # Exibe leitor de CSV (DictReader)
    print("Devemos converter esse tipo: ", leitor_csv)

    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Adiciona cada linha (dicionário) à lista de dados
        arquivo_csv.append(linha)

# Exibe os dados
print("\n", arquivo_csv)

# Outra forma de exibição
for registro in arquivo_csv:
    print(registro)
