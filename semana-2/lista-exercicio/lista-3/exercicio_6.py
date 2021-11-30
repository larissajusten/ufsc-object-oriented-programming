"""
    Exercício 6. Criar 10 frozensets com 30 números aleatórios cada, e construir um dicionário que contenha a soma de cada um deles.
"""
import random

def get_random_set(size):
    return frozenset(random.sample(range(1, 100), size))

def get_random_sets(size, num_sets):
    return [get_random_set(size) for _ in range(num_sets)]

def get_dict_from_sets_sum(sets):
    return {key: sum(value) for key, value in enumerate(sets)}

if __name__ == '__main__':
    _sets = get_random_sets(30, 10)
    _dict = get_dict_from_sets_sum(_sets)
    print(_dict)