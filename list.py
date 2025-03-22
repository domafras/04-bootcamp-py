produto1: str = "sapato"
produto2: str = "camiseta"
produto3: str = "videogame"

produtos: list = []

produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)

print(produtos)

# retira o ultimo da lista (mais performático)
produtos.pop()

print(produtos)

# exemplo de extend / diferença para append
# numeros = []
# numeros.extend(range(0,5))
# print(numeros)
