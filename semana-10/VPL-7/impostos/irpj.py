"""
TODO
"""


from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class IRPJ(Imposto):
    '''TODO'''
    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto,
                 desconto: float):
        self.__desconto = desconto
        super().__init__(aliquota, incidencia_imposto)

    def calcula_aliquota(self):
        return self.aliquota - self.__desconto
