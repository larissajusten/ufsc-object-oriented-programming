"""
    Exercício 1. Escreva uma função que conta a frequência de ocorrência de cada
    palavra em um texto (arquivo txt) e armazena tal quantidade em um dicionário, onde a
    chave é a vogal considerada.

    Correção: "onde a chave é a PALAVRA considerada"
"""

from collections import Counter


def count_palavras(nome_arquivo: str):
    file = open(f'{nome_arquivo}.txt', 'rt')
    texto = file.read()

    palavras = [palavra for palavra in texto.split(' ')]
    dicionario = dict(Counter(palavras))
    # dicionario2 = {i: palavras.count(i)  for i in list(set(palavras))}

    return dicionario


if __name__ == '__main__':
    nome_arquivo = input('Digite o nome do arquivo de texto: ')
    dicionario = count_palavras(nome_arquivo)
    print(dicionario)
    novo_dicionario = delete_stopwords(dicionario)
    print(novo_dicionario)
