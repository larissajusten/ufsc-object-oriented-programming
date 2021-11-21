# Exercício 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
def LeVetorDeCincoNumeros():
    print('# Digite os 5 numeros inteiros a seguir!')
    vetor = []
    for i in range(5):
        vetor.append(int(input(f'[{i+1}] Numero: ')))
    
    print(f'Numeros: {vetor}')

# Exercício 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa
def LeVetorDezNumerosEMostraNaOrdemInversa():
    print('# Digite os 10 numeros reais a seguir!')
    vetor = []
    for i in range(10):
        vetor.append(input(f'[{i+1}] Numero: '))

    print(f'Numeros: {vetor[:]}')
    print(f'Ordem inversa: {vetor[::-1]}')

# Exercício 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
def LeQuatroNotasEMostraNotasEMostraMedia():
    print('# Digite as 4 notas a seguir:')
    vetor = []
    valor = ' '
    for i in range(4):
        while True:
            try:
                vetor.append(float(input(f'[{i+1}] Nota: ')))
                break
            except:
                print("Nota invalida!")
    
    media = sum(vetor)/len(vetor)
    print(f'# Media: {media}')
    print(f'# Notas: {vetor}')

# Exercício 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
def LeConstantesEContaConstantes():
    constantes = ['a', 'e', 'i', 'o', 'u']
    vetor = []
    for i in range(10):
        vetor.append(input(f'[{i+1}] Caracter: ')[0])
    
    vetor_constantes = [caracter for caracter in vetor if caracter in constantes]
    print(f'# Constantes[{len(vetor_constantes)}]: {vetor_constantes}')

# Exercício 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
def isPar(value):
    return value % 2 == 0

def LeVinteNumerosESeparaEmImparEPar():
    vetor, vetor_par, vetor_impar = ([] for i in range(3))

    for i in range(20):
        while True:
            try:
                value = int(input(f'[{i+1}] Numero: '))
                vetor.append(value)
                if isPar(value):
                    vetor_par.append(value)
                else:
                    vetor_impar.append(value)
                break
            except:
                print("Entrada invalida!")

    print(f'# Vetor: {vetor}')
    print(f'# Vetor par: {vetor_par}')
    print(f'# Vetor impar: {vetor_impar}')

# Exercício 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.
def LeNotasDezAlunos(notas_alunos = [], num_alunos = 1):
    valor = 0

    print('')
    print(f'# Digite as notas do aluno {num_alunos}:')
    for i in range(4):
        while True:
            try:
                valor += float(input(f'[{i+1}] Nota: '))
                notas_alunos.append(valor/4)
                break
            except:
                print('Entrada invalida!')
        
    if num_alunos < 10:
        LeNotasDezAlunos(notas_alunos, num_alunos+1)
    
    if num_alunos == 10:
        print('')
        media_maior_igual_7 = [nota for nota in notas_alunos if nota >= 7.0]
        print(f'# Numero de alunos com media maior ou igual a 7.0: {len(media_maior_igual_7)}')        

# Exercício 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
def LeCincoNumeros():
    print('# Digite os 5 numeros inteiros:')
    vetor_numeros = []
    soma = 0
    multiplicacao = 1

    for i in range(5):
        while True:
            try:
                valor = int(input(f'[{i+1}] Numero: '))
                soma += valor
                multiplicacao *= valor
                vetor_numeros.append(valor)
                break
            except:
                print('Entrada invalida!')
    
    print(f'# Soma: {soma}')
    print(f'# Multiplicacao: {multiplicacao}')
    print(f'# Numeros: {vetor_numeros}')

# Exercício 8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.
def LeIdadeEAltura():
    vetor_idade = []
    vetor_altura = []

    for i in range(5):
        while True:
            try:
                idade = int(input(f'[{i+1}] Idade: '))
                altura = float(input(f'[{i+1}] Altura: '))
                vetor_idade.append(idade)
                vetor_altura.append(altura)
                break
            except:
                print('Entrada invalida!')

    print(f'# Idades: {vetor_idade[::-1]}')
    print(f'# Altura: {vetor_altura[::-1]}')

# Exercício 9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
def LeDezNumeros():
    vetor = []

    for i in range(10):
        while True:
            try:
                vetor.append(int(input(f'[{i+1}] Numero: ')))
                break
            except:
                print('Entrada invalida!')

    list_quadrados = [valor**2 for valor in vetor]
    print(f'# Vetor: {vetor}')
    print(f'# Soma dos quadrados dos elementos do vetor: {sum(list_quadrados)}')

# Exercício 10. Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores
def LeDoisVetoresDezElementos():
    vetor_a = []
    vetor_b = []

    for i in range(20):
        valor = input(f'[{i+1}] Elemento: ')
        if i <= 9:
            vetor_a.append(valor)
        elif i > 9:
            vetor_b.append(valor)

    vetor_c = []
    [[vetor_c.append(vetor_a[i]), vetor_c.append(vetor_b[i])] for i in range(len(vetor_a))]
    print(vetor_c)
