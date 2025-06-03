from typing import List, Optional
from pydantic import BaseModel
from datetime import date
from .perfil import Perfil
from .endereco import Endereco
from .quiz import Quiz

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    dataNascimento: date
    foto: Optional[bytes] = None
    sobreMim: Optional[str] = None
    tagsDePreferencias: List[str] = []
    perfil: Optional[Perfil] = None
    endereco: Optional[Endereco] = None
    quizzes: List[Quiz] = []
    
    class Config:
        schema_extra = {
            "example": {
                "nome": "João Silva",
                "dataNascimento": "1990-01-01",
                "sobreMim": "Gosto de festas e eventos",
                "tagsDePreferencias": ["música", "gastronomia"]
            }
        }
