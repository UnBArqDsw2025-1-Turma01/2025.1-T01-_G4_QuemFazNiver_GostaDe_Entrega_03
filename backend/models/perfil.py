from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class Perfil(BaseModel):
    biografia: Optional[str] = None
    interesses: List[str] = []
    visibilidade: str = "publico"  # publico, privado, amigos
    quiz_realizado: bool = False
    fornecedores_contratados: List[Dict[str, Any]] = []
    buffet_contratado: Optional[Dict[str, Any]] = None
    festa_criada: Optional[Dict[str, Any]] = None
    evento_organizado: Optional[Dict[str, Any]] = None
    convite_criado: Optional[Dict[str, Any]] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "biografia": "Amo organizar festas e eventos especiais",
                "interesses": ["festas", "música", "gastronomia"],
                "visibilidade": "publico",
                "quiz_realizado": True,
                "fornecedores_contratados": [],
                "buffet_contratado": None,
                "festa_criada": None,
                "evento_organizado": None,
                "convite_criado": None
            }
        }
