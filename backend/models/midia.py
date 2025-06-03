from pydantic import BaseModel, Field
from datetime import datetime
from .enums import TipoMidia

class Midia(BaseModel):
    url: str
    tipo: TipoMidia
    dataUpload: datetime = Field(default_factory=datetime.now)
