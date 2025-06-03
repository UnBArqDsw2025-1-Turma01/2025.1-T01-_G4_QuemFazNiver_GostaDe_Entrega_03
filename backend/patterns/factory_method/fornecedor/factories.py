from typing import List
from .interfaces import FornecedorFactory, Fornecedor
from .products import Pizzaria, Confeitaria, Churrascaria

class PizzariaFornecedorFactory(FornecedorFactory):
    def create_fornecedor(self, nome: str, tags: List[str], contato: str, portfolio: str = None) -> Fornecedor:
        return Pizzaria(nome, tags, contato, portfolio)

class ConfeitariaFornecedorFactory(FornecedorFactory):
    def create_fornecedor(self, nome: str, tags: List[str], contato: str, portfolio: str = None) -> Fornecedor:
        return Confeitaria(nome, tags, contato, portfolio)

class ChurrascariaFornecedorFactory(FornecedorFactory):
    def create_fornecedor(self, nome: str, tags: List[str], contato: str, portfolio: str = None) -> Fornecedor:
        return Churrascaria(nome, tags, contato, portfolio)
