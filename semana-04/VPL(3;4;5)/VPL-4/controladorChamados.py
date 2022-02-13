from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = defaultdict()
        self.__tipoChamados = []

    @property
    def chamados(self):
        return self.__chamados

    @chamados.setter
    def chamados(self, chamado):
        self.__chamados[id(chamado)] = chamado

    @property
    def tipoChamados(self):
        return self.__tipoChamados

    @tipoChamados.setter
    def tipoChamados(self, tipoChamados):
        self.__tipoChamados.append(tipoChamados)

    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        if isinstance(cliente, Cliente) and isinstance(tecnico, Tecnico) and isinstance(tipo, TipoChamado):
            existe_chamado = next((chamado for chamado in self.chamados.values()
                                   if chamado.cliente.codigo == cliente.codigo
                                   and chamado.tecnico.codigo == tecnico.codigo
                                   and chamado.tipo.codigo == tipo.codigo), False)
            if not existe_chamado:
                chamado = Chamado(data, cliente, tecnico,
                                  titulo, descricao, prioridade, tipo)
                self.chamados = chamado
                return chamado

    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        existe_tipoChamado = next((tipoChamado for tipoChamado in self.tipoChamados
                                   if tipoChamado.codigo == codigo
                                   and tipoChamado.nome == nome
                                   and tipoChamado.descricao == descricao), False)

        if not existe_tipoChamado:
            tipoChamado = TipoChamado(codigo, descricao, nome)
            self.tipoChamados = tipoChamado
            return tipoChamado

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        quantidade_chamados = [
            chamado for chamado in self.chamados.values() if chamado.tipo.codigo == tipo.codigo]
        return len(quantidade_chamados)
