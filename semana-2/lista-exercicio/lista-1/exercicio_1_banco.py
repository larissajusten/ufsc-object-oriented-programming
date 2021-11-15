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
from datetime import datetime
import re

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

    def VisualizarClientes(self):
        for conta in self.contasPoupança + self.contasCorrente + self.contasEspeciais:
            conta.VisualizarTitulares()

    def VisualizarInformacoesContas(self):
        print('')
        print('# CONTAS POUPANCA')
        for i, conta in enumerate(self.contasPoupança):
            print(f'Conta {i}')
            print(f'[Saldo]: {conta.saldo}')
            conta.VisualizarTitulares()
        
        print('')
        print('# CONTAS CORRENTE')
        for i, conta in enumerate(self.contasCorrente):

            print(f'Conta {i+len(self.contasPoupança)}')
            print(f'[Saldo]: {conta.saldo}')
            conta.VisualizarTitulares()

        print('')
        print('# CONTAS ESPECIAIS')
        for i, conta in enumerate(self.contasEspeciais):
            print(f'Conta {i+len(self.contasPoupança)+len(self.contasCorrente)}')
            print(f'[Saldo]: {conta.saldo}')
            conta.VisualizarTitulares()

    def ProcurarConta(self, nome):
        for conta in self.contasPoupança + self.contasCorrente + self.contasEspeciais:
            conta_encontrada = [conta for titular in conta.titulares if nome.lower() in titular.nome.lower()]
            if conta_encontrada: 
                return conta_encontrada[0]
        return False

    def ProcurarCliente(self, nome):
        for conta in self.contasPoupança + self.contasCorrente + self.contasEspeciais:
            cliente = [titular.nome for titular in conta.titulares if nome.lower() in titular.nome.lower()]
            if cliente: 
                return cliente[0]
        return False

class Conta(ABC):
    def __init__(self, titulares):
        self.__saldo = 0
        self.__titulares = titulares
        self.__extrato = []

    @property
    def saldo(self):
        return self.__saldo

    @property
    def extrato(self):
        return self.__extrato

    @property
    def titulares(self):
        return self.__titulares

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @extrato.setter
    def extrato(self, nova_operacao):
        self.extrato.append(nova_operacao)

    @abstractmethod
    def InformacoesEspecificasDaConta(self):
        print(f'# Saldo: {self.saldo}')

    def Sacar(self, valor):
        if valor < 0:
            raise ValueError('# Valor invalido!')
        elif valor > self.saldo:
            print('# Saldo insuficiente! Não foi possivel realizar a operação.')
        else:
            self.saldo = self.saldo - valor
            print(f'# Saque de R$ {valor} realizado com sucesso!')
            print(f'# Saldo: {self.saldo}')
            self.extrato = f'# (Saldo) Saque de R$ {valor} -> {round(self.saldo, 2)}'

    def Depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print(f'# Deposito de R$ {valor} realizado com sucesso!')
            print(f'# Saldo: {self.saldo}')
            self.extrato = f'# (Saldo) Deposito de R$ {valor} -> {self.saldo}'
        else:
            raise ValueError('# Valor invalido!')

    def TirarExtrato(self):
        print('# Extrato:')
        print(f'# Saldo: {self.saldo}')
        for i, operacao in enumerate(self.extrato):
            print(f'[{i}]: {operacao}')

    def VisualizarTitulares(self):
        for titular in self.titulares:
            print(f'[{titular.nome}]: {titular.telefone}')

