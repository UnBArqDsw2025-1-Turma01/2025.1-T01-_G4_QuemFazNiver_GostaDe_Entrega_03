from abc import ABC, abstractmethod
from .builder import Festa

# Implementor
class TipoConvite(ABC):
    @abstractmethod
    def gerarMensagem(self, festa: Festa) -> str:
        pass

# Concrete Implementor 1 - Convite da Festa
class TipoConviteFesta(TipoConvite):
    def gerarMensagem(self, festa: Festa) -> str:
        return f"""
        ================================
               CONVITE PARA A FESTA
        ================================
        🎉 Nome do Aniversariante: {festa.nomeAniversariante}
        📍 Local: {festa.local}
        📅 Data: {festa.data.strftime('%d/%m/%Y')}
        ⏰ Hora: {festa.hora.strftime('%H:%M')}
        🔗 Link do Grupo: {festa.linkGrupo if festa.linkGrupo else 'Não informado'}
        ================================
        """

# Concrete Implementor 2 - Lista de Preferências
class TipoListaPreferencias(TipoConvite):
    def gerarMensagem(self, festa: Festa) -> str:
        return f"""
        ================================
           PREFERÊNCIAS DA FESTA
        ================================
        🍴 Buffet: {', '.join(festa.buffet)}
        🎵 Estilos Musicais: {', '.join(festa.estilosMusicais)}
        ================================
        """

# Abstraction
class Convite(ABC):
    def __init__(self, festa: Festa, tipo: TipoConvite):
        self.festa = festa
        self.tipo = tipo

    @abstractmethod
    def gerarConvite(self) -> str:
        pass

# Refined Abstraction - Convite da Festa
class ConviteFesta(Convite):
    def gerarConvite(self) -> str:
        return self.tipo.gerarMensagem(self.festa)

# Refined Abstraction - Lista de Preferências
class ListaPreferencias(Convite):
    def gerarConvite(self) -> str:
        return self.tipo.gerarMensagem(self.festa)
