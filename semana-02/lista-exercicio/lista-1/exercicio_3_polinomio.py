"""
    Crie uma classe que modela um polinômio do tipo c0 + c1*x + c2*x^2 + … + cN*x^N .
    Os usuários serão estudantes de engenharia e ciências da computação que querem resolver exercícios de álgebra. 
    A entrada são os N coeficientes em ordem crescente de potência. 
    Os usuários precisarão acessar o grau do polinômio, avaliar o resultado para dado valor de x,
        somar e multiplicar dois polinômios.
--- Desafio: Implemente um método que plota o polinômio para um dado intervalo de entrada.
"""
import numpy as np
import matplotlib.pyplot as plt

class Polinomio:
    def __init__(self, array_coeficientes):
        self.__array_coeficientes = array_coeficientes

    @property
    def array_coeficientes(self):
        return self.__array_coeficientes

    @array_coeficientes.setter
    def array_coeficientes(self, new_array_coeficientes):
        self.__array_coeficientes = new_array_coeficientes
        
    def __CheckListaVazia(self):
        if all(self.array_coeficientes) == 0 or not self.array_coeficientes:
            print('Polinomio de grau nulo!')
            return True

    def VizualizarPolinomio(self):
        # c0 + c1*x + c2*x^2 + … + cN*x^N
        string_polinomio = ''
        for i, coeficiente in enumerate(self.array_coeficientes):
            if i == 0:
                string_polinomio += f'{coeficiente}'
            elif coeficiente == 0:
                continue
            else:
                if coeficiente > 0:
                    string_polinomio += f' + {coeficiente}'
                else:
                    string_polinomio += f' - {abs(coeficiente)}'
                if i == 1:
                    string_polinomio += 'x'
                else:
                    string_polinomio += f'x^{i}'
        return f'[{string_polinomio}]'

    def RetornaGrau(self):
        print('# Grau: ', end='')
        if self.__CheckListaVazia():
            return

        print(len(self.array_coeficientes) - 1)
        return len(self.array_coeficientes)-1

    def ResultadoPolinomio(self, x):
        print(f'# Resultado: ', end='')
        if self.__CheckListaVazia():
            return

        resultado = 0
        for i, coeficiente in enumerate(self.array_coeficientes):
            resultado += coeficiente*(x**i)
    
        print(f'P(x) = {self.VizualizarPolinomio()} -> P({x}) = {resultado}')
        return resultado

    def SomarPolinomio(self, polinomio):
        diferenca_tamanho = len(self.array_coeficientes) - len(polinomio.array_coeficientes)
        if diferenca_tamanho > 0:
            for i in range(diferenca_tamanho):
                polinomio.array_coeficientes.append(0)
        elif diferenca_tamanho < 0:
            for i in range(diferenca_tamanho*-1):
                self.array_coeficientes.append(0)

        print(f'# Soma: {self.VizualizarPolinomio()} + {polinomio.VizualizarPolinomio()}', end='')
        self.array_coeficientes = [x + y for x, y in zip(self.array_coeficientes, polinomio.array_coeficientes)]
        print(f' = {self.VizualizarPolinomio()}')

    def MultiplicarPolinomio(self, polinomio):
        # (c0 + c1*x) * (c0 + c1*x) = c0^2 + 2*c0*c1*x + c1^2*x^2
        # (1 + 2x^1) * (1 + 2x^1) = 1 * 1 + 1 * 2 x^1 + 2x^1 * 1 + 2x^1 * 2x^1 = 1 + 4x^1 + 4x^2
        p1 = self.array_coeficientes[::-1]
        p2 = polinomio.array_coeficientes[::-1]

        print(f'# Multiplicação: {self.VizualizarPolinomio()} * {polinomio.VizualizarPolinomio()}', end='')
        self.array_coeficientes = list(np.polynomial.polynomial.polymul(p1, p2))[::-1]
        print(f' = {self.VizualizarPolinomio()}')
    
    def Plot(self, x_range, img_name = "polinomio"):
        x = np.linspace(x_range[0], x_range[1], 100)
        y = np.polyval(self.array_coeficientes[::-1], x)
        plt.plot(x, y)
        plt.savefig(f"{img_name}.png")

def PreCriacaoDeClientes():
    return Polinomio([1000,231,2,1])

def CriarPolinomio():
    print('# Digite o coeficiente a seguir e aperte [ENTER] para digitar o proximo coeficiente')
    print('# Para sair digite [Z]')

    coeficientes = []
    coeficiente = ''
    while coeficiente != 'z':
        coeficiente = input(f'Coeficiente: ')
        if coeficiente != 'z' and coeficiente.isnumeric():
            coeficientes.append(float(coeficiente))

    if coeficientes:
        return Polinomio(coeficientes)
    else:
        return Polinomio([0])

def Menu(polinomio):
    print('')
    print('# MENU')
    opcao_escolhida = 0

    while True:
        print('')
        print('[1]: Visualizar polinomio')
        print('[2]: Somar polinomio')
        print('[3]: Multiplicar polinomio')
        print('[4]: Resultado do polinomio')
        print('[5]: Plotar polinomio')
        print('[z]: Sair')

        opcao_escolhida = input('> Escolha uma opcao: ')

        if opcao_escolhida.lower() == 'z':
            exit()

        if opcao_escolhida == '1':
            print('')
            print(f'Polinomio: {polinomio.VizualizarPolinomio()}')
        elif opcao_escolhida == '2':
            print('')
            novo_polinomio = CriarPolinomio()
            polinomio.SomarPolinomio(novo_polinomio)
        elif opcao_escolhida == '3':
            print('')
            novo_polinomio = CriarPolinomio()
            polinomio.MultiplicarPolinomio(novo_polinomio)
        elif opcao_escolhida == '4':
            print('')
            x = float(input('> Digite o valor de x: (inteiro/decimal) '))
            polinomio.ResultadoPolinomio(x)
        elif opcao_escolhida == '5':
            print('')
            intervalo_inicial = float(input('> Digite o primeiro valor do intervalo: (inteiro/decimal) '))
            intervalo_final = float(input('> Digite o ultimo valor do intervalo: (inteiro/decimal) '))
            nome_imagem = input('> Digite o nome da imagem plotada: ')
            polinomio.Plot([intervalo_inicial, intervalo_final], nome_imagem)      
        else:
            print('# Opcao invalida!')

def main():
    while True:
        verify = ''
        while verify != 's' and verify != 'n' and verify != 'z':
            verify = input('> Voce deseja usar um polinomio ja existente: [S/N/Z] ').lower()
        
        if verify == 's':
            Menu(PreCriacaoDeClientes())
        elif verify == 'z':
            exit()
        else:
            Menu(CriarPolinomio())
            break

if __name__ == '__main__':
    main()
