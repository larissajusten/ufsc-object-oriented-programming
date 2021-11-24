

class Animal(ABC):
	def __init__(self, tamanhoPasso: int):
		...

	
	"""Insira aqui os outros metodos"""
	
	@abstractmethod
	def produzirSom(self):
		pass