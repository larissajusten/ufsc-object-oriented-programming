"""
    Exercício 3. Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. 
    A entrada de dados deve terminar quando for lida uma string vazia como nome.
    Escreva uma função que retorna a média do aluno, dado seu nome.
"""


def le_notas(dicionario = {}):
    nome_aluno = input('Digite o nome do aluno: ')
    if nome_aluno.isalpha() and nome_aluno not in dicionario.keys():
        nota1 = float(input('Digite a primeira nota: (somente numeros) '))
        nota2 = float(input('Digite a segunda nota: (somente numeros) '))
        dicionario[nome_aluno] = [nota1, nota2]
        le_notas(dicionario)
    elif nome_aluno in dicionario.keys():
        print('Aluno ja adicionado!')
        le_notas(dicionario)

    return dicionario


def retorna_nota_aluno(dicionario, nome_aluno):
    return (dicionario[nome_aluno][0] + dicionario[nome_aluno][1]) / 2


if __name__ == '__main__':
    dicionario = le_notas()
    nome_aluno = input('\nDigite o nome do aluno que deseja saber a nota: ')

    if dicionario and nome_aluno in dicionario.keys():
        media = retorna_nota_aluno(dicionario, nome_aluno)
        print(f'{nome_aluno}: {media}')
