tupla = (2,5,9,12)
print(tupla)

segundo_elemento = tupla[1]
print(segundo_elemento)

tupla1 = (2,)
print(tupla1)

tupla_de_lista = tuple([2,5,8])
print(tupla_de_lista)

lista_de_tupla = list(tupla)
print(lista_de_tupla)

tupla_elemento_mutavel = (9,[2,5],12)
print(tupla_elemento_mutavel)

# erro - AttributeError: 'int' object has no attribute 'append'
# tupla[1].append(18)

# erro - TypeError: 'tuple' object does not support item assignment
# tupla[1]=[2,5,18]
