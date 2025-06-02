from pydantic import BaseModel

class Endereco(BaseModel):
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    cep: str
