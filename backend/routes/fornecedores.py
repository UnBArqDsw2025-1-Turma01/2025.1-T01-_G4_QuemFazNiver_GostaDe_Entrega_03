from fastapi import APIRouter, HTTPException
from typing import List
from models import Fornecedor
import uuid
from database.db import fornecedores_db
from fornecedor_factory import get_fornecedor_factory

router = APIRouter(
    prefix="/fornecedores",
    tags=["Fornecedores"]
)

@router.post("/")
async def criar_fornecedor(fornecedor: Fornecedor, tipo: str):
    try:
        # Obter a fábrica correspondente ao tipo de fornecedor
        factory = get_fornecedor_factory(tipo)
        
        # Criar o fornecedor através da fábrica
        fornecedor_obj = factory.create_fornecedor(
            nome=fornecedor.nome,
            tags=fornecedor.tags,
            contato=fornecedor.contato,
            portfolio=fornecedor.portfolio
        )
        
        # Gerar ID e salvar no banco de dados
        fornecedor_id = str(uuid.uuid4())
        
        # Armazenar informações básicas no banco de dados
        fornecedores_db[fornecedor_id] = fornecedor
        
        return {
            "id": fornecedor_id,
            "nome": fornecedor.nome,
            "tipo": tipo,
            "info": fornecedor_obj.exibir_info(),
            "preco_base": fornecedor_obj.calcular_preco(),
            "servicos": fornecedor_obj.listar_servicos()
        }
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[Fornecedor])
async def listar_fornecedores():
    return list(fornecedores_db.values())

@router.get("/{fornecedor_id}")
async def obter_fornecedor(fornecedor_id: str):
    if fornecedor_id not in fornecedores_db:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    
    return fornecedores_db[fornecedor_id]
