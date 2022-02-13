from abc import ABC


class Transporte(ABC):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float) -> None:
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def altura(self) -> float:
        return self.__altura

    @altura.setter
    def altura(self, altura: float) -> None:
        self.__altura = altura

    @property
    def comprimento(self) -> float:
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, comprimento: float) -> None:
        self.__comprimento = comprimento

    @property
    def carga(self) -> float:
        return self.__carga

    @carga.setter
    def carga(self, carga: float) -> None:
        self.__carga = carga

    @property
    def velocidade(self) -> float:
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade: float) -> None:
        self.__velocidade = velocidade

    def mostrar_veiculo(self) -> str:
        return f'[{self.nome}] Altura: {self.altura}' + f'\n[{self.nome}] Comprimento: {self.comprimento}' + f'\n[{self.nome}] Carga: {self.carga}' + f'\n[{self.nome}] Velocidade: {self.velocidade}'


class TransporteAereo(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, autonomia: float, envergadura: float) -> None:
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura

    @property
    def autonomia(self) -> float:
        return self.__autonomia

    @property
    def envergadura(self) -> float:
        return self.__envergadura

    def mostrar_veiculo(self) -> str:
        return f'[{self.nome}] Altura: {self.altura}' + f'\n[{self.nome}] Comprimento: {self.comprimento}' + f'\n[{self.nome}] Carga: {self.carga}' + f'\n[{self.nome}] Velocidade: {self.velocidade}' + f'\n[{self.nome}] Autonomia: {self.autonomia}' + f'\n[{self.nome}] Envergadura: {self.envergadura}'


class TransporteTerrestre(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, motor: str, rodas: str) -> None:
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__rodas = rodas

    @property
    def motor(self) -> str:
        return self.__motor

    @property
    def rodas(self) -> str:
        return self.__rodas

    def mostrar_veiculo(self) -> str:
        return f'[{self.nome}] Altura: {self.altura}' + f'\n[{self.nome}] Comprimento: {self.comprimento}' + f'\n[{self.nome}] Carga: {self.carga}' + f'\n[{self.nome}] Velocidade: {self.velocidade}' + f'\n[{self.nome}] Motor: {self.motor}' + f'\n[{self.nome}] Rodas: {self.rodas}'


class TransporteAquatico(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, boca: float, calado: float) -> None:
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    @property
    def boca(self) -> str:
        return self.__boca

    @property
    def calado(self) -> str:
        return self.__calado

    def mostrar_veiculo(self) -> str:
        return f'[{self.nome}] Altura: {self.altura}' + f'\n[{self.nome}] Comprimento: {self.comprimento}' + f'\n[{self.nome}] Carga: {self.carga}' + f'\n[{self.nome}] Velocidade: {self.velocidade}' + f'\n[{self.nome}] Boca: {self.boca}' + f'\n[{self.nome}] Calado: {self.calado}'


class Catalogo:
    def __init__(self) -> None:
        self.__veiculos_cadastrados = []

    @property
    def veiculos_cadastrados(self):
        return self.__veiculos_cadastrados

    def inserir_veiculo(self, veiculo: TransporteTerrestre or TransporteAquatico or TransporteAereo or Transporte) -> None:
        if isinstance(veiculo, TransporteAquatico) or isinstance(veiculo, TransporteTerrestre) or isinstance(veiculo, TransporteAereo):
            self.__veiculos_cadastrados.append(veiculo)
        else:
            print('Valor invalido!')

    def mostrar_veiculos(self):
        for veiculo in self.veiculos_cadastrados:
            print(veiculo.mostrar_veiculo())


if __name__ == '__main__':
    catalogo = Catalogo()
    catalogo.inserir_veiculo(TransporteAquatico(
        'navio', 2, 3, 100, 50, 50, 50))
    catalogo.inserir_veiculo(TransporteTerrestre(
        'carro', 2, 3, 100, 50, 'zetta', 'pirelli'))
    catalogo.inserir_veiculo(TransporteAereo('aviao', 2, 3, 100, 50, 5.8, 7.9))
    catalogo.inserir_veiculo('')
    catalogo.mostrar_veiculos()
