"""
Arquivo da classe Empresa

Classes:
    Empresa
"""
from impostos import Imposto, IncidenciaImposto, ISS


class Empresa():
    """
    Classe de representação de uma Empresa.

    ...

    Atributos
    ----------
    cnpj : int
        número único que identifica uma pessoa jurídica e outros tipos de
        arranjo jurídico sem personalidade jurídica junto à
        Receita Federal brasileira
    nome_de_fantasia : str
        designação popular de título de estabelecimento utilizada
        por uma instituição, seja pública ou privada, sob o qual
        ela se torna conhecida do público.

    Metodos
    -------
    inclui_imposto(): float
        retorna o valor da diferenca de estado
    diferenca_estado(diferenca_estado: float): None
        define um novo valor para o atributo diferenca_estado
    calcula_aliquota(): float
        calculo da aliquota do imposto ICMS
    """

    def __init__(self, cnpj: int, nome_de_fantasia: str):
        self.__cnpj = cnpj
        self.__nome_de_fantasia = nome_de_fantasia
        self.__impostos = []
        self.__faturamento_servicos = 0.
        self.__faturamento_producao = 0.
        self.__faturamento_vendas = 0.

    @property
    def cnpj(self) -> int:
        '''
        Número único que identifica uma pessoa jurídica e outros
            tipos de arranjo jurídico sem personalidade jurídica junto à
            Receita Federal brasileira

            Retorno:
                cnpj (int): valor do cnpj da empresa
        '''
        return self.__cnpj

    @property
    def nome_de_fantasia(self) -> str:
        '''
        Designação popular de título de estabelecimento utilizada por
            uma instituição, seja pública ou privada, sob o qual
            ela se torna conhecida do público.

            Retorno:
                nome_de_fantasia (str): nome fantasia da empresa
        '''
        return self.__nome_de_fantasia

    @nome_de_fantasia.setter
    def nome_de_fantasia(self, nome_de_fantasia: str) -> None:
        self.__nome_de_fantasia = nome_de_fantasia

    @property
    def impostos(self) -> list:
        '''
        Retorna a lista de impostos da empresa
        @return Lista de impostos da empresa
        '''
        return self.__impostos

    def __has_imposto(self, imposto: Imposto):
        '''
        Verifica se o imposto ja esta cadastrado na lista atual de impostos
            Parametros:
                imposto (Imposto) : imposto a ser verificado
        '''
        if self.impostos and isinstance(imposto, Imposto):
            return next((imp for imp in self.impostos
                         if imp.aliquota == imposto.aliquota
                         and imp.incidencia_imposto ==
                         imposto.incidencia_imposto), False)

    def inclui_imposto(self, imposto: Imposto) -> None:
        '''
        Inclui um imposto na lista de impostos da empresa
        Verifica se o imposto ja esta cadastrado antes de inserir um novo
        @param imposto imposto a ser incluido
        '''
        if not self.__has_imposto(imposto) and isinstance(imposto, Imposto):
            self.__impostos.append(imposto)

    def remove_imposto(self, imposto: Imposto):
        '''
        Exclui um imposto cadastrado
        @param imposto imposto a ser excluido da lista de impostos da empresa
        '''
        if self.__has_imposto(imposto):
            self.__impostos.remove(imposto)

    @property
    def faturamento_servicos(self) -> float:
        '''Valor de faturamentos do tipo servico feitos na empresa'''
        return self.__faturamento_servicos

    @property
    def faturamento_producao(self) -> float:
        '''Valor de faturamentos do tipo producao feitos na empresa'''
        return self.__faturamento_producao

    @property
    def faturamento_vendas(self) -> float:
        '''Valor de faturamentos do tipo vendas feitos na empresa'''
        return self.__faturamento_vendas

    def faturamento_total(self) -> float:
        '''
        Calcula o total dos faturamentos da empresa,
        somando: faturamento_producao,
            faturamento_servicos e faturamento_vendas
        @return Somatorio dos faturamentos
        '''
        fat = self.faturamento_vendas + self.faturamento_producao
        return self.faturamento_servicos + fat

    def total_impostos(self) -> float:
        '''
        Calcula o total de todos os impostos da empresa
        Percorre a lista de impostos da empresa,
        aplicando a aliquota de cada imposto.
        Leva em conta o tipo de cada imposto (IncidenciaImposto) para
        aplicar a aliquota ao faturamento de Producao, Vendas,
        Servicos ou sobre o Total
        @return soma total dos impostos
        '''
        imp_producao = sum([(self.faturamento_producao *
                             (imposto.calcula_aliquota() / 100.0))
                            for imposto
                            in self.impostos
                            if imposto.incidencia_imposto ==
                            IncidenciaImposto.PRODUCAO])

        imp_vendas = sum([(self.faturamento_vendas *
                           (imposto.calcula_aliquota() / 100.0))
                          for imposto
                          in self.impostos
                          if imposto.incidencia_imposto ==
                          IncidenciaImposto.VENDAS])

        imp_servicos = sum([(self.faturamento_servicos *
                             (imposto.calcula_aliquota() / 100.0))
                            for imposto
                            in self.impostos
                            if imposto.incidencia_imposto ==
                            IncidenciaImposto.SERVICOS])

        imp_todos = sum([(self.faturamento_total() *
                          (imposto.calcula_aliquota() / 100.0))
                         for imposto
                         in self.impostos
                         if imposto.incidencia_imposto ==
                         IncidenciaImposto.TODOS])

        return imp_producao + imp_vendas + imp_servicos + imp_todos

    def set_faturamentos(self,
                         fat_servicos: float,
                         fat_producao: float,
                         fat_vendas: float):
        '''
        Define novos valores para os faturamentos de servicoes, producao,
            vendas, respectivamente

            Parametros:
                fat_servicos (float): valor de faturamento de servicos
                fat_producao (float): valor de faturamento de producao
                fat_vendas (float): valor de faturamento de vendas
        '''
        if isinstance(fat_servicos, float):
            self.__faturamento_servicos = fat_servicos
        elif isinstance(fat_servicos, int):
            self.__faturamento_servicos = float(fat_servicos)
        if isinstance(fat_producao, float):
            self.__faturamento_producao = fat_producao
        elif isinstance(fat_producao, int):
            self.__faturamento_producao = float(fat_producao)
        if isinstance(fat_vendas, float):
            self.__faturamento_vendas = fat_vendas
        elif isinstance(fat_vendas, int):
            self.__faturamento_vendas = float(fat_vendas)
