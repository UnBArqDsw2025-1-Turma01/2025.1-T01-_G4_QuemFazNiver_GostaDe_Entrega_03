from portifolio_template import Portifolio

class PortifolioFotografia(Portifolio):
    def __init__(self, titulo, descricao, valores, funcionamento, estilo_fotografia, amostras_fotos):
        super().__init__(titulo, descricao, valores, funcionamento)
        self.estilo_fotografia = estilo_fotografia
        self.amostras_fotos = amostras_fotos

    def criar_descricao_geral(self) -> str:
        fotos = ", ".join(self.amostras_fotos) if self.amostras_fotos else "nenhuma amostra disponível"
        return (
            f"Estilo de fotografia: {self.estilo_fotografia}. "
            f"Amostras: {fotos}. "
            f"{self.descricao}"
        )
































