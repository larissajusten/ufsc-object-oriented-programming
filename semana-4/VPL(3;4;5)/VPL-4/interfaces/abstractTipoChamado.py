from abc import ABC, abstractmethod

class AbstractTipoChamado(ABC):

	@property
	@abstractmethod
	def codigo(self) -> int:
		pass

	@property
	@abstractmethod
	def descricao(self) -> str:
		pass

	@property
	@abstractmethod
	def nome(self) -> str:
		pass