from fastapi import APIRouter, Form, HTTPException, UploadFile, File
from models import Midia, TipoMidia
from typing import List
import uuid

router = APIRouter(
    prefix="/midias",
    tags=["Mídias"]
)

# Mock storage for media
midias_db = {}

@router.post("/upload")
async def upload_midia(arquivo: UploadFile = File(...), tipo: str = "IMAGEM"):
    midia_id = str(uuid.uuid4())
    conteudo = await arquivo.read()
    
    midias_db[midia_id] = {
        "id": midia_id,
        "nome": arquivo.filename,
        "tipo": tipo,
        "conteudo": conteudo,
        "tamanho": len(conteudo)
    }
    
    return {"id": midia_id, "nome": arquivo.filename, "tipo": tipo}

@router.get("/{midia_id}")
async def get_midia(midia_id: str):
    if midia_id not in midias_db:
        raise HTTPException(status_code=404, detail="Mídia não encontrada")
    
    midia = midias_db[midia_id]
    return {
        "id": midia["id"],
        "nome": midia["nome"],
        "tipo": midia["tipo"],
        "tamanho": midia["tamanho"]
    }

@router.post("/")
async def adicionar_midia(
    url: str = Form(...),
    tipo: TipoMidia = Form(...),
):
    midia = Midia(url=url, tipo=tipo)
    return midia

@router.delete("/{url}")
async def remover_midia(url: str):
    return {"message": f"Mídia {url} removida com sucesso"}
