"""
Arquivo da classe Imposto

Classes:
    Imposto
"""
from abc import ABC, abstractmethod
from . import IncidenciaImposto


class Imposto(ABC):
    """
    Classe de representação de um Imposto.

    ...

    Atributos
    ----------
    aliquota : float
        percentual ou valor fixo que será aplicado para o cálculo do valor
        de um tributo
    incidencia_imposto : IncidenciaImposto
        maneira pela qual a carga tributária é dividida entre compradores
        e vendedores

    Metodos
    -------
    aliquota(): float
        retorna o valor da aliquota do imposto
    incidencia_imposto(): IncidenciaImposto
        retorna a incidencia do imposto
    calcula_aliquota(): float
        calculo da aliquota do imposto
    """

    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto):
        self.__aliquota = aliquota
        self.__incidencia_imposto = incidencia_imposto

    @property
    def aliquota(self) -> float:
        '''
        Retorna o valor da aliquota do imposto
            Parametros:
                -

            Retorno:
                aliquota (float): valor inicial da aliquota do imposto
        '''
        return self.__aliquota

    @property
    def incidencia_imposto(self) -> IncidenciaImposto:
        '''
        Retorna a incidencia do imposto
            Parametros:
                -

            Retorno:
                incidencia (IncidenciaImposto): valor da incidencia

        '''
        return self.__incidencia_imposto

    @abstractmethod
    def calcula_aliquota(self) -> float:
        '''
        Operacao abstrata que ira calcular a aliquota
        Cada classe que ira estender Imposto devera implementar o calculo de
            acordo com a sua regra
        '''
