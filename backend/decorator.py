from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from models import Usuario

class Convite(ABC):
    """Classe abstrata para representar um Convite."""
    
    def __init__(self, destinatario: List[Usuario], remetente: Usuario, titulo: str, template=None, mensagem: str = "", dataEnvio: datetime = None):
        self.destinatario = destinatario
        self.remetente = remetente
        self.titulo = titulo
        self.template = template
        self.mensagem = mensagem
        self.dataEnvio = dataEnvio or datetime.now()
        self._status = "PENDENTE"
    
    @abstractmethod
    def criar_convite(self) -> dict:
        """Método abstrato para criar um convite."""
        pass
    
    def get_status(self) -> str:
        """Retorna o status do convite."""
        return self._status
    
    def set_status(self, status: str) -> None:
        """Define o status do convite."""
        self._status = status


class TemplateDefault:
    """Implementação concreta de um template padrão para convites."""
    
    def __init__(self):
        self.paletaCores = ["#FFFFFF", "#000000", "#FF5733"]
        self.tema = "Padrão"
    
    def criar_convite(self) -> dict:
        """Cria um convite com template padrão."""
        return {
            "tipo": "template_default",
            "paletaCores": self.paletaCores,
            "tema": self.tema
        }


class ConviteConcreto(Convite):
    """Implementação concreta da classe Convite."""
    
    def criar_convite(self) -> dict:
        """Cria um convite básico."""
        template_info = {}
        if self.template:
            template_info = self.template.criar_convite()
            
        return {
            "destinatario": [dest.id for dest in self.destinatario],
            "remetente": self.remetente.id,
            "titulo": self.titulo,
            "mensagem": self.mensagem,
            "dataEnvio": self.dataEnvio.isoformat(),
            "status": self.get_status(),
            "template": template_info
        }


class DecoratorConvite(Convite):
    """Classe base para decoradores de convites."""
    
    def __init__(self, convite: Convite):
        self._convite = convite
        super().__init__(
            destinatario=convite.destinatario,
            remetente=convite.remetente,
            titulo=convite.titulo,
            template=convite.template,
            mensagem=convite.mensagem,
            dataEnvio=convite.dataEnvio
        )
    
    def decorar_convite(self) -> dict:
        """Método para aplicar decoração ao convite."""
        return self._convite.criar_convite()
    
    def criar_convite(self) -> dict:
        """Implementação do método abstrato que delega para o convite interno."""
        return self.decorar_convite()


class DecoratorInterativo(DecoratorConvite):
    """Decorador que adiciona elementos interativos ao convite."""
    
    def __init__(self, convite: Convite):
        super().__init__(convite)
        self.googleMaps = None
        self.carousel = []
        self.comentarios = []
    
    def configurar_mapa(self, latitude: float, longitude: float, zoom: int = 15) -> None:
        """Configura o mapa para o convite."""
        self.googleMaps = {
            "latitude": latitude, 
            "longitude": longitude, 
            "zoom": zoom
        }
    
    def adicionar_imagem_carousel(self, image_url: str) -> None:
        """Adiciona uma imagem ao carrossel."""
        self.carousel.append({"tipo": "imagem", "url": image_url})
    
    def adicionar_comentario(self, comentario: str) -> None:
        """Adiciona um comentário ao convite."""
        self.comentarios.append(comentario)
    
    def decorar_convite(self) -> dict:
        """Aplica decoração de interatividade ao convite."""
        convite_base = super().decorar_convite()
        
        # Adiciona elementos interativos
        interativo = {}
        if self.googleMaps:
            interativo["googleMaps"] = self.googleMaps
        
        if self.carousel:
            interativo["carousel"] = self.carousel
            
        if self.comentarios:
            interativo["comentarios"] = self.comentarios
        
        if interativo:
            convite_base["interativo"] = interativo
        
        return convite_base
    
    def confirmar_convite(self) -> None:
        """Método para confirmar a presença no convite."""
        self.set_status("CONFIRMADO")


class DecoratorLuxo(DecoratorConvite):
    """Decorador que adiciona elementos de luxo ao convite."""
    
    def __init__(self, convite: Convite):
        super().__init__(convite)
        self.carousel = []
        self.videos = []
        self.sons = None
        self.tipografia = "Arial"
    
    def adicionar_video(self, video_url: str) -> None:
        """Adiciona um vídeo ao convite."""
        self.videos.append(video_url)
    
    def configurar_som(self, som_url: str, autoplay: bool = False) -> None:
        """Configura som de fundo para o convite."""
        self.sons = {
            "url": som_url,
            "autoplay": autoplay
        }
    
    def configurar_tipografia(self, fonte: str) -> None:
        """Configura a tipografia do convite."""
        self.tipografia = fonte
    
    def adicionar_imagem_carousel(self, image_url: str) -> None:
        """Adiciona uma imagem ao carrossel."""
        self.carousel.append(image_url)
    
    def decorar_convite(self) -> dict:
        """Aplica decoração de luxo ao convite."""
        convite_base = super().decorar_convite()
        
        # Adiciona elementos de luxo
        luxo = {}
        if self.carousel:
            luxo["carousel"] = self.carousel
        
        if self.videos:
            luxo["videos"] = self.videos
            
        if self.sons:
            luxo["sons"] = self.sons
            
        if self.tipografia:
            luxo["tipografia"] = self.tipografia
        
        if luxo:
            convite_base["luxo"] = luxo
        
        return convite_base
