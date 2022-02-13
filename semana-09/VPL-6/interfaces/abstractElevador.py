from abc import ABC, abstractmethod

class AbstractElevador(ABC):
    @abstractmethod
    def __init__(self):
        pass

    # ElevadorJahNoTerreoException
    @abstractmethod
    def descer(self) -> str:
    	pass
    
    # ElevadorCheioException
    @abstractmethod
    def entraPessoa(self) -> str:
    	pass
    
    # ElevadorJahVazioException
    @abstractmethod
    def saiPessoa(self) -> str:
    	pass
    
    # ElevadorJahNoUltimoAndarException
    @abstractmethod
    def subir(self) -> str:
    	pass
    
    @property
    @abstractmethod
    def capacidade(self) -> int:
    	pass
    
    @property
    @abstractmethod
    def totalPessoas(self) -> int:
    	pass
    
    @property
    @abstractmethod
    def totalAndaresPredio(self) -> int:
    	pass
    
    @property
    @abstractmethod
    def andarAtual(self) -> int:
    	pass
    
    @totalAndaresPredio.setter
    @abstractmethod
    def totalAndaresPredio(self, totalAndaresPredio: int):
    	pass

