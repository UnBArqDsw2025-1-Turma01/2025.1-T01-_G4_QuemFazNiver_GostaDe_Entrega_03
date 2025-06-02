from abc import ABC, abstractmethod
from .festa_organizada import FestaOrganizada

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
