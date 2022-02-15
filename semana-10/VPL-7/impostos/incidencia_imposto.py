'''
Enum contendo tres tipos de incidencia de impostos:
PRODUCAO, SERVICOS, VENDAS e TODOS
'''

from enum import Enum


class IncidenciaImposto(Enum):
    '''TODO'''
    PRODUCAO = 1
    SERVICOS = 2
    VENDAS = 3
    TODOS = 4
