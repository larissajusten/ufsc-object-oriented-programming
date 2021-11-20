"""
    Projete e implemente um baralho de cartas genérico, isto é, que poderia ser usado para
    implementar diversos jogos de carta.
"""
from enum import Enum
from random import shuffle

class LocalNoBaralho(Enum):
    BARALHO = 1
    FORA_DO_BARALHO = 2

class Carta:
    def __init__(self, numero: str, naipe: str):
        self.__numero = numero
        self.__naipe = naipe
        self.local_da_carta = LocalNoBaralho.BARALHO.value

    @property
    def numero(self):
        return self.__numero
    
    @property
    def naipe(self):
        return self.__naipe

    @property
    def local_da_carta(self):
        return self.__local_da_carta

    @local_da_carta.setter
    def local_da_carta(self, local_da_carta):
        self.__local_da_carta = local_da_carta
    
    def ModificarLocalDaCarta(self, novo_local):
        self.local_da_carta = novo_local

    def VisualizaInformacoesDaCarta(self):
        return f'[{self.naipe}]: {self.numero}'

class Baralho:
    def __init__(self):
        self.__cartas = []

    @property
    def cartas(self):
        return self.__cartas

    @cartas.setter
    def cartas(self, cartas):
        self.__cartas = cartas

    def __isEmpty(self):
        if not self.cartas:
            print('# BARALHO VAZIO')
            return True
        else:
            return False

    def AdicionarCartas(self, cartas):
        self.cartas = cartas

    def AdicionarUnicaCarta(self, carta, local = 'inicio'):
        if self.__isEmpty():
            self.AdicionarCartas([carta])
        else:
            if local == 'fim':
                self.__cartas.append(carta)
            else: 
                self.__cartas.insert(0, carta)
        print(f'# Carta ({carta.naipe}: {carta.numero}) adicionada com sucesso!')

    def RemoverUnicaCarta(self, local = 'inicio'):
        if self.__isEmpty():
            print(f'# Nao ha cartas para remover!')
            return None
        else:
            carta = ''
            if local == 'fim':
                carta = self.cartas.pop(-1)
            else:
                carta = self.cartas.pop(0)
            print(f'# Carta ({carta.naipe}: {carta.numero}) removida com sucesso!')
            return carta
    
    def RemoverTodasCartas(self):
        if self.__isEmpty():
            print(f'# Nao ha cartas para remover!')
            return None

        self.cartas = []
        print('# Cartas removidas com sucesso!')

    def RetornarBaralho(self):
        if self.__isEmpty():
            return None

        return {id(carta): carta for carta in self.cartas}

    def VisualizarBaralho(self):
        if self.__isEmpty():
            return
        print(f'# Total de cartas: {len(self.cartas)}')
        for carta in self.cartas:
            print(carta.VisualizaInformacoesDaCarta())

    def VisualizarCartas(self, local = LocalNoBaralho.BARALHO.value):
        if self.__isEmpty():
            return
        cartas = [carta for carta in self.cartas if carta.local_da_carta == local]
        if not cartas:
            return print(f'# Nao ha cartas no local selecionado.')
        for carta in cartas:
            print(carta.VisualizaInformacoesDaCarta())

    def Embaralhar(self):
        if self.__isEmpty():
            return None

        print('# Baralho embaralhado!')
        shuffle(self.cartas)

    def MoverTodasCartas(self, local = LocalNoBaralho.FORA_DO_BARALHO.value):
        if self.__isEmpty():
            return None
        if local == LocalNoBaralho.BARALHO.value:
            print('# Cartas movidas para o Baralho!')
            for carta in self.cartas:
                carta.ModificarLocalDaCarta(LocalNoBaralho.BARALHO.value)
        else:
            print('# Cartas movidas para fora do Baralho!')
            for carta in self.cartas:
                carta.ModificarLocalDaCarta(LocalNoBaralho.FORA_DO_BARALHO.value)

def PreCriacaoDeCartasParaBaralhoTeste():
    cartas = []
    naipes = ['ouro', 'paus', 'copas', 'espada']
    numeros = range(1, 14)
    for naipe in naipes:
        for numero in numeros:
            if numero == 1:
                carta = Carta('A', naipe)
            elif numero == 11:
                carta = Carta('J', naipe)
            elif numero == 12:
                carta = Carta('Q', naipe)
            elif numero == 13:
                carta = Carta('K', naipe)
            else:  
                carta = Carta(numero, naipe)
            cartas.append(carta)
    return cartas

def CriarConjunto(nome_conjunto: str):
    nome = nome_conjunto.lower()
    print(f'# Digite "{nome}" da carta a seguir e aperte [ENTER], para sair digite [Z]')

    valores_do_conjunto = []
    valor = ''
    while valor != 'z':
        valor = str(input(f'{nome} da carta: ')).lower()
        if valor != 'z' and not valor.isspace():
            valores_do_conjunto.append(valor)

    return valores_do_conjunto

