from abc import ABC, abstractmethod
from typing import List, cast
from observer.subject import Subject, Festa
from factory.NotificationCreators import NotificationCreator, NotificationType, EmailCreator, WhatsAppCreator, TelegramCreator

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class UsuarioObserver(Observer):
    def __init__(self, nome: str, notification_type: List[NotificationType] = []) -> None:
        self.nome = nome
        self.notification_type = notification_type

    def update(self, subject: Subject) -> None:
        festa = cast(Festa, subject)
        notification_creator: NotificationCreator
        for type in self.notification_type:
            if type == NotificationType.EMAIL:
                notification_creator = EmailCreator()
            elif type == NotificationType.WHATSAPP:
                notification_creator = WhatsAppCreator()
            elif type == NotificationType.TELEGRAM:
                notification_creator = TelegramCreator()
            else:
                raise ValueError(f"Tipo de notificação desconhecido: {type}")

            notification_product = notification_creator.notification_factory()
            notification_product.send_notification(
                destinatario=self.nome,
                message=festa.get_state()
            ) 
