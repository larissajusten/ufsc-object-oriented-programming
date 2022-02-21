"""
Arquivo da classe Imposto

Classes:
    ISS
"""
from . import Imposto, IncidenciaImposto


class ISS(Imposto):
    """
    Classe de representação do Imposto ISS.

    ...

    Atributos
    ----------
    aliquota : float
        percentual ou valor fixo que será aplicado para o cálculo do valor
        de um tributo
    incidencia_imposto : IncidenciaImposto
        maneira pela qual a carga tributária é dividida entre compradores
        e vendedores
    servicos: list
        lista de Servicos do ISS

    Metodos
    -------
    inclui_servico(nome: str): None
        inclui servico na lista de servicos
    exclui_servico(nome: str): None
        remove servico da lista de servicos
    calcula_aliquota(): float
        calculo da aliquota do imposto ISS
    """

    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto):
        super().__init__(aliquota, incidencia_imposto)
        self.__servicos = []

    def inclui_servico(self, nome: str):
        '''
        Inclui um servico na lista de servicos do ISS
            Parametros:
                nome (str) : nome do servico a ser incluido

            Retorno:
                None
        '''
        if isinstance(nome, str):
            self.__servicos.append(nome)

    def exclui_servico(self, nome: str):
        '''
        Remove um servico na lista de servicos do ISS
            Parametros:
                nome (str) : nome do servico a ser removido

            Retorno:
                None
        '''
        has_servico = next((nome for nome in self.__servicos
                            if nome == nome), False)
        if not has_servico:
            self.__servicos.remove(nome)

    def calcula_aliquota(self):
        return self.aliquota - len(self.__servicos) / 10
