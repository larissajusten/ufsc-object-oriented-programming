from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__tecnicos = []
        self.__clientes = []

    @property
    def tecnicos(self):
        return self.__tecnicos

    @tecnicos.setter
    def tecnicos(self, tecnico):
        self.__tecnicos.append(tecnico)

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self, cliente):
        self.__clientes.append(cliente)

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        existe_cliente = next((cliente for cliente in self.clientes
                               if cliente.codigo == codigo), False)
        if not existe_cliente:
            novo_cliente = Cliente(nome, codigo)
            self.clientes = novo_cliente
            return novo_cliente

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        existe_tecnico = next((tecnico for tecnico in self.tecnicos
                               if tecnico.codigo == codigo), False)
        if not existe_tecnico:
            novo_tecnico = Tecnico(nome, codigo)
            self.tecnicos = novo_tecnico
            return novo_tecnico
