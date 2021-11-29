class Pessoa:
    def __init__(self, nome: str, cpf: str, dinheiro: float):
        self.__nome = nome
        self.__cpf = cpf
        self.__dinheiro = dinheiro

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def dinheiro(self):
        return self.__dinheiro

    @dinheiro.setter
    def dinheiro(self, valor: float):
        self.__dinheiro = valor


class Veiculo:
    staticVar = "abc"

    def __init__(self, modelo: str, cor: str, dono: Pessoa):
        self.__modelo = modelo
        self.__cor = cor
        self.__dono = dono
        self.__velocidade = 0
        self.__sujo = True

    @property
    def modelo(self):
        return self.__modelo

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, nova_cor: str):
        self.__cor = nova_cor

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, novo_dono: Pessoa):
        self.__dono = novo_dono

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, valor: int):
        self.__velocidade = valor

    @property
    def sujo(self):
        return self.__sujo

    @sujo.setter
    def sujo(self, sujo):
        self.__sujo = sujo

    def lavar(self):
        total = self.dono.dinheiro
        if total >= 30:
            self.dono.dinheiro = total - 30
            self.__sujo = False

    def frear(self):
        pass


class Carro(Veiculo):
    def __init__(self, modelo: str, cor: str, placa: str, dono: Pessoa):
        super().__init__(modelo, cor, dono)
        self.__placa = placa

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, nova_placa: str):
        self.__placa = nova_placa

    def buzinar(self):
        print(self.__modelo, 'buzinou!')

    def acelerar(self, valor: int):
        self.velocidade += valor

    def frear(self):
        self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0


class Bicicleta(Veiculo):
    def __init__(self, modelo: str, cor: str, marchas: int, amortecedor: bool, dono: Pessoa):
        super().__init__(modelo, cor, dono)
        self.__marchas = marchas
        self.__amortecedor = amortecedor

    @property
    def marchas(self):
        return self.__marchas

    @marchas.setter
    def marchas(self, novas_marchas: int):
        self.__marchas = novas_marchas

    @property
    def amortecedor(self):
        return self.__amortecedor

    @amortecedor.setter
    def amortecedor(self, novo_amortecedor: bool):
        self.__amortecedor = novo_amortecedor

    def pedalar(self, valor: int):
        self.velocidade += valor

    def lavar(self):
        total = self.dono.dinheiro
        if total >= 10:
            self.dono.dinheiro = total - 10
            self.__sujo = False

    def frear(self):
        self.velocidade -= 1
        if self.velocidade < 0:
            self.velocidade = 0


joao = Pessoa('Joao Silva', '123.456.789-0', 50)
carro1 = Carro('Gol', 'Vermelho', 'ABC-1234', joao)
bicicleta1 = Bicicleta('Caloi 10', 'Vermelha', 12, False, joao)

print(joao.nome, ', Dinheiro = R$', joao.dinheiro)
print(carro1.modelo, carro1.placa, ', Velocidade =', carro1.velocidade, 'km/h')
print(bicicleta1.modelo, ',', bicicleta1.marchas, 'marchas, Velocidade =',
      bicicleta1.velocidade, 'km/h, Sujo=', bicicleta1.sujo)

carro1.acelerar(80)
bicicleta1.pedalar(5)
carro1.lavar()
bicicleta1.lavar()

print(joao.nome, ', Dinheiro = R$', joao.dinheiro)
print(carro1.modelo, carro1.placa, ', Velocidade =', carro1.velocidade, 'km/h')
print(bicicleta1.modelo, ',', bicicleta1.marchas, 'marchas, Velocidade =',
      bicicleta1.velocidade, 'km/h, Sujo=', bicicleta1.sujo)

# Pergunta:
# o que acontece se, ao invés de criarmos o método setter como dito acima, alterarmos o código do método lavar() da classe Bicicleta para
# alterar diretamente o atributo privado: self.__sujo = False? O código apresentará um erro? Funcionará corretamente? O que acontece? Teste isso!
# R: Não consegue acessar o atributo e mudar seu valor.
