"""
    Implemente uma classe que, implementa algumas séries matemáticas importantes: Fibonacci,
    Fatorial, Fibonarial, Primo. Use recursão para Fibonacci e Fatorial.
"""

class Series:
    def __init__(self):
        pass

    def Fibonacci(self, n):
        # http://oeis.org/A000045
        # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, [...]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    def SeqDeFibonacci(self, n):
        if n == 0:
            return []
        elif n == 1:
            return [0,1]
        else:
            return self.SeqDeFibonacci(n-1) + [self.Fibonacci(n)]

    def Tribonacci(self, n):
        # http://oeis.org/A000073
        # 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, [...]
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.Tribonacci(n-1) + self.Tribonacci(n-2) + self.Tribonacci(n-3)

    def SeqDeTribonacci(self, n):
        if n == 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0,0,1]
        else:
            return self.SeqDeTribonacci(n-1) + [self.Tribonacci(n)]

    def Fibonorial(self, n):
        # http://oeis.org/A003266
        # 1, 1, 1, 2, 6, 30, 240, 3120, 65520, 2227680, 122522400, 10904493600, 1570247078400, [...]
        if n == 0:
            return 1
        else:
            return self.Fibonacci(n) * self.Fibonorial(n-1)

    def SeqDeFibonorial(self, n):
        l = []
        if n == 0:
            return []
        elif n == 1:
            return [1]

        l = [1]
        for i in range(1, n+1):
            l.append(self.Fibonorial(i))
        return l

    def Fatorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.Fatorial(n-1)

    def SeqDePrimos(self, n):
        # http://oeis.org/A000040
        # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, [...]
        l = []

        if n == 0:
            return []
        elif n == 1:
            return [2]

        l = [2]
        i = 3
        while len(l) < n:
            l.append(i) if self.IsPrimo(i) else None
            i += 2
        return l

    def IsPrimo(self, n):
        if n == 0:
            return False
        elif n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

def main():
    print('# Exercicio 4 - Series')

    series = Series()
    print('\n# Fibonacci')
    print(f'F_{10} = {series.Fibonacci(10)}')
    print(f'Sequência Fibonacci até n={10}: {series.SeqDeFibonacci(10)}')

    print('\n# Tribonacci')
    print(f'F_{10} = {series.Tribonacci(10)}')
    print(f'Sequência Tribonacci até n={10}: {series.SeqDeTribonacci(10)}')

    print('\n# Fibonorial')
    print(f'F_{10}! = {series.Fibonorial(10)}')
    print(f'Sequência Fibonorial até n={10}: {series.SeqDeFibonorial(10)}')

    print('\n# Fatorial')
    print(f'{10}! = {series.Fatorial(10)}')

    print('\n# Primo')
    print(f'Sequência Primo até {12}º termo: {series.SeqDePrimos(12)}')

if __name__ == '__main__':
    main()
