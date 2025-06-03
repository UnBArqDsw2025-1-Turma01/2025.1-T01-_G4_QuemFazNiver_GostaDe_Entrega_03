from typing import List, Optional
from pydantic import BaseModel
from datetime import date
from .desejo import Desejo
from .convite import Convite

class Festa(BaseModel):
    id: Optional[str] = None
    listaConvidados: List[str] = []
    dataEvento: date
    temas: List[str] = []
    desejos: List[Desejo] = []
    convites: List[Convite] = []
    
    class Config:
        json_schema_extra = {
            "example": {
                "dataEvento": "2023-12-31",
                "temas": ["Ano Novo", "Festa"]
            }
        }
