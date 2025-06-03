from pydantic import BaseModel
from .enums import TipoNotificacao

class MensagemNotificacao(BaseModel):
    destinatario: str
    mensagem: str
    tipo_notificacao: TipoNotificacao = TipoNotificacao.EMAIL
