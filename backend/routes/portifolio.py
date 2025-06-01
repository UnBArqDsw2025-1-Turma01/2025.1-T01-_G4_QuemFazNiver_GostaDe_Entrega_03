from fastapi import APIRouter, HTTPException
from typing import List, Optional, Union
from pydantic import BaseModel

from portifolio_buffet import PortifolioBuffet
from portifolio_fotografia import PortifolioFotografia
from portifolio_confeitaria import PortifolioConfeitaria

router = APIRouter(
    prefix="/portifolios",
    tags=["Portifolios"]
)

class PortifolioBase(BaseModel):
    titulo: str
    descricao: str
    valores: float
    funcionamento: str
    tipo: str  # "buffet", "fotografia", "confeitaria"

class PortifolioBuffetCreate(PortifolioBase):
    tipo_evento: str
    cardapio_pratos: List[str]

class PortifolioFotografiaCreate(PortifolioBase):
    estilo_fotografia: str
    amostras_fotos: List[str]

class PortifolioConfeitariaCreate(PortifolioBase):
    tipo_doce: List[str]
    cardapio_doces: List[str]
    cardapio_restricoes: List[str]

@router.post("/")
async def gerar_portifolio(portifolio_data: dict):
    tipo = portifolio_data.get("tipo")

    try:
        if tipo == "buffet":
            data = PortifolioBuffetCreate(**portifolio_data)
            port = PortifolioBuffet(
                titulo=data.titulo,
                descricao=data.descricao,
                valores=data.valores,
                funcionamento=data.funcionamento,
                tipo_evento=data.tipo_evento,
                cardapio_pratos=data.cardapio_pratos
            )

        elif tipo == "fotografia":
            data = PortifolioFotografiaCreate(**portifolio_data)
            port = PortifolioFotografia(
                titulo=data.titulo,
                descricao=data.descricao,
                valores=data.valores,
                funcionamento=data.funcionamento,
                estilo_fotografia=data.estilo_fotografia,
                amostras_fotos=data.amostras_fotos
            )

        elif tipo == "confeitaria":
            data = PortifolioConfeitariaCreate(**portifolio_data)
            port = PortifolioConfeitaria(
                titulo=data.titulo,
                descricao=data.descricao,
                valores=data.valores,
                funcionamento=data.funcionamento,
                tipo_doce=data.tipo_doce,
                cardapio_doces=data.cardapio_doces,
                cardapio_restricoes=data.cardapio_restricoes
            )

        else:
            raise ValueError("Tipo de portfólio inválido.")

        return port.gerar_portifolio()

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
