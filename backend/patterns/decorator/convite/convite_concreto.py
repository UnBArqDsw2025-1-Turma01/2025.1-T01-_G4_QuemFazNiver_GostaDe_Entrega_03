from .convite_base import Convite
from models import Usuario
from typing import List
from datetime import datetime

class TemplateDefault:
    def __init__(self):
        self.paletaCores = ["#FFFFFF", "#000000", "#FF5733"]
        self.tema = "Padrão"

    def criar_convite(self) -> dict:
        return {
            "tipo": "template_default",
            "paletaCores": self.paletaCores,
            "tema": self.tema
        }

class ConviteConcreto(Convite):
    def criar_convite(self) -> dict:
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