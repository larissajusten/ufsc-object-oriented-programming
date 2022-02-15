"""
    TODO
"""

from impostos.imposto import Imposto
from impostos.incidencia_imposto import IncidenciaImposto


class Empresa():
    '''TODO'''

    def __init__(self, cnpj: int, nome_de_fantasia: str):
        self.__cnpj = cnpj
        self.__nome_de_fantasia = nome_de_fantasia
        self.__impostos = []
        self.__faturamento_servicos: float = 0.
        self.__faturamento_producao: float = 0.
        self.__faturamento_vendas: float = 0.

    @property
    def cnpj(self) -> int:
        '''TODO'''
        return self.__cnpj

    @property
    def nome_de_fantasia(self) -> str:
        '''TODO'''
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
            Verifica se o imposto ja esta cadastrado na lista de impostos
        '''
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
        if not self.__has_imposto(imposto):
            self.__impostos.append(imposto)

    def remove_imposto(self, imposto: Imposto):
        '''
            Exclui um imposto cadastrado
            @param imposto imposto a ser excluido da lista de impostos da empresa
        '''
        if not self.__has_imposto(imposto):
            self.__impostos.append(imposto)

    @property
    def faturamento_servicos(self) -> list:
        '''TODO'''
        return self.__faturamento_servicos

    @property
    def faturamento_producao(self) -> list:
        '''TODO'''
        return self.__faturamento_producao

    @property
    def faturamento_vendas(self) -> list:
        '''TODO'''
        return self.__faturamento_vendas

    def faturamento_total(self) -> float:
        '''
            Calcula o total dos faturamentos da empresa,
            somando: faturamento_producao,
                faturamento_servicos e faturamento_vendas
            @return Somatorio dos faturamentos
        '''
        return sum(self.faturamento_servicos + self.faturamento_vendas
                   + self.faturamento_producao)

    def total_impostos(self) -> float:
        '''
            Calcula o total de todos os impostos da empresa
            Percorre a lista de impostos da empresa,
            aplicando a aliquota de cada imposto.
            Leva em conta o tipo de cada imposto (IncidenciaImposto) para
            aplicar a aliquota ao faturamento de Producao, Vendas,
            Servicos ou sobre o Total
            @return
        '''
        imp_producao = sum([(self.faturamento_producao *
                             (imposto.calcula_aliquota()/100))
                            for imposto
                            in self.impostos
                            if imposto.incidencia_imposto ==
                            IncidenciaImposto.PRODUCAO])

        imp_vendas = sum([(self.faturamento_vendas *
                           (imposto.calcula_aliquota()/100))
                          for imposto
                          in self.impostos
                          if imposto.incidencia_imposto ==
                          IncidenciaImposto.VENDAS])

        imp_servicos = sum([(self.faturamento_servicos *
                             (imposto.calcula_aliquota()/100))
                            for imposto
                            in self.impostos
                            if imposto.incidencia_imposto ==
                            IncidenciaImposto.SERVICOS])

        fat_todos = self.faturamento_servicos + \
            self.faturamento_producao + self.faturamento_vendas

        imp_todos = sum([(fat_todos * (imposto.calcula_aliquota()/100))
                         for imposto
                         in self.impostos
                         if imposto.incidencia_imposto ==
                         IncidenciaImposto.TODOS])

        return imp_producao + imp_vendas + imp_servicos + imp_todos

    def set_faturamentos(self,
                         fat_servicos: float,
                         fat_producao: float,
                         fat_vendas: float):
        '''TODO'''
        if isinstance(fat_servicos, float):
            self.__faturamento_servicos = fat_servicos
        if isinstance(fat_producao, float):
            self.__faturamento_producao = fat_producao
        if isinstance(fat_vendas, float):
            self.__faturamento_vendas = fat_vendas
