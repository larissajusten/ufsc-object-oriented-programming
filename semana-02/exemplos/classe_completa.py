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

        
class Carro:
    def __init__(self, modelo: str, cor: str, placa: str, dono: Pessoa):
        self.__modelo = modelo
        self.__cor = cor
        self.__placa = placa
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
    def placa(self):
        return self.__placa
    
    @placa.setter
    def placa(self, nova_placa: str):
        self.__placa = nova_placa
    
    @property
    def dono(self):
        return self.__dono
    
    @dono.setter
    def dono(self, novo_dono: Pessoa):
        self.__dono = novo_dono
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def sujo(self):
        return self.__sujo
    
    def lavar(self):
        total = self.dono.dinheiro
        if total >= 30:
            self.dono.dinheiro = total - 30
            self.__sujo = False
        else:
            print(f"Desculpe, não será possível lavar o {self.modelo} de placas {self.placa}. A lavagem custa 30 reais e o dono do carro possui apenas {self.dono.dinheiro}")
    
    def buzinar(self):
        print(self.__modelo, 'buzinou!')
        
    def acelerar(self, valor: int):
        self.__velocidade += valor
        
    def frear(self):
        self.__velocidade -= 10
        if self.__velocidade < 0:
            self.__velocidade = 0
                     
joao = Pessoa('Joao Silva', '123.456.789-0', 50)
carro1 = Carro('Gol', 'Vermelho', 'ABC-1234', joao)
carro2 = Carro('Fox', 'Preto', 'XYZ-9876', joao)

print(carro1.modelo, ', Sujo =', carro1.sujo)
print(carro2.modelo, ', Sujo =', carro2.sujo)
print(joao.nome, ', Dinheiro = R$', joao.dinheiro)

carro1.lavar()
carro2.lavar()

print(carro1.modelo, ', Sujo =', carro1.sujo)
print(carro2.modelo, ', Sujo =', carro2.sujo)
print(joao.nome, ', Dinheiro = R$', joao.dinheiro)

print('O que aconteceria se o atributo sujo fosse público e pudesse ser setado para False por atribuição direta?')
print('No contexto do exercicio: ele poderia voltar a ficar sujo mesmo após lavagem')
