from typing import List, Optional
from pydantic import BaseModel

class Fornecedor(BaseModel):
    nome: str
    tags: List[str] = []
    contato: str
    portfolio: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "nome": "Fornecedor Exemplo",
                "tags": ["comida", "bebida"],
                "contato": "contato@fornecedor.com",
                "portfolio": "Diversos serviços de alimentação"
            }
        }

class Portfolio(BaseModel):
    contatos: str
    descricao: str
