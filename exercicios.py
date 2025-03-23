from typing import Dict, Any
from collections import Counter

# 1) Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
print("\n1)")

numeros = list(range(1, 11))
for numero in numeros:
    print(numero**2)

# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
print("\n2)")

linguagens = ["Python", "Java", "C++", "JavaScript"]

linguagens.remove("C++")
linguagens.append("Ruby")

print(linguagens)

# 3) Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
print("\n3)")

livro1: Dict[str, Any] = {
    "titulo": "Why We Sleep",
    "autor": "Matthew Walker",
    "ano": 2017}

for chave, valor in livro1.items():
    print(f"{chave}: {valor}")

# Dicionario com dicionarios
livro2: Dict[str, Any] = {
    "titulo": "Atomic Habits",
    "autor": "James Clear",
    "ano": 2018}

lista_livros = []
lista_livros.append(livro1)
lista_livros.append(livro2)
print("Lista de livros: ", lista_livros)

lista_livros_dict:dict = {
    "livro1": {"titulo": "Why We Sleep",
    "autor": "Matthew Walker",
    "ano": 2017},

    "livro2": {"titulo": "Atomic Habits",
    "autor": "James Clear",
    "ano": 2018}
}

print("Dicionario de livros: ", lista_livros_dict["livro1"])
print("Título do livro 2: ", lista_livros_dict["livro2"]["titulo"])

# Gabarito de uma solução mais simples
livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

# 4) Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
print("\n4)")

# Implementa built in Counter
def contar_caracteres(s):
    return Counter(s)

print(contar_caracteres("aaabbc"))

# Utiliza count() dentro de dict comprehension
def contar_caracteres(s):
    return {char: s.count(char) for char in set(s)}

print(contar_caracteres("aaabbc"))

# Implementa sem built in
def contar_caracteres(s):
    contagem = {}
    for char in s:
        contagem[char] = contagem.setdefault(char, 0) + 1
    return contagem

print(contar_caracteres("aaabbc"))

# 5) Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
print("\n5)")

lista_compras = ["maçã", "banana", "cereja"]
preco = {"maçã": 1.49, "banana": 2.99, "cereja": 0.49}

total = sum(preco[item] for item in lista_compras)
print(f"Preço total: {total}")

# 6) Remoção de duplicatas 
# Dada uma lista de emails, remover todos os duplicados.
print("\n6)")

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)

# 7) Filtragem de Dados
# Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
print("\n7)")

idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)

# 8) Ordenação Personalizada
# Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
print("\n8)")

pessoas = [
    {"nome": "Ziraldo", "idade": 30},
    {"nome": "Amado", "idade": 25},
    {"nome": "Denilson", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)

# 9) Agregação de dados
# Dado um conjunto de números, calcular a média.
print("\n9)")

numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)

print("Média:", media)

# 10) Divisão de dados em grupos
# Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
print("\n10)")

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)

# 11) Atualização de dados
# Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
print("\n11)")

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos)

# 12) Fusão de Dicionários
# Dados dois dicionários, fundi-los em um único dicionário.
print("\n12)")

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)

# 13) Filtragem de Dados em Dicionário
# Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
print("\n13)")

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)

# 14) Extração de Chaves e Valores
# Dado um dicionário, criar listas separadas para suas chaves e valores.
print("\n14)")

dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves:", chaves)
print("Valores:", valores)

# 15) Contagem de Frequência de Itens
# Dada uma string, contar a frequência de cada caractere usando um dicionário.
print("\n15)")

texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)