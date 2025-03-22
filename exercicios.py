from typing import Dict, Any

# 1) Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.


# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".


# 3) Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro1: Dict[str, Any] = {
    "titulo": "Why We Sleep",
    "autor": "Matthew Walker",
    "ano": 2017}

print("3)")
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



# 4) Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.


# 5) Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.