from abc import ABC, abstractmethod
from elevador import Elevador


class AbstractControladorElevador(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    '''
    Faz o elevador subir um andar. Se jah estiver no ultimo andar, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador 
    @throws ElevadorJahNoUltimoAndarException 
    '''
    @abstractmethod
    def subir(self) -> str:
        pass
    
    '''
    Faz o elevador descer um andar. Se jah estiver no terreo, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoTerreoException
    '''
    @abstractmethod
    def descer(self) -> str:
        pass

    '''
    Entra uma pessoa no Elevador. Se nao for possivel permitir a entrada da pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorCheioException
    '''
    @abstractmethod
    def entraPessoa(self) -> str:
        pass
	
    '''
    Sai uma pessoa no Elevador. Se nao for possivel permitir a saida de uma pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahVazioException
    '''
    @abstractmethod
    def saiPessoa() -> str:
        pass
	
    '''
    @return Elevador
    '''
    @property
    @abstractmethod
    def elevador(self) -> Elevador:
    	pass

    '''
    @param andarAtual andar atual do elevador
    @param totalAndaresPredio total de andares do predio
    @param capacidade capacidade maxima do elevador
    @param totalPessoas total de pessoas atual do elevador
    '''
    @abstractmethod
    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        pass
