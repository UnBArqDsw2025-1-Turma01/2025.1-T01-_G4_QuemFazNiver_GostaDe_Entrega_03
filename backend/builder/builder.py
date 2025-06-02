from abc import ABC, abstractmethod
from typing import List
from datetime import date, time

# Produto
class Festa:
    def __init__(self):
        self.nomeAniversariante = ""
        self.local = ""
        self.buffet = []
        self.estilosMusicais = []
        self.data = None
        self.hora = None
        self.linkGrupo = ""

# Interface Builder
class FestaBuilder(ABC):
    @abstractmethod
    def setNomeAniversariante(self, nomeAniversariante: str):
        pass

    @abstractmethod
    def setLocal(self, local: str):
        pass

    @abstractmethod
    def setbuffet(self, buffet: List[str]):
        pass

    @abstractmethod
    def setEstilosMusicais(self, estilosMusicais: List[str]):
        pass

    @abstractmethod
    def setData(self, data: date):
        pass

    @abstractmethod
    def setHora(self, hora: time):
        pass

    @abstractmethod
    def setLinkGrupo(self, linkGrupo: str):
        pass

    @abstractmethod
    def getFesta(self) -> Festa:
        pass

# Implementação do Builder
class FestaPersonalizadaBuilder(FestaBuilder):
    def __init__(self):
        self.festa = Festa()

    def setNomeAniversariante(self, nomeAniversariante: str):
        self.festa.nomeAniversariante = nomeAniversariante

    def setLocal(self, local: str):
        self.festa.local = local

    def setbuffet(self, buffet: List[str]):
        self.festa.buffet = buffet

    def setEstilosMusicais(self, estilosMusicais: List[str]):
        self.festa.estilosMusicais = estilosMusicais

    def setData(self, data: date):
        self.festa.data = data

    def setHora(self, hora: time):
        self.festa.hora = hora

    def setLinkGrupo(self, linkGrupo: str):
        self.festa.linkGrupo = linkGrupo

    def getFesta(self) -> Festa:
        return self.festa

# Director
class Organizador:
    def __init__(self, builder: FestaBuilder):
        self.builder = builder

    def construirFesta(self, nomeAniversariante: str, local: str, buffet: List[str], estilosMusicais: List[str], data: date, hora: time, linkGrupo: str) -> Festa:
        self.builder.setNomeAniversariante(nomeAniversariante)
        self.builder.setLocal(local)
        self.builder.setbuffet(buffet)
        self.builder.setEstilosMusicais(estilosMusicais)
        self.builder.setData(data)
        self.builder.setHora(hora)
        self.builder.setLinkGrupo(linkGrupo)
        return self.builder.getFesta()