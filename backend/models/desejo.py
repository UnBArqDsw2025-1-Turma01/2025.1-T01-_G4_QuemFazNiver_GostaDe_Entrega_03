from pydantic import BaseModel

class Desejo(BaseModel):
    nome: str
    hyperlink: str
    foiAdquirido: bool = False
