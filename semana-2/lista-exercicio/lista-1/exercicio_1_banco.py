"""
Exercício 1: Banco
    O banco Tatu, moderno e eficiente, precisa de um novo programa para controlar o saldo de seus correntistas.

    Cada conta corrente pode ter um ou mais clientes como titular. 
    O banco controla apenas o nome e o telefone de cada cliente. 
    A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos. 
    
    Quando o cliente fizer um saque, diminuiremos o saldo da conta corrente. 
    Quando ele fizer um depósito, aumentaremos o saldo. 
    
    O banco oferece também contas especiais, com limite especial além do saldo, e conta poupança, 
        que oferece um rendimento mensal sempre que o saldo na conta completa um mês. 
    Evidentemente é necessário oferecer aos clientes a possibilidade de verificar saldos, extratos 
        e um resumo com todas as informações da conta e seus respectivos clientes.
"""
from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

class Banco:
    def __init__(self):
        self.__contasCorrente = []
        self.__contasEspeciais = []
        self.__contasPoupança = []

    @property
    def contasCorrente(self):
        return self.__contasCorrente

    @property
    def contasEspeciais(self):
        return self.__contasEspeciais

    @property
    def contasPoupança(self):
        return self.__contasPoupança

    @contasCorrente.setter
    def contasCorrente(self, nova_conta):
        self.contasCorrente.append(nova_conta)

    @contasEspeciais.setter
    def contasEspeciais(self, nova_conta):
        self.contasEspeciais.append(nova_conta)

    @contasPoupança.setter
    def contasPoupança(self, novaConta):
        self.contasPoupança.append(novaConta)

    def AdicionarContaCorrente(self, novaConta):
        self.contasCorrente = novaConta

    def AdicionarContaEspecial(self, novaConta):
        self.contasEspeciais = novaConta

    def AdicionarContaPoupanca(self, novaConta):
        self.contasPoupança = novaConta

class ContaCorrente:
    def __init__(self, titulares):
        self.__saldo = 0
        self.__titulares = titulares
        self.__extrato = []
        self.__limite_especial = 400

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def titulares(self):
        return self.__titulares

    @property
    def extrato(self):
        return self.__extrato

    @extrato.setter
    def extrato(self, nova_operacao):
        self.extrato.append(nova_operacao)

    @property
    def limite_especial(self):
        return self.__limite_especial

    @limite_especial.setter
    def limite_especial(self, novo_limite_especial):
        self.__limite_especial = novo_limite_especial

    def Depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            self.extrato = f'# Deposito de {valor}                       |      {self.saldo}'
        else:
            raise ValueError('!Valor invalido!')

    def Sacar(self, valor):
        if valor < 0:
            raise ValueError('Valor invalido!')
        elif valor > self.saldo and (valor - self.saldo) < self.limite_especial:
            resp = input('> Deseja utilizar o limite especial? [S/N]: ')[0].upper()
            if resp == 'S':
                self.SacarLimiteEspecial(valor - self.saldo)
                self.extrato = f'# Saque de {valor}                            |      {round(self.saldo, 2)}'
                self.extrato = f'# Saque de {round(valor - self.saldo, 2)} no limite especial        |      {round(self.limite_especial, 2)}'
                self.saldo = 0
            else:
                print('Limite insuficiente! Não foi possivel realizar a operação. Por favor tente novamente.')
        elif valor > self.saldo:
            print('Limite insuficiente! Não foi possivel realizar a operação. Por favor tente novamente.')
        else:
            self.saldo = self.saldo - valor
            self.extrato = f'# Saque de {valor}                            |      {round(self.saldo, 2)}'

    def SacarLimiteEspecial(self, valor):
        self.limite_especial = self.limite_especial - valor

    def TirarExtrato(self):
        print('# Extrato:')
        for i, operacao in enumerate(self.extrato):
            print(f'[{i}]: {operacao}')

def main():
    clienteJoao = Cliente('Joao', '51 98171 0800')
    clienteMaria = Cliente('Maria', '51 98899 5678')

    contaCorreteJoaoMaria = ContaCorrente([clienteJoao, clienteMaria])

    tatu = Banco()
    tatu.AdicionarContaCorrente(contaCorreteJoaoMaria)

    print('[clienteJoao]: nome ', clienteJoao.nome, ' numero: ', clienteJoao.telefone)
    print('[clienteMaria]: nome ', clienteMaria.nome, ' numero: ', clienteMaria.telefone)
    print('[contaCorreteJoaoMaria]: saldo ', contaCorreteJoaoMaria.saldo)
    contaCorreteJoaoMaria.Depositar(50.8)
    print('[contaCorreteJoaoMaria +50 no saldo]: saldo ', contaCorreteJoaoMaria.saldo)
    contaCorreteJoaoMaria.Sacar(60)
    print('[contaCorreteJoaoMaria -50 no saldo]: saldo ', contaCorreteJoaoMaria.saldo)
    contaCorreteJoaoMaria.TirarExtrato()

main()