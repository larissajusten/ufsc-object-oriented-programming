dicionario = {"nome": "Shirley Manson",
    "banda":"Garbage",
    "Ano":1993}

dicionarioA = {"nome": "Shirley Manson",
 "banda":"Garbage",
 (1,5,4):1993}

print(dicionario)
print(dicionarioA)

dicionario["album"] = "Version 2.0"
print(dicionario)

del dicionario["album"]
print(dicionario)

print('itens:', dicionario.items())
print('chaves:', dicionario.keys())
print('valores:', dicionario.values())
print('')

#
progs = {"Yes":['Close to the Edge','Fragile'],
    "Genesis":['Foxtrot','The Nursery Crime'],
    "ELP":['Brain Salad Surgery']}
progs["King Crimsom"] = ['Red','Discipline']
a = progs.items()

print(progs.items())
print(progs)

for prog, albuns in a:
    print(prog,"=>",albuns)
print(len(progs),"bandas")

if 'ELP' in progs:
    del progs["ELP"]
print("Agora",len(progs),"bandas")

for prog, albuns in a:
    print(prog,"=>",albuns)