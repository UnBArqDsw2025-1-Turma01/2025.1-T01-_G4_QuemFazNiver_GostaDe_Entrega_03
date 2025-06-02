from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Convite(BaseModel):
    destinatario_id: str = Field(..., alias="destinatario")
    remetente_id: str = Field(..., alias="remetente")
    imagens: Optional[bytes] = None
    video: Optional[bytes] = None
    mensagem: Optional[str] = None
    dataEnvio: datetime = Field(default_factory=datetime.now)
    status: str = "PENDENTE"
