class NotificationService:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def notify(self, nome_usuario: str, mensagem: str) -> None:
        print(f"[{self.tipo}] Notificando {nome_usuario}: {mensagem}")
