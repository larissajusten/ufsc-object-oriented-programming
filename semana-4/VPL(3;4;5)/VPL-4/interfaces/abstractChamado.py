from abc import ABC, abstractmethod
from cliente import Cliente
from tecnico import Tecnico
from tipoChamado import TipoChamado
from datetime import date as Date


class AbstractChamado(ABC):
	@property
	@abstractmethod
	def cliente(self) -> Cliente:
		pass

	@property
	@abstractmethod
	def data(self) -> Date:
		pass

	@property
	@abstractmethod
	def descricao(self) -> str:
		pass

	@property
	@abstractmethod
	def prioridade(self) -> int:
		pass

	@property
	@abstractmethod
	def tecnico(self) -> Tecnico:
		pass

	@property
	@abstractmethod
	def tipo(self) -> TipoChamado:
		pass

	@property
	@abstractmethod
	def titulo(self) -> str:
		pass