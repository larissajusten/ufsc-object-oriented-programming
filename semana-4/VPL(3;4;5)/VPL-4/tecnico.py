from pessoa import Pessoa


class Tecnico(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
