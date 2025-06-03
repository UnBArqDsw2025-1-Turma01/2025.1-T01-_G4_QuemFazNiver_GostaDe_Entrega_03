from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from models import Usuario
from .enums import StatusConvite

class Convite(ABC):
    def __init__(
        self,
        destinatario: List[Usuario],
        remetente: Usuario,
        titulo: str,
        template=None,
        mensagem: str = "",
        dataEnvio: datetime = None
    ):
        self.destinatario = destinatario
        self.remetente = remetente
        self.titulo = titulo
        self.template = template
        self.mensagem = mensagem
        self.dataEnvio = dataEnvio or datetime.now()
        self._status = StatusConvite.PENDENTE

    @abstractmethod
    def criar_convite(self) -> dict:
        pass

    def get_status(self) -> str:
        return self._status

    def set_status(self, status: StatusConvite) -> None:
        self._status = status