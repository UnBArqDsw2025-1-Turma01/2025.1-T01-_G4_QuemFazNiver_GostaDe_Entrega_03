from .builder_interface import FestaBuilder
from .plano_de_festa import PlanoDeFesta
from .festa_organizada import FestaOrganizada

class FestaPersonalizadaBuilder(FestaBuilder):
    def __init__(self, plano: PlanoDeFesta):
        self.plano = plano
        self.festa = FestaOrganizada(
            nomeAniversariante=plano.nomeAniversariante,
            data=plano.data,
            horario=plano.horario,
            localFornecedor="",
            buffet=[],
            banda=""
        )

    def escolherLocalFornecedor(self):
        self.festa.localFornecedor = self.plano.localFornecedor

    def selecionarBuffet(self):
        self.festa.buffet = self.plano.buffetEscolhidas

    def contratarBanda(self):
        self.festa.banda = self.plano.bandaEscolhida

    def gerarConvite(self):
        nome = self.plano.nomeAniversariante
        self.festa.linkWhatsapp = f"https://wa.me/?text=Convite%20para%20a%20festa%20de%20{nome}"
        self.festa.convite = f"Convite da festa de {nome}"

    def getFesta(self) -> FestaOrganizada:
        return self.festa
