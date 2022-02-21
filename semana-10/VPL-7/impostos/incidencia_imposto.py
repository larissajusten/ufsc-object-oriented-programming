"""
Arquivo da classe IncidenciaImposto

Classes:
    IncidenciaImposto
"""
from enum import Enum


class IncidenciaImposto(Enum):
    """
    Classe de representação das Incidencias dos Impostos.

    Enum contendo tres tipos de incidencia de impostos:
        PRODUCAO, SERVICOS, VENDAS e TODOS
    """
    PRODUCAO = 1
    SERVICOS = 2
    VENDAS = 3
    TODOS = 4