class ContaEspecial(Conta):
    def __init__(self, titulares):
        super().__init__(titulares)
        self.__limite_especial = 400

    @property
    def limite_especial(self):
        return self.__limite_especial

    @limite_especial.setter
    def limite_especial(self, novo_limite_especial):
        self.__limite_especial = novo_limite_especial

    def InformacoesEspecificasDaConta(self):
        print(f'# Saldo: {self.saldo} - Limite Especial: {self.limite_especial}')

    def Sacar(self, valor):
        if valor < 0:
            raise ValueError('# Valor invalido!')
        elif (valor > self.saldo and self.limite_especial > (valor - self.saldo)) or valor == (self.saldo + self.limite_especial):
            resp = input('> Deseja utilizar o limite especial? [S/N]: ')[0].upper()
            if resp == 'S':
                self.__SacarLimiteEspecial(valor - self.saldo)
                if self.saldo != 0:
                    self.extrato = f'# (Saldo) Saque de R$ {valor} -> {round(self.saldo, 2)}'
                self.extrato = f'# (Limite Especial) Saque de {round(valor - self.saldo, 2)} no limite especial -> {round(self.limite_especial, 2)}'
                self.saldo = 0

                print(f'# Saque de R$ {valor} realizado com sucesso!')
                print(f'# Saldo: {self.saldo} - Limite Especial: {self.limite_especial}')
            else:
                print('# Saldo insuficiente! Não foi possivel realizar a operação.')
        elif valor > self.saldo:
            print('# Saldo insuficiente! Não foi possivel realizar a operação.')
        else:
            self.saldo = self.saldo - valor
            print(f'# Saque de R$ {valor} realizado com sucesso' )
            print(f'# Saldo: {self.saldo} - Limite Especial: {self.limite_especial}')
            self.extrato = f'# (Saldo) Saque de R$ {valor} -> {round(self.saldo, 2)}'

    def __SacarLimiteEspecial(self, valor):
        self.limite_especial = self.limite_especial - valor

    def Depositar(self, valor):
        if valor > 0 and self.limite_especial < 400:
            valor_faltante_limite_especial = 400 - self.limite_especial

            if valor > valor_faltante_limite_especial:
                self.limite_especial += valor_faltante_limite_especial
                self.saldo += valor - valor_faltante_limite_especial
                self.extrato = f'# (Saldo) Deposito de R$ {valor - valor_faltante_limite_especial} no saldo -> {self.saldo}'
                self.extrato = f'# (Limite Especial) Deposito de R$ {valor_faltante_limite_especial} no limite especial -> {self.limite_especial}'
            else:
                self.limite_especial += valor
                self.extrato = f'# (Saldo) Deposito de R$ {0} no saldo -> {self.saldo}'
                self.extrato = f'# (Limite Especial) Deposito de R$ {valor} no limite especial -> {self.limite_especial}'
                
            print(f'# Deposito de R$ {valor} realizado com sucesso!')
            print(f'# Saldo: {self.saldo} - Limite Especial: {self.limite_especial}')
        elif valor > 0:
            self.saldo = self.saldo + valor
            print(f'# Deposito de R$ {valor} realizado com sucesso!')
            print(f'# Saldo: {self.saldo} - Limite Especial: {self.limite_especial}')
            self.extrato = f'# (Saldo) Deposito de R$ {valor} -> {self.saldo}'
        else:
            raise ValueError('# Valor invalido!')

class ContaCorrente(Conta):
    def __init__(self, titulares):
        super().__init__(titulares)

    def InformacoesEspecificasDaConta(self):
        print(f'# Saldo: {self.saldo}')
    
class ContaPoupanca(Conta):
    def __init__(self, titulares, data_de_criacao = datetime.now()):
        super().__init__(titulares)
        self.__rendimento = 1.5
        self.__data_de_criacao = data_de_criacao

    @property
    def rendimento(self):
        return self.__rendimento

    @property
    def data_de_criacao(self):
        return self.__data_de_criacao

    def InformacoesEspecificasDaConta(self):
        print(f'# Saldo: {self.saldo} - Data de criacao: {self.data_de_criacao.strftime("%m/%d/%Y")} - Rendimentos: {self.rendimento}')

    def CalcularRendimentoMensal(self):
        now = datetime.now()
        meses = (now.year - self.data_de_criacao.year) * 12 + now.month - self.data_de_criacao.month
        saldo_por_mes = (self.saldo * (self.rendimento/100))
        self.saldo += (meses * saldo_por_mes)

def PreCriacaoDeClientes():
    clienteJoao = Cliente('Joao', '51 98171 0800')
    clienteMaria = Cliente('Maria', '51 98899 5678')
    clienteLincoln = Cliente('Lincoln', '51 30980789')
    clienteGiovana = Cliente('Giovana', '48 99322 8741')
    clienteJonata = Cliente('Jonata Tyska Carvalho', '51 90801 0801')
    clienteMateus = Cliente('Mateus Grellert', '51 90800 0800')
    return [clienteJoao, clienteMaria, clienteLincoln, clienteGiovana, clienteJonata, clienteMateus]

