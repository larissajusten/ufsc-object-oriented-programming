"""
    Exercício 4. Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
    Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor.
    Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1o o campeão).
    O campeão é o que tem a menor média de tempos.
"""


def le_tempos_corridas(array_tempos=[], numero_voltas=0):
    if numero_voltas < 2:
        tempo_volta = float(
            input(f'[{numero_voltas+1}] Digite o tempo: (numerico/seg) '))
        if tempo_volta > 0:
            array_tempos.append(tempo_volta)
            le_tempos_corridas(array_tempos, numero_voltas+1)
        else:
            print('# Valor invalido no tempo da volta!')
            le_tempos_corridas(array_tempos, numero_voltas)
    return array_tempos


def le_corredores(dicionario={}, num_corredores=0):
    if num_corredores < 2:
        nome_corredor = input(
            f'[{num_corredores+1}] Digite o nome do corredor: ')
        if nome_corredor.isalpha():
            array_tempos = le_tempos_corridas(array_tempos=[])
            dicionario[nome_corredor] = sorted(array_tempos)
            le_corredores(dicionario, num_corredores+1)
        else:
            print('# Valor invalido no nome do corredor!')
            le_corredores(dicionario, num_corredores)
    return dicionario


def calc_media_tempos(dicionario):
    return {corredor: sum(array_tempos)/len(array_tempos) for corredor, array_tempos in dicionario.items()}


if __name__ == '__main__':
    dicionario = le_corredores()

    for i in sorted(dicionario, key=dicionario.get):
        print(
            f'# {i.capitalize()} teve a melhor volta com duracao de {dicionario[i][0]} segundos!')
        break

    dicionario_medias = calc_media_tempos(dicionario)
    for index, i in enumerate(sorted(dicionario_medias, key=dicionario_medias.get)):
        print(
            f'[{index+1} Lugar] {i.capitalize()} com media de {dicionario_medias[i]} segundos!')
        if index == 2:
            break
