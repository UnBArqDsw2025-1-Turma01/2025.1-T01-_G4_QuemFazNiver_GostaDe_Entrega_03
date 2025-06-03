from enum import Enum

class TipoMidia(str, Enum):
    IMAGEM = "IMAGEM"
    VIDEO = "VIDEO"

class TipoNotificacao(str, Enum):
    EMAIL = "EMAIL"
    WHATSAPP = "WHATSAPP"
    TELEGRAM = "TELEGRAM"
