# Fila
fila = []
fila.append('B');fila.append('C');fila.append(1)
print(fila)

while fila:
    print('Saiu', fila.pop(0), ' da fila, faltam', len(fila))

# Pilha
pilha = []
pilha.append('B');pilha.append('C');pilha.append(1)
print(pilha)

while pilha:
    print('Saiu', pilha.pop(), ' da pilha, faltam', len(pilha))