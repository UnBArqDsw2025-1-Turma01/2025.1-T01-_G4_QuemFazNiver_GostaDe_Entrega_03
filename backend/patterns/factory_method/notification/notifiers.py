from .interfaces import Notification

class WhatsApp(Notification):
    def __init__(self):
        self.access_token = "access-token-whatsapp"
    
    def send_notification(self, destinatario: str, mensagem: str) -> None:
        print(f"WhatsApp para {destinatario}: {mensagem}")

class Telegram(Notification):
    def __init__(self):
        self.bot_token = "bot-token-telegram"
        self.chat_id = "default-chat-id"
        self.api_url = "https://api.telegram.org"

    def send_notification(self, destinatario: str, mensagem: str) -> None:
        print(f"Telegram para {destinatario}: {mensagem}")

class Email(Notification):
    def __init__(self):
        self.email_origin = "sistema@festas.com"
        self.senha_app = "senha-app-email"
        self.servidor_smtp = "smtp.festas.com"
        self.porta = 587

    def send_notification(self, destinatario: str, mensagem: str) -> None:
        print(f"Email para {destinatario}: {mensagem}")
