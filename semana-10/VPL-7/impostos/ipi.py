"""
TODO
"""


from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class IPI(Imposto):
    '''TODO'''

    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto,
                 aliquota_adicional: bool):
        self.__aliquota_adicional = aliquota_adicional
        super().__init__(aliquota, incidencia_imposto)

    def calcula_aliquota(self):
        if self.__aliquota_adicional:
            return self.aliquota * 1.10