def Menu(tatu, conta):
    print('# MENU')
    opcao_escolhida = 0

    while True:
        print('')
        print('[1]: Visualizar todas contas do banco tatu')
        print('[2]: Visualizar todos clientes do banco tatu')
        print('[3]: Sacar')
        print('[4]: Depositar')
        print('[5]: Tirar extrato')
        print('[6]: Informacoes Especificas da Conta')
        print('[z]: Sair')

        opcao_escolhida = input('> Escolha uma opcao: ')

        if opcao_escolhida == 'z':
            exit()

        if opcao_escolhida == '1':
            tatu.VisualizarInformacoesContas()
        elif opcao_escolhida == '2':
            print('')
            tatu.VisualizarClientes()
        elif opcao_escolhida == '3':
            print('')
            valor = float(input('> Digite um valor que deseja sacar: '))
            conta.Sacar(valor)
        elif opcao_escolhida == '4':        
            print('')
            valor = float(input('> Digite o valor que deseja depositar: '))
            conta.Depositar(valor)
        elif opcao_escolhida == '5':
            print('')
            conta.TirarExtrato()        
        elif opcao_escolhida == '6':
            print('')
            conta.InformacoesEspecificasDaConta()
        else:
            print('# Opcao invalida!')

def CriarConta(banco):
    print('# CRIACAO DE CONTA')
    nome = input('> Digite seu nome: ')
    telefone = input('> Digite seu telefone com DDD (somente numeros): ')
    novoCliente = Cliente(nome, telefone)

    tipo_de_conta = ''
    while tipo_de_conta not in ['corrente', 'poupanca', 'corrente', 'z']:
        tipo_de_conta = input('> Escolha o tipo de conta: [CORRENTE/POUPANCA/ESPECIAL]').lower()
        if tipo_de_conta == 'z':
            exit()
        elif tipo_de_conta == 'corrente':
            banco.AdicionarContaCorrente(ContaCorrente([novoCliente]))
        elif tipo_de_conta == 'poupanca':
            banco.AdicionarContaPoupanca(ContaPoupanca([novoCliente]))
        elif tipo_de_conta == 'especial':
            banco.AdicionarContaEspecial(ContaEspecial([novoCliente]))
    return nome

def main():
    print('# BEM VINDO AO BANCO TATU')
    print('[Pressione Z para sair]')
    print('')

    sair = False
    tatu = Banco()

    clientes = PreCriacaoDeClientes()
    contasPoupanca = ContaPoupanca(clientes[:3], data_de_criacao = datetime(2021,10,14))
    contasCorrente = ContaCorrente(clientes[3:5])
    contasEspecial = ContaEspecial(clientes[5:])
    tatu.AdicionarContaPoupanca(contasPoupanca)
    tatu.AdicionarContaCorrente(contasCorrente)
    tatu.AdicionarContaEspecial(contasEspecial)

    nome = ''

    while not sair:
        verify_exite_conta = ''
        while verify_exite_conta != 's' and verify_exite_conta != 'n' and verify_exite_conta != 'z':
            verify_exite_conta = input('# Voce ja tem uma conta: [S/N/Z] ').lower()

        if verify_exite_conta == 's':
            nome = input('> Digite seu nome e sobrenome: ')
            cliente = tatu.ProcurarCliente(nome)
            if cliente:
                print('')
                conta = tatu.ProcurarConta(nome)
                nome_conta = str(re.sub(r"(\w)([A-Z])", r"\1 \2", type(conta).__name__))
                print(f'# Ola {cliente}! {nome_conta}')
                conta.InformacoesEspecificasDaConta()
                print('')
            else:
                print('# Cliente nao encontrado!')
        elif verify_exite_conta == 'z':
            exit()
        else:
            nome = CriarConta(tatu)

        Menu(tatu, tatu.ProcurarConta(nome))

main()