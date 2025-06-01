from fastapi import APIRouter, Query, HTTPException
from typing import List, Dict
from database.db import fornecedores_db

router = APIRouter(
    prefix="/sugestoes",
    tags=["Sugestões"]
)

# Mock data para sugestões
sugestoes_presentes = [
    {"id": "1", "nome": "Livro", "categoria": "Cultura", "faixa_preco": "Baixo"},
    {"id": "2", "nome": "Perfume", "categoria": "Moda", "faixa_preco": "Médio"},
    {"id": "3", "nome": "Smartwatch", "categoria": "Tecnologia", "faixa_preco": "Alto"},
]

sugestoes_temas = [
    {"id": "1", "nome": "Anos 80", "categoria": "Retro"},
    {"id": "2", "nome": "Super Heróis", "categoria": "Infantil"},
    {"id": "3", "nome": "Luau", "categoria": "Praia"},
]

@router.get("/presentes")
async def listar_sugestoes_presentes(categoria: str = None, faixa_preco: str = None):
    resultados = sugestoes_presentes
    
    if categoria:
        resultados = [sugestao for sugestao in resultados if sugestao["categoria"] == categoria]
    
    if faixa_preco:
        resultados = [sugestao for sugestao in resultados if sugestao["faixa_preco"] == faixa_preco]
    
    return resultados

@router.get("/temas")
async def listar_sugestoes_temas(categoria: str = None):
    resultados = sugestoes_temas
    
    if categoria:
        resultados = [tema for tema in resultados if tema["categoria"] == categoria]
    
    return resultados

@router.get("/personalizado/{usuario_id}")
async def sugestoes_personalizadas(usuario_id: str):
    # Simular recomendações personalizadas
    # Em uma implementação real, isso usaria um algoritmo de recomendação
    # baseado nas preferências do usuário
    return {
        "presentes": sugestoes_presentes[:2],
        "temas": sugestoes_temas[:1],
        "baseado_em": ["histórico", "preferências"]
    }

@router.get("/por-tema/")
async def sugerir_fornecedor_por_tema(temas: List[str] = Query(...)):
    sugestoes = []
    
    for fornecedor_id, fornecedor in fornecedores_db.items():
        for tema in temas:
            if tema in fornecedor.tags:
                sugestoes.append(fornecedor)
                break
    
    return sugestoes

@router.get("/por-tags/")
async def sugerir_fornecedor_por_tags(tags: List[str] = Query(...)):
    sugestoes = []
    
    for fornecedor_id, fornecedor in fornecedores_db.items():
        for tag in tags:
            if tag in fornecedor.tags:
                sugestoes.append(fornecedor)
                break
    
    return sugestoes
