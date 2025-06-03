from typing import List
from .interfaces import Fornecedor

class Pizzaria(Fornecedor):
    def exibir_info(self) -> str:
        return f"Pizzaria: {self.nome} - Contato: {self.contato}"
    
    def calcular_preco(self) -> float:
        # Lógica específica para cálculo de preço de pizzaria
        return 150.0 * len(self.tags)
    
    def listar_servicos(self) -> List[str]:
        return ["Pizza tradicional", "Pizza gourmet", "Esfihas", "Calzones"]

class Confeitaria(Fornecedor):
    def exibir_info(self) -> str:
        return f"Confeitaria: {self.nome} - Contato: {self.contato}"
    
    def calcular_preco(self) -> float:
        # Lógica específica para cálculo de preço de confeitaria
        return 200.0 * len(self.tags)
    
    def listar_servicos(self) -> List[str]:
        return ["Bolos", "Doces", "Salgados", "Coffee break"]

class Churrascaria(Fornecedor):
    def exibir_info(self) -> str:
        return f"Churrascaria: {self.nome} - Contato: {self.contato}"
    
    def calcular_preco(self) -> float:
        # Lógica específica para cálculo de preço de churrascaria
        return 300.0 * len(self.tags)
    
    def listar_servicos(self) -> List[str]:
        return ["Churrasco completo", "Espetos", "Buffet de carnes", "Acompanhamentos"]
