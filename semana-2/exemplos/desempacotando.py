lista = [2,4,6]
a, b, c = lista
print(a,b,c)

tupla = (2,4,6)
a, b, c = tupla
a=8
print(a,b,c)

lista = [2,4,6,8,10]
a, b, *resto = lista
print(a,b,resto)

lista = [2,4,6,8,10]
a, *resto, b = lista
print(a,b,resto)