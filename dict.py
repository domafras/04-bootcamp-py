import json

# exemplo lista para produto
produto_00: list =  ["Sapato", 39, 10.38, True]

# exemplo dicionario para produto
produto_1: dict = {
    "nome":"Sapato",
    "quantidade":39,
    "preco":10.38,
    "disponibilidade":True  
}
produto_2: dict = {
    "nome":"Televisao",
    "quantidade":10,
    "preco":70.55,
    "disponibilidade":False  
}

carrinho: list = []

carrinho.append(produto_1)
carrinho.append(produto_2)

print(carrinho)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)