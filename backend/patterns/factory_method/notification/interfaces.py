from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_notification(self, destinatario: str, mensagem: str) -> None:
        pass

class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass
