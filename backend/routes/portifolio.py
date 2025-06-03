from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from patterns.template_method.portifolio_buffet import PortifolioBuffet
from patterns.template_method.portifolio_fotografia import PortifolioFotografia
from patterns.template_method.portifolio_confeitaria import PortifolioConfeitaria

router = APIRouter(
    prefix="/portifolios",
    tags=["Portfólios"]
)

@router.post("/buffet")
async def criar_portifolio_buffet(
    titulo: str,
    descricao: str,
    valores: float,
    funcionamento: str,
    tipo_evento: str,
    cardapio_pratos: list[str]
) -> Dict[str, Any]:
    """
    Cria um portfólio para serviço de buffet.
    
    - **titulo**: Título do portfólio
    - **descricao**: Descrição do serviço
    - **valores**: Valores a partir de (em reais)
    - **funcionamento**: Horários de funcionamento
    - **tipo_evento**: Tipo de evento atendido
    - **cardapio_pratos**: Lista de pratos oferecidos
    """
    portifolio = PortifolioBuffet(
        titulo=titulo,
        descricao=descricao,
        valores=valores,
        funcionamento=funcionamento,
        tipo_evento=tipo_evento,
        cardapio_pratos=cardapio_pratos
    )
    
    return portifolio.gerar_portifolio()

@router.post("/fotografia")
async def criar_portifolio_fotografia(
    titulo: str,
    descricao: str,
    valores: float,
    funcionamento: str,
    estilo_fotografia: str,
    amostras_fotos: list[str]
) -> Dict[str, Any]:
    """
    Cria um portfólio para serviço de fotografia.
    
    - **titulo**: Título do portfólio
    - **descricao**: Descrição do serviço
    - **valores**: Valores a partir de (em reais)
    - **funcionamento**: Horários de funcionamento
    - **estilo_fotografia**: Estilo fotográfico oferecido
    - **amostras_fotos**: Links para amostras de fotos
    """
    portifolio = PortifolioFotografia(
        titulo=titulo,
        descricao=descricao,
        valores=valores,
        funcionamento=funcionamento,
        estilo_fotografia=estilo_fotografia,
        amostras_fotos=amostras_fotos
    )
    
    return portifolio.gerar_portifolio()

@router.post("/confeitaria")
async def criar_portifolio_confeitaria(
    titulo: str,
    descricao: str,
    valores: float,
    funcionamento: str,
    tipo_doce: list[str],
    cardapio_doces: list[str],
    cardapio_restricoes: list[str]
) -> Dict[str, Any]:
    """
    Cria um portfólio para serviço de confeitaria.
    
    - **titulo**: Título do portfólio
    - **descricao**: Descrição do serviço
    - **valores**: Valores a partir de (em reais)
    - **funcionamento**: Horários de funcionamento
    - **tipo_doce**: Tipos de doces oferecidos
    - **cardapio_doces**: Lista de doces disponíveis
    - **cardapio_restricoes**: Opções para restrições alimentares
    """
    portifolio = PortifolioConfeitaria(
        titulo=titulo,
        descricao=descricao,
        valores=valores,
        funcionamento=funcionamento,
        tipo_doce=tipo_doce,
        cardapio_doces=cardapio_doces,
        cardapio_restricoes=cardapio_restricoes
    )
    
    return portifolio.gerar_portifolio()
