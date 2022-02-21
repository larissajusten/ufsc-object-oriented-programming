"""
Arquivo da classe Imposto

Classes:
    IRPJ
"""
from . import Imposto, IncidenciaImposto


class IRPJ(Imposto):
    """
    Classe de representação do Imposto IRPJ.

    ...

    Atributos
    ----------
    aliquota : float
        percentual ou valor fixo que será aplicado para o cálculo do valor
        de um tributo
    incidencia_imposto : IncidenciaImposto
        maneira pela qual a carga tributária é dividida entre compradores
        e vendedores
    desconto : float
        valor de desconto sobre a aliquota atual

    Metodos
    -------
    calcula_aliquota(): float
        calculo da aliquota do imposto IRPJ
    """

    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto,
                 desconto: float):
        self.__desconto = desconto
        super().__init__(aliquota, incidencia_imposto)

    def calcula_aliquota(self):
        return self.aliquota - self.__desconto
