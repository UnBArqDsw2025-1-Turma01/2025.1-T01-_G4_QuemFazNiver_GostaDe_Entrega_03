from abc import ABC, abstractmethod
from typing import List

# Abstract Product
class Fornecedor(ABC):
    def __init__(self, nome: str, tags: List[str], contato: str, portfolio: str = None):
        self.nome = nome
        self.tags = tags
        self.contato = contato
        self.portfolio = portfolio
    
    @abstractmethod
    def exibir_info(self) -> str:
        pass
    
    @abstractmethod
    def calcular_preco(self) -> float:
        pass
    
    @abstractmethod
    def listar_servicos(self) -> List[str]:
        pass

# Abstract Factory
class FornecedorFactory(ABC):
    @abstractmethod
    def create_fornecedor(self, nome: str, tags: List[str], contato: str, portfolio: str = None) -> Fornecedor:
        pass
