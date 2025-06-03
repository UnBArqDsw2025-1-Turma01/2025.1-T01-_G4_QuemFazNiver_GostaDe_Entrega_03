from abc import ABC, abstractmethod

class NotificationProduct(ABC):
    @abstractmethod
    def send_notification(self, destinatario: str, message: str) -> None:
        """Notify the user with a message."""
        pass


class ConcreteWhatsAppNotification(NotificationProduct):
    def send_notification(self, destinatario: str, message: str) -> None:
        print(f"Sending WhatsApp notification to {destinatario} with message: {message}")


class ConcreteEmailNotification(NotificationProduct):
    def send_notification(self,destinatario: str, message: str) -> None:
        print(f"Sending Email notification to {destinatario} with message: {message}")


class ConcreteTelegramNotification(NotificationProduct):
    def send_notification(self, destinatario: str, message: str) -> None:
        print(f"Sending Telegram notification to {destinatario} with message: {message}")
