# 1) [X] Crie a classe Televisao com os atributos ligada (inicializado com valor False) e canal (inicializado com valor 2).
# 2) [X] Adicione os atributos tamanho e marca à classe Televisao. Crie dois objetos Televisao e atribua tamanhos e marcas diferentes. 
#       Depois, imprima o valor desses atributos de forma a confirmar independência dos valores de cada instância (objeto).
# 3) [X] Adicione dois novos métodos muda_canal_para_cima e muda_canal_para_baixo.
#       Atualmente, a classe Televisao inicializa o canal com 2. Modifique a classe televisao de forma a receber o canal inicial em seu construtor.
# 4) [X] Adicione mais dois atributos canal_minimo (valor padrão 1) e canal_maximo (valor padrão 99) e modifique a classe Televisao de forma que, 
#       se pedirmos para mudar o canal para baixo, além do mínimo, ela vá para o canal máximo. 
#       Se mudarmos para cima, além do canal máximo, que volte ao canal mínimo.
# 5) [X] Modifique o construtor da classe Televisao de forma que canal_minimo e canal_maximo seja parametros opcionais valendo respectivamente 2 e 14.
# 6) [X] Crie duas instancias de Televisao, especificando o valor de canal_minimo e canal_maximo por nome.
class Televisao:
    def __init__(self, marca: str, tamanho: int, canal: int, canal_maximo: int = 14, canal_minimo: int = 2):
        self.__ligada = False
        self.__marca = marca
        self.__tamanho = tamanho
        self.__canal_maximo = canal_maximo
        self.__canal_minimo = self.__VerifyCanalMinimo(canal_minimo)
        self.__canal = self.__CheckValorCanal(canal)

    @property
    def ligada(self):
        return self.__ligada

    @property
    def canal(self):
        return self.__canal

    @property
    def marca(self):
        return self.__marca

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def canal_maximo(self):
        return self.__canal_maximo

    @property
    def canal_minimo(self):
        return self.__canal_minimo

    @canal.setter
    def canal(self, canal: int):
        self.__canal = self.__CheckValorCanal(canal)

    @ligada.setter
    def ligada(self,  ligada: bool):
        self.__ligada = ligada

    def __CheckValorCanal(self, canal: int):
        if canal < self.canal_minimo:
            return self.canal_maximo
        elif canal > self.canal_maximo:
            return self.canal_minimo
        else:
            return canal

    def __VerifyCanalMinimo(self, canal_minimo: int):
        if canal_minimo > self.canal_maximo:
            print('Erro: Canal minimo maior que canal maximo indicado!')
            return 1
        else:
            return canal_minimo

    def MudarCanalParaBaixo(self):
        self.canal = self.canal - 1
    
    def MudarCanalParaCima(self):
        self.canal = self.canal + 1

# 7) [X] Crie classes para representar estados e cidades. Cada estado tem um nome, sigla e cidades.
#       Cada cidade tem nome e população. Escreva um programa de testes que crie três estados com algumas cidades em cada um. 
#       Exiba a população de cada estado como a soma da população de suas cidades.
class Cidade:
    def __init__(self, nome: str, populacao: int):
        self.__nome = nome
        self.__populacao = populacao

    @property
    def nome(self):
        return self.__nome

    @property
    def populacao(self):
        return self.__populacao

class Estado:
    def __init__(self, nome: str, sigla: str, cidades):
        self.__nome = nome
        self.__sigla = sigla
        self.__cidades = cidades
        self.__populacao_total = self.__CountPopulacao()

    @property
    def nome(self):
        return self.__nome

    @property
    def sigla(self):
        return self.__sigla

    @property
    def cidades(self):
        return self.__cidades

    @property
    def populacao_total(self):
        return self.__populacao_total

    @populacao_total.setter
    def populacao_total(self,  populacao_total: int):
        self.populacao_total = populacao_total

    def __CountPopulacao(self):
        pop_total = 0
        for cidade in self.cidades:
            pop_total += cidade.populacao

        return pop_total

# 8) [X] Escreva uma classe Coordenada com atributos x e y, e métodos para mostrar as coordenadas,
#       calcular a distancia para outra coordenada, comparar coordenadas, mostrar no formato coordenada polar.
import math

