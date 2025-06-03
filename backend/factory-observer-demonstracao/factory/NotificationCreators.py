from enum import Enum
from abc import ABC, abstractmethod
from factory.NotificationProducts import ConcreteEmailNotification, ConcreteTelegramNotification, ConcreteWhatsAppNotification, NotificationProduct

class NotificationType(Enum):
    EMAIL = "EMAIL"
    WHATSAPP = "WHATSAPP"
    TELEGRAM = "TELEGRAM"

class NotificationCreator(ABC):
    @abstractmethod
    def notification_factory(self) -> NotificationProduct:
        pass

class WhatsAppCreator(NotificationCreator):
    def notification_factory(self):
        return ConcreteWhatsAppNotification()

class EmailCreator(NotificationCreator):
    def notification_factory(self):
        return ConcreteEmailNotification()

class TelegramCreator(NotificationCreator):
    def notification_factory(self):
        return ConcreteTelegramNotification()
