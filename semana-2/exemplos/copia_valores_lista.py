#copia a apenas os valores
lista1 = [1,5,2]
lista2 = lista1[:]
# ou list(lista1)
# ou lista1.copy()
# ou copy.deepcopy(lista1) - listas de listas (import copy)
lista2[0] = 3
print(lista1)
print(lista2)
print(id(lista1))
print(id(lista2))