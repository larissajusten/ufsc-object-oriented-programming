"""
Arquivo da classe Imposto

Classes:
    ICMS
"""
from . import Imposto, IncidenciaImposto


class ICMS(Imposto):
    """
    Classe de representação do Imposto ICMS.

    ...

    Atributos
    ----------
    aliquota : float
        percentual ou valor fixo que será aplicado para o cálculo do valor de
        um tributo
    incidencia_imposto : IncidenciaImposto
        maneira pela qual a carga tributária é dividida entre compradores
        e vendedores
    diferenca_estado : float
        solução criada para que o recolhimento desse imposto fosse feito de
        maneira mais justa entre os estados

    Metodos
    -------
    diferenca_estado(): float
        retorna o valor da diferenca de estado
    diferenca_estado(diferenca_estado: float): None
        define um novo valor para o atributo diferenca_estado
    calcula_aliquota(): float
        calculo da aliquota do imposto ICMS
    """

    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto,
                 diferenca_estado: float):
        self.__diferenca_estado = diferenca_estado
        super().__init__(aliquota, incidencia_imposto)

    @property
    def diferenca_estado(self) -> float:
        '''
        Retorna o valor da diferenca de estado
            Parametros:
                -

            Retorno:
                diferenca_estado (float): valor inicial da diferenca de estado
        '''
        return self.__diferenca_estado

    @diferenca_estado.setter
    def diferenca_estado(self, value: float) -> None:
        self.__diferenca_estado = value

    def calcula_aliquota(self):
        return self.aliquota + self.diferenca_estado
