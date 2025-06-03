from .notification_service import NotificationService
from .tipos import TipoDeNotificacao

class Usuario:
    def __init__(self, nome: str, tipos_de_notificacao: list[TipoDeNotificacao]):
        self.nome = nome
        self.tiposDeNotificacao = tipos_de_notificacao

    def update(self, mensagem: str) -> None:
        for tipo in self.tiposDeNotificacao:
            NotificationService(tipo).notify(self.nome, mensagem)
