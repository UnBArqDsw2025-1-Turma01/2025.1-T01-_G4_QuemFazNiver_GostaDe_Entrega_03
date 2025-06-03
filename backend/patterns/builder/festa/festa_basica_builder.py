from .builder_interface import FestaBuilder
from .festa_organizada import FestaOrganizada
from datetime import date

class FestaBasicaBuilder(FestaBuilder):
    """
    Builder para festas básicas com configurações padrão.
    Demonstra como diferentes builders podem criar produtos diferentes.
    """
    
    def __init__(self, nome_aniversariante: str, data_festa: date):
        self.festa = FestaOrganizada(
            nomeAniversariante=nome_aniversariante,
            data=data_festa,
            horario="",
            localFornecedor="",
            buffet=[],
            banda=""
        )

    def escolherLocalFornecedor(self):
        """Configuração padrão para festa básica"""
        self.festa.localFornecedor = "Casa do Aniversariante"

    def selecionarBuffet(self):
        """Buffet simples padrão"""
        self.festa.buffet = ["Bolo", "Salgadinhos", "Refrigerante", "Docinhos"]

    def contratarBanda(self):
        """Música ambiente padrão"""
        self.festa.banda = "Playlist Spotify"

    def gerarConvite(self):
        """Convite simples"""
        nome = self.festa.nomeAniversariante
        self.festa.horario = "15:00"  # Horário padrão para festa básica
        self.festa.linkWhatsapp = f"https://wa.me/?text=Venha%20para%20a%20festa%20de%20{nome}!"
        self.festa.convite = f"Você está convidado para a festa de aniversário de {nome}!"

    def getFesta(self) -> FestaOrganizada:
        return self.festa
