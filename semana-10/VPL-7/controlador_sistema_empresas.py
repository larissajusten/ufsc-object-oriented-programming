"""
Arquivo da classe ControladorSistemaEmpresas

Classes:
    ControladorSistemaEmpresas
"""
from . import Empresa, EmpresaDAO, EmpresaDuplicadaException


class ControladorSistemaEmpresas():
    """
    Classe de representação do Controlador do Sistemas de Empresas.

    ...

    Atributos
    ----------

    Metodos
    -------
    inclui_empresa(empresa: Empresa):
        Inclui empresa no sistema
    exclui_empresa(empresa: Empresa):
        Exclui empresa no sistema
    busca_empresa_pelo_cnpj(cnpj: int): Empresa
        Busca cnpj no sistema e retorna Empresa correspondente
    calcula_total_impostos(): float
        Retorna a soma do calculo total de todos impostos de todas
        empresas no sistema
    """

    def __init__(self):
        self.__empresa_dao = EmpresaDAO()

    def __existe_empresa(self, empresa: Empresa):
        empresas = list(dict(self.__empresa_dao.get_all()).values())
        return next((emp for emp in empresas
                    if emp.cnpj == empresa.cnpj), False)

    def inclui_empresa(self, empresa: Empresa):
        '''
        Permite incluir uma empresa utilizando a EmpresaDAO.
        Valida pelo CNPJ se a empresa ja esta cadastrada
        Utiliza a EmpresaDAO para buscar as empresas
        @param empresa objeto Empresa que sera incluido
        @throws EmpresaDuplicadaException Excecao gerada quando se
            tenta incluir uma empresa com CNPJ ja cadastrado
        '''
        if self.__existe_empresa(empresa):
            raise EmpresaDuplicadaException()
        elif isinstance(empresa, Empresa):
            self.__empresa_dao.add(empresa.cnpj, empresa)

    def exclui_empresa(self, empresa: Empresa):
        '''
        Permite excluir uma empresa cadastrada na EmpresaDAO
        @param empresa empresa que sera excluida
        '''
        if self.__existe_empresa(empresa):
            self.__empresa_dao.remove(empresa.cnpj)

    def busca_empresa_pelo_cnpj(self, cnpj: int) -> Empresa:
        '''
        Permite buscar uma empresa na lista de empresas pelo CNPJ
        Utiliza a EmpresaDAO para buscar as empresas
        @param cnpj numero do CNPJ da empresa desejada
        @return retorna None se a empresa nao for encontrada
        '''
        if isinstance(cnpj, int):
            return self.__empresa_dao.get(cnpj)

    @property
    def empresas(self) -> list:
        '''
        Retorna a lista de empresas cadastradas
        Utiliza a EmpresaDAO para buscar as empresas
        @return lista de empresas cadastradas
        '''
        return list(dict(self.__empresa_dao.get_all()).values())

    def calcula_total_impostos(self) -> float:
        '''
        Calcula o total de impostos de todas as empresas.
        Invoca a operacao total_impostos() de cada uma
        das empresas cadastradas no Dicionario, somando os resultados
        Utiliza a EmpresaDAO para buscar as empresas
        @return somatorio dos impostos de todas as empresas cadastradas
        '''
        empresas_dict = dict(self.__empresa_dao.get_all()).values()
        empresas_cadastradas = list(empresas_dict)
        return sum(empresa.total_impostos() for empresa
                   in empresas_cadastradas)
