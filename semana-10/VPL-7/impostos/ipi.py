"""
Arquivo da classe Imposto

Classes:
    IPI
"""
from . import Imposto, IncidenciaImposto


class IPI(Imposto):
    """
    Classe de representação do Imposto IPI.

    ...

    Atributos
    ----------
    aliquota : float
        percentual ou valor fixo que será aplicado para o cálculo do valor
        de um tributo
    incidencia_imposto : IncidenciaImposto
        maneira pela qual a carga tributária é dividida entre compradores
        e vendedores
    aliquota_adicional : bool
        flag para adicao de aliquota adicional

    Metodos
    -------
    calcula_aliquota(): float
        calculo da aliquota do imposto IPI
    """

    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto,
                 aliquota_adicional: bool):
        self.__aliquota_adicional = aliquota_adicional
        super().__init__(aliquota, incidencia_imposto)

    def calcula_aliquota(self):
        if self.__aliquota_adicional:
            return self.aliquota * 1.10
