from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andar_atual: int, total_andares_predio: int,
                 capacidade: int, total_pessoas: int) -> None:
        self.__total_andares_predio = total_andares_predio
        self.__andar_atual = andar_atual
        self.__capacidade = capacidade
        self.__total_pessoas = total_pessoas

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, value) -> None:
        self.__capacidade = value

    @property
    def totalPessoas(self) -> int:
        return self.__total_pessoas

    @totalPessoas.setter
    def totalPessoas(self, value) -> None:
        self.__total_pessoas = value

    @property
    def totalAndaresPredio(self) -> int:
        return self.__total_andares_predio

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int) -> None:
        self.__total_andares_predio = totalAndaresPredio

    @property
    def andarAtual(self) -> int:
        return self.__andar_atual

    @andarAtual.setter
    def andarAtual(self, value) -> None:
        self.__andar_atual = value

    # ElevadorJahNoTerreoException
    def descer(self) -> str:
        if (self.andarAtual == 0):
            raise ElevadorJahNoTerreoException()
        else:
            self.andarAtual -= 1

    # ElevadorJahNoUltimoAndarException
    def subir(self) -> str:
        if (self.andarAtual == self.totalAndaresPredio - 1):
            raise ElevadorJahNoUltimoAndarException()
        else:
            self.andarAtual += 1

    # ElevadorCheioException
    def entraPessoa(self) -> str:
        if (self.totalPessoas == self.capacidade):
            raise ElevadorCheioException()
        else:
            self.totalPessoas += 1

    # ElevadorJahVazioException
    def saiPessoa(self) -> str:
        if (self.totalPessoas == 0):
            raise ElevadorJahVazioException()
        else:
            self.totalPessoas -= 1
