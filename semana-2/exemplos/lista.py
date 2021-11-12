lista1 = [1,5,2]
lista2 = lista1
lista2[0] = 3
print(lista1)
print(lista2)
print(id(lista1))
print(id(lista2))