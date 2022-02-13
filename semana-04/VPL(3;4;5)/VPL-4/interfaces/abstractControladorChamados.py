from abc import ABC, abstractmethod
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico

class AbstractControladorChamados(ABC):
	# Retorna o total de chamados registrados para o TipoChamado recebido como parametro
	# @param tipo TipoChamado
	# @return int com a quantidade total dos chamados daquele tipo
	@abstractmethod
	def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
		pass

	# Permite incluir um novo chamado na lista de Chamados. O chamado incluido eh retornado como um IChamado
	# @param data data do chamado em formato Date
	# @param cliente referencia para o Cliente do chamado
	# @param tecnico referencia para o Tecnico do chamado
	# @param titulo titulo do chamado
	# @param descricao descricao do chamado
	# @param prioridade prioridade do chamado
	# @param tipo tipo do chamado (TipoChamado)
	# @return retorna o chamato cadastrado
	@abstractmethod
	def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
			pass

	# Permite incluir um novo TipoChamado na lista de TiposChamado. O TipoChamado incluido eh retornado como um ITipoChamado
	# @param codigo codigo do Tipo Chamado
	# @param nome nome do Tipo Chamado
	# @param descricao descricao do Tipo Chamado
	# @return retorna o Tipo Chamado cadastrado
	@abstractmethod
	def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
		pass
	
	@property	
	@abstractmethod
	def tipoChamados(self):
	    pass