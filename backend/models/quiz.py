from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Opcao(BaseModel):
    texto: str
    correta: Optional[bool] = False

class Pergunta(BaseModel):
    texto: str
    opcoes: List[Opcao]

class Quiz(BaseModel):
    titulo: str
    numPerguntas: int
    respostaQuiz: Optional[datetime] = None
    tipo: str
    perguntas: List[Pergunta] = []