class Coordenada:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    def CoordenadaFormatada(self):
        return f'({self.x}, {self.y})'

    def CalcDistancia(self, outra_coordenada):
        __ponto_x = math.pow((outra_coordenada.x - self.x), 2)
        __ponto_y = math.pow((outra_coordenada.y - self.y), 2)
        return math.sqrt(__ponto_x + __ponto_y)

    def CompCoordenadas(self, outraCoordenada):
        coordenada_inicial = Coordenada(0, 0)
        comp_coordenada = self.CalcDistancia(coordenada_inicial)
        comp_outra_coordenada = outraCoordenada.CalcDistancia(coordenada_inicial)

        if comp_coordenada > comp_outra_coordenada:
            return f'A coordenada ({self.x}, {self.y}) esta mais distante da origem que a coordenada ({outraCoordenada.x}, {outraCoordenada.y})'
        elif comp_coordenada < comp_outra_coordenada:
            return f'A coordenada ({outraCoordenada.x}, {outraCoordenada.y}) esta mais distante da origem que a coordenada ({self.x}, {self.y})'
        else:
            return f'Ambas coordenadas [({outraCoordenada.x}, {outraCoordenada.y}), ({self.x}, {self.y})] tem a mesma distancia da origem'

    def FormatarEmCoordenadasPolar(self):
        Xpow2 = math.pow(self.x, 2)
        Ypow2 = math.pow(self.y, 2)
        return f'P({math.sqrt(Xpow2+Ypow2)}, {math.atan(self.x/self.y)})'

# 9) [X] Escreva classes para as seguintes formas: quadrado, retângulo e círculo.
class Quadrado:
    def __init__(self, lado: float):
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

class Retangulo:
    def __init__(self, base: float, altura: float):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

class Circulo:
    def __init__(self, raio: float):
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio

# 10) [X] Escreva uma classe Fracao que armazena dois inteiros, numerador e denominador.
#  a) [X] Implemente metodos para somas, subtração, multiplicação e divisão de duas frações
#  b) [X] Implemente o método que imprime uma fração no formato numerador / denominador
#  c) [X] Implemente um método que inverte a fração
#  c) [X] Implemente um método que retorna a fração em valor real
#  d) [ ] Implemente um método que cria uma fração (numerador/denominador) a partir de um número real
def mmc(num1, num2): # Fonte: http://devfuria.com.br/logica-de-programacao/mmc/
    a = num1
    b = num2

    resto = None
    while resto != 0:
        resto = a % b
        a  = b
        b  = resto

    return (num1 * num2) / a

class Fracao:
    def __init__(self, numerador: int, denominador: int):
        self.__numerador = numerador
        self.__denominador = denominador

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    @numerador.setter
    def numerador(self, numerador):
        self.__numerador = numerador

    @denominador.setter
    def denominador(self, denominador):
        self.__denominador = denominador

    def ImprimeFuncao(self):
        return f'{self.numerador}/{self.denominador}'

    def __OperacaoComumSomaSubtracao(self, fracao, denominador_comum):
        return fracao.numerador * (denominador_comum/fracao.denominador)

    def InverteFração(self):
        [self.numerador, self.denominador] = [self.denominador, self.numerador]

    def Soma(self, fracao):
        denominador_comum = mmc(self.denominador, fracao.denominador)
        resultado_fracao_1 = self.__OperacaoComumSomaSubtracao(self, denominador_comum)
        resultado_fracao_2 = self.__OperacaoComumSomaSubtracao(self, denominador_comum)
        return f'{(resultado_fracao_1 + resultado_fracao_2)}/{denominador_comum}'

    def Subtracao(self, fracao):
        denominador_comum = mmc(self.denominador, fracao.denominador)
        resultado_fracao_1 = self.__OperacaoComumSomaSubtracao(self, denominador_comum)
        resultado_fracao_2 = self.__OperacaoComumSomaSubtracao(fracao, denominador_comum)
        return f'{(resultado_fracao_1 - resultado_fracao_2)}/{denominador_comum}'

    def Multiplicação(self, fracao):
        resultado_numerador = self.numerador * fracao.numerador
        resultado_denominador = self.denominador * fracao.denominador
        return f'{resultado_numerador}/{resultado_denominador}'

    def Divisao(self, fracao):
        fracao.InverteFração()
        resultado_numerador = self.numerador * fracao.numerador
        resultado_denominador = self.denominador * fracao.denominador
        return f'{resultado_numerador}/{resultado_denominador}'

    def FracaoParaNumeroReal(self):
        return self.numerador / self.denominador

    def NumeroRealParaFracao(self, numero_real):
        return f'{numero_real*5}/{5}'

