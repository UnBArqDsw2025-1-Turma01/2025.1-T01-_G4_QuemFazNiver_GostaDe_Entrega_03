from .interfaces import NotificationFactory
from .notifiers import WhatsApp, Telegram, Email

class WhatsAppNotificationFactory(NotificationFactory):
    def create_notification(self):
        return WhatsApp()

class TelegramNotificationFactory(NotificationFactory):
    def create_notification(self):
        return Telegram()

class EmailNotificationFactory(NotificationFactory):
    def create_notification(self):
        return Email()
