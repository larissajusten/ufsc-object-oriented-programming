class Capitulo:
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo = titulo

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int) -> None:
        self.__numero = numero

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self.__titulo = titulo