def CriarCartas(baralho):
    print('# CRIAR CARTAS')
    print('# Vamos comecar com os valores (numeros/letras)!')
    valores = CriarConjunto('valor')

    print('')
    print('# Agora vamos adicionar os naipes!')
    naipes = CriarConjunto('naipe')

    cartas = []
    if naipes and valores:
        for naipe in naipes:
            for valor in valores:
                cartas.append(Carta(valor, naipe))
    return cartas

def CriarCarta():
    print('# CRIAR CARTA')

    valor = ''
    naipe = ''

    while not valor or valor.isspace():
        valor = input('> Digite o valor da carta: ')
    
    while not naipe or naipe.isspace():
        naipe = input('> Digite o naipe da carta: ')

    return Carta(valor, naipe)

def Menu(baralho):
    opcao_escolhida = 0

    while True:
        print('')
        print('# MENU')
        print('[1]: Visualizar todas cartas')
        print('[2]: Visualizar todas cartas no baralho')
        print('[3]: Visualizar todas cartas fora do baralho')
        print('[4]: Substituir baralho por novo baralho')
        print('[5]: Embaralhar')
        print('[6]: Mover todas cartas para fora do baralho')
        print('[7]: Mover todas cartas para o baralho')
        print('[8]: Adicionar uma carta no inicio do baralho')
        print('[9]: Adicionar uma carta no fim do baralho')
        print('[Q]: Remover primeira carta do baralho')
        print('[W]: Remover ultima carta do baralho')
        print('[E]: Remover todas cartas do baralho')
        print('[Z]: Sair')

        opcao_escolhida = input('> Escolha uma opcao: ').upper()
        print('')

        if opcao_escolhida == 'Z':
            break

        if opcao_escolhida == '1':
            print('## BARALHO')
            baralho.VisualizarBaralho()
        elif opcao_escolhida == '2':
            print('## CARTAS NO BARALHO')
            baralho.VisualizarCartas()
        elif opcao_escolhida == '3':
            print('## CARTAS FORA DO BARALHO')
            baralho.VisualizarCartas(local = LocalNoBaralho.FORA_DO_BARALHO.value)
        elif opcao_escolhida == '4':
            print('## SUBSTITUIR BARALHO POR UM NOVO BARALHO')
            baralho.AdicionarCartas(CriarCartas(baralho))
        elif opcao_escolhida == '5':
            print('## EMBARALHAR')
            baralho.Embaralhar()
        elif opcao_escolhida == '6':
            print('## MOVER CARTAS PARA FORA DO BARALHO')
            baralho.MoverTodasCartas()
        elif opcao_escolhida == '7':
            print('## MOVER CARTAS PARA O BARALHO')
            baralho.MoverTodasCartas(local = LocalNoBaralho.BARALHO.value)
        elif opcao_escolhida == '8':
            print('## ADICIONAR CARTA NO INICIO DO BARALHO')
            baralho.AdicionarUnicaCarta(CriarCarta())
        elif opcao_escolhida == '9':
            print('## ADICIONAR CARTA NO FIM DO BARALHO')
            baralho.AdicionarUnicaCarta(CriarCarta(), 'fim')
        elif opcao_escolhida == 'Q':
            print('## REMOVER PRIMEIRA CARTA DO BARALHO')
            baralho.RemoverUnicaCarta()
        elif opcao_escolhida == 'W':
            print('## REMOVER ULTIMA CARTA DO BARALHO')
            baralho.RemoverUnicaCarta(local = 'fim')
        elif opcao_escolhida == 'E':
            print('## REMOVER TODAS CARTAS DO BARALHO')
            baralho.RemoverTodasCartas()
        else:
            print('# Opcao invalida!')

def main():
    print('# Exercicio 6 - Baralho')
    print('# BEM VINDO AO BARALHO')
    print('[Pressione Z para sair]')
    print('')

    baralho = Baralho()
    utilizar_baralho_existente = ''

    while utilizar_baralho_existente != 's' and utilizar_baralho_existente != 'n' and utilizar_baralho_existente != 'z':
        utilizar_baralho_existente = input('# Voce deseja utilizar o baralho pre existente: [S/N/Z] ').lower()
    print('')

    if utilizar_baralho_existente == 'z':
        print('# Finalizando baralho!')
    elif utilizar_baralho_existente == 's':
        baralho.AdicionarCartas(PreCriacaoDeCartasParaBaralhoTeste())
    elif utilizar_baralho_existente == 'n':
        baralho.AdicionarCartas(CriarCartas(baralho))

    while True:        
        Menu(baralho)
        break

if __name__ == '__main__':
    main()
