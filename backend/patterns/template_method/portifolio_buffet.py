from .portifolio_template import Portifolio  

class PortifolioBuffet(Portifolio):
    def __init__(self, titulo, descricao, valores, funcionamento, tipo_evento, cardapio_pratos):
        super().__init__(titulo, descricao, valores, funcionamento)
        self.tipo_evento = tipo_evento
        self.cardapio_pratos = cardapio_pratos

    def criar_descricao_geral(self) -> str:
        pratos = ", ".join(self.cardapio_pratos) if self.cardapio_pratos else "não informado"
        return (
            f"Buffet para eventos como: {self.tipo_evento}. "
            f"Cardápio com pratos como: {pratos}. "
            f"{self.descricao}"
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        