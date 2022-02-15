"""
TODO
"""


from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class ISS(Imposto):
    '''TODO'''

    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto):
        super().__init__(aliquota, incidencia_imposto)
        self.__servicos = []

    def inclui_servico(self, nome: str):
        '''TODO'''
        if isinstance(nome, str):
            self.__servicos.append(nome)

    def exclui_servico(self, nome: str):
        '''TODO'''
        has_servico = next((nome for nome in self.__servicos
                            if nome == nome), False)
        if not has_servico:
            self.__servicos.remove(nome)

    def calcula_aliquota(self):
        return self.aliquota - len(self.__servicos)/10
