from .interfaces import NotificationFactory

class NotificationService:
    def __init__(self, factory: NotificationFactory):
        self.notification = factory.create_notification()

    def notify(self, destinatario: str, mensagem: str) -> None:
        self.notification.send_notification(destinatario, mensagem)
