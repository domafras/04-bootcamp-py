# Implementa algoritmo de ordenação

# Lista original:  [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
# lista ordenada:  [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

lista_numeros = [5,4,3,2,1,0,-1,-2,-3,-4,-5]

def ordernar_lista(numeros: list) -> list:
    nova_lista = numeros.copy()

    for i in range(len(nova_lista)):
        for j in range(i+1, len(nova_lista)):
            if nova_lista[i] > nova_lista[j]:
                nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]

    return nova_lista

lista_ordenada = ordernar_lista(lista_numeros)

print("Lista original: ", lista_numeros)
print("lista ordenada: ", lista_ordenada)

# Implementa de forma simplificada usando built in function

# Ordenando a lista com sort()

lista_exemplo = [5,4,3,2,1,0,-1,-2,-3,-4,-5]
lista_exemplo.sort()

print("Lista ordenada com método built-in:", lista_exemplo)