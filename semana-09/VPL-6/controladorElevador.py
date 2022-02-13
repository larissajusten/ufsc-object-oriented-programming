from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    @elevador.setter
    def elevador(self, value: Elevador):
        self.__elevador = value

    def subir(self) -> str:
        self.elevador.subir()

    def descer(self) -> str:
        self.elevador.descer()

    def entraPessoa(self) -> str:
        self.elevador.entraPessoa()

    def saiPessoa(self) -> str:
        self.elevador.saiPessoa()

    def validateValues(self, values):
        return all(isinstance(value, int) and value >= 0 for value in values)

    def validadeAndares(self, andarAtual, totalAndaresPredio):
        return andarAtual <= totalAndaresPredio

    def validadeCapacidade(self, capacidade, totalPessoas):
        return totalPessoas <= capacidade

    def inicializarElevador(
            self, andarAtual: int, totalAndaresPredio: int, capacidade: int,
            totalPessoas: int):
        if (self.validateValues([andarAtual, totalAndaresPredio, capacidade,
                                totalPessoas])):
            if(self.validadeAndares(andarAtual, totalAndaresPredio - 1)
               and self.validadeCapacidade(capacidade, totalPessoas)):
                self.elevador = Elevador(
                    andarAtual, totalAndaresPredio, capacidade, totalPessoas)
            else:
                raise ComandoInvalidoException()
        else:
            raise ComandoInvalidoException()