def main():
    # Instancias de Televisão
    print('>> Instancias de Televisão')
    televisaoDaJulia= Televisao('Samsung', 55, 1, canal_minimo = 3, canal_maximo = 6)
    televisaoDaLeticia = Televisao('LG', 65, 99, canal_maximo = 4, canal_minimo = 5)
    print('[Televisao da Julia] marca:', televisaoDaJulia.marca, ' tamanho: ', televisaoDaJulia.tamanho, ' canal: ', televisaoDaJulia.canal)
    print('[Televisao da Julia] canal_minimo: ', televisaoDaJulia.canal_minimo, ' canal_maximo: ', televisaoDaJulia.canal_maximo)
    print('[Televisao da Leticia] marca:', televisaoDaLeticia.marca, ' tamanho: ', televisaoDaLeticia.tamanho, ' canal: ', televisaoDaLeticia.canal)
    print('[Televisao da Leticia] canal_minimo:', televisaoDaLeticia.canal_minimo, ' canal_maximo: ', televisaoDaLeticia.canal_maximo)
    televisaoDaJulia.MudarCanalParaBaixo()
    televisaoDaLeticia.MudarCanalParaCima()
    print('## Mudança de canal ##')
    print('[Televisao da Julia] marca:', televisaoDaJulia.marca, ' tamanho: ', televisaoDaJulia.tamanho, ' canal: ', televisaoDaJulia.canal)
    print('[Televisao da Leticia] marca:', televisaoDaLeticia.marca, ' tamanho: ', televisaoDaLeticia.tamanho, ' canal: ', televisaoDaLeticia.canal)    
    print('')

    # Instancias de Cidade e Estado
    print('>> Instancias de Cidade e Estado')
    uruguaiana = Cidade('Uruguaiana', 200)
    portoAlegre = Cidade('Porto Alegre', 5000)
    estado = Estado('Rio Grande do Sul', 'RS', [uruguaiana, portoAlegre])
    print('[', uruguaiana.nome, ']: populacao de ', uruguaiana.populacao)
    print('[', portoAlegre.nome, ']: populacao de ', portoAlegre.populacao)
    print('[', estado.nome, ']: populacao total de ', estado.populacao_total)
    print('')

    # Instancias de Coordenadas
    print('>> Instancias de Coordenadas')
    coordenadaA = Coordenada(2, 2)
    coordenadaB = Coordenada(3, 3)
    print('[Coordenada A]: ', coordenadaA.CoordenadaFormatada())
    print('[Coordenada B]: ', coordenadaB.CoordenadaFormatada())
    print('[Distancia coordA -> coordB]: ', coordenadaA.CalcDistancia(coordenadaB))
    print('[Distancia coordB -> coordA]: ', coordenadaB.CalcDistancia(coordenadaA))
    print('[Comparacao da distancia das coordenadas até a origem]: ', coordenadaA.CompCoordenadas(coordenadaB))
    print('[coordA -> Polar]', coordenadaA.FormatarEmCoordenadasPolar())
    print('[coordB -> Polar]', coordenadaB.FormatarEmCoordenadasPolar())    
    print('')

    # Instancias de Fracoes
    print('>> Instancias de Fracoes')
    fracaoA = Fracao(4, 12)
    fracaoB = Fracao(8, 3)
    print('[Imprime fracao A]: ', fracaoA.ImprimeFuncao())
    print('[Imprime fracao B]: ', fracaoB.ImprimeFuncao())
    print('[Soma das fracoes A+B]: ', fracaoA.Soma(fracaoB))
    print('[Subtracao das fracoes A-B]: ', fracaoA.Subtracao(fracaoB))
    print('[Multiplicacao das fracoes A*B]: ', fracaoA.Multiplicação(fracaoB))
    print('[Divisao das fracoes A/B]: ', fracaoA.Divisao(fracaoB))
    fracaoA.InverteFração()
    print('[Imprime fracao A]: ', fracaoA.ImprimeFuncao())
    print('[Numero real da fracao A]: ', fracaoA.FracaoParaNumeroReal())
    print('[Numero real 10 em fração]: ', fracaoA.NumeroRealParaFracao(10))
    print('')
    

main()