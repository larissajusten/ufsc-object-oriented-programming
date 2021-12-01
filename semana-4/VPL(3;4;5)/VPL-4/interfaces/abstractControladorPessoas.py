from abc import ABC, abstractmethod, abstractproperty
from cliente import Cliente
from tecnico import Tecnico

class AbstractControladorPessoas(ABC):
	# @return retorna a lista de clientes
	@abstractproperty
	@property
	def clientes(self) -> list:
		pass

	# @return retorna a lista de tecnicos
	@abstractproperty
	@property
	def tecnicos(self) -> list:
		pass

	# Permite a inclusao de um novo cliente na lista de clientes
	# @param codigo codigo do Cliente
	# @param nome nome do Cliente
	# @return retorna o cliente inserido como um IPessoa
	@abstractmethod
	def incluiCliente(self, codigo :int, nome :str) -> Cliente:
		pass

	# Permite a inclusao de um novo tecnico na lista de tecnicos
	# @param codigo codigo do tecnico
	# @param nome nome do tecnico
	# @return retorna o tecnico inserido como um IPessoa
	@abstractmethod
	def incluiTecnico(self, codigo :int, nome :str) -> Tecnico:
		pass
