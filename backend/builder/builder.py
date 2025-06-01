from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date

class PlanoDeFesta:
    def __init__(
        self,
        buffetEscolhidas: List[str],
        bandaEscolhida: str,
        nomeAniversariante: str,
        data: date,
        horario: str,
        localFornecedor: str
    ):
        self.buffetEscolhidas = buffetEscolhidas
        self.bandaEscolhida = bandaEscolhida
        self.nomeAniversariante = nomeAniversariante
        self.data = data
        self.horario = horario
        self.localFornecedor = localFornecedor

class FestaOrganizada:
    def __init__(
        self,
        nomeAniversariante: str,
        data: date,
        horario: str,
        localFornecedor: str,
        buffet: List[str],
        banda: str,
        linkWhatsapp: Optional[str] = None,
        convite: Optional[str] = None
    ):
        self.nomeAniversariante = nomeAniversariante
        self.data = data
        self.horario = horario
        self.localFornecedor = localFornecedor
        self.buffet = buffet
        self.banda = banda
        self.linkWhatsapp = linkWhatsapp
        self.convite = convite

class FestaBuilder(ABC):
    @abstractmethod
    def escolherLocalFornecedor(self): pass

    @abstractmethod
    def selecionarBuffet(self): pass

    @abstractmethod
    def contratarBanda(self): pass

    @abstractmethod
    def gerarConvite(self): pass

    @abstractmethod
    def getFesta(self) -> FestaOrganizada: pass

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
        self.festa.linkWhatsapp = f"https://wa.me/?text=Convite%20para%20a%20festa%20de%20{self.plano.nomeAniversariante}"
        self.festa.convite = f"Convite da festa de {self.plano.nomeAniversariante}"

    def getFesta(self) -> FestaOrganizada:
        return self.festa

class OrganizadorDeFesta:
    def construirFesta(self, builder: FestaBuilder) -> FestaOrganizada:
        builder.escolherLocalFornecedor()
        builder.selecionarBuffet()
        builder.contratarBanda()
        builder.gerarConvite()
        return builder.getFesta()