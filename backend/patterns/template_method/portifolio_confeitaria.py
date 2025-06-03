from .portifolio_template import Portifolio 

class PortifolioConfeitaria(Portifolio):
    def __init__(self, titulo, descricao, valores, funcionamento, tipo_doce, cardapio_doces, cardapio_restricoes):
        super().__init__(titulo, descricao, valores, funcionamento)
        self.tipo_doce = tipo_doce
        self.cardapio_doces = cardapio_doces
        self.cardapio_restricoes = cardapio_restricoes

    def criar_descricao_geral(self) -> str:
        tipos = ", ".join(self.tipo_doce) if self.tipo_doce else "não especificado"
        doces = ", ".join(self.cardapio_doces) if self.cardapio_doces else "nenhum"
        restritos = ", ".join(self.cardapio_restricoes) if self.cardapio_restricoes else "nenhum"
        return (
            f"Doces oferecidos: {doces}. "
            f"Tipos: {tipos}. "
            f"Opções para restrições: {restritos}. "
            f"{self.descricao}"
        )


























