from enum import Enum

class TipoDeNotificacao(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
