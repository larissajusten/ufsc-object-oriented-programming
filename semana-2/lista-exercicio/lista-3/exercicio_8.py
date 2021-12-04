"""
    Exercício 8. Crie uma classe MatrizEsparsa que pode ser construida das duas formas abaixo, 
        e contenha métodos para mostrar a matriz no formato String e também no formato de dicionário.
        
        1) receber uma dupla (tupla com 2 elementos) indicando quantas linhas e colunas tem a matriz, 
            e um dicionário com duplas como chave (linha, coluna) e um valor numérico.

        2) Receber uma string no seguinte formato:
        matriz = '''0 8 0 0 0 0 0 0 0
                    0 0 0 0 0 0 0 0 0
                    0 2 0 0 0 0 1 0 0
                    0 0 0 0 0 0 0 0 0
                    0 0 0 7 0 0 0 0 0
                    0 0 0 0 0 0 4 0 0'''

    *dica: use os métodos splitlines() e split da classe String, e o método get() da classe dict
"""