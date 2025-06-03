from typing import Optional
from pydantic import BaseModel

class Endereco(BaseModel):
    rua: str
    numero: str
    complemento: Optional[str] = None
    bairro: str
    cidade: str
    estado: str
    cep: str
    
    class Config:
        schema_extra = {
            "example": {
                "rua": "Rua das Flores",
                "numero": "123",
                "complemento": "Apt 45",
                "bairro": "Centro",
                "cidade": "São Paulo",
                "estado": "SP",
                "cep": "01234-567"
            }
        }
