"""
TODO
"""

from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class ICMS(Imposto):
    '''TODO'''

    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto,
                 diferenca_estado: float):
        self.__diferenca_estado = diferenca_estado
        super().__init__(aliquota, incidencia_imposto)

    @property
    def diferenca_estado(self) -> float:
        '''TODO'''
        return self.__diferenca_estado

    @diferenca_estado.setter
    def diferenca_estado(self, value: float) -> None:
        self.__diferenca_estado = value

    def calcula_aliquota(self):
        return self.aliquota + self.diferenca_estado
