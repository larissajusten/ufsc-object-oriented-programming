"""
TODO
"""

from abc import ABC, abstractmethod
from incidencia_imposto import IncidenciaImposto


class Imposto(ABC):
    '''TODO'''

    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto):
        self.__aliquota = aliquota
        self.__incidencia_imposto = incidencia_imposto

    @property
    def aliquota(self) -> float:
        '''TODO'''
        return self.__aliquota

    # @aliquota.setter
    # def aliquota(self, value: float) -> None:
    #     self.__aliquota = value

    @property
    def incidencia_imposto(self) -> IncidenciaImposto:
        '''TODO'''
        return self.__incidencia_imposto

    # @incidencia_imposto.setter
    # def incidencia_imposto(self, value: IncidenciaImposto) -> None:
    #     self.__incidencia_imposto = value

    @abstractmethod
    def calcula_aliquota(self) -> float:
        '''TODO'''
