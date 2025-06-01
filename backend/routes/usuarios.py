from fastapi import APIRouter, HTTPException, UploadFile, File, Path, Body
from typing import List
import uuid
from models import Usuario
from database.db import usuarios_db

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

@router.post("/", response_model=Usuario, summary="Criar novo usuário")
async def criar_usuario(usuario: Usuario = Body(..., description="Dados do usuário a ser criado")):
    """
    Cria um novo usuário no sistema.
    
    - **nome**: Nome completo do usuário
    - **dataNascimento**: Data de nascimento no formato YYYY-MM-DD
    - **sobreMim**: (Opcional) Descrição pessoal
    - **tagsDePreferencias**: (Opcional) Lista de tags de preferências
    
    Retorna o usuário criado com seu ID.
    """
    usuario_id = str(uuid.uuid4())
    usuario.id = usuario_id
    usuarios_db[usuario_id] = usuario
    return usuario

@router.get("/", response_model=List[Usuario], summary="Listar todos os usuários")
async def listar_usuarios():
    """
    Lista todos os usuários cadastrados no sistema.
    
    Retorna uma lista de objetos do tipo Usuário.
    """
    return list(usuarios_db.values())

@router.get("/{usuario_id}", response_model=Usuario, summary="Obter usuário por ID")
async def obter_usuario(
    usuario_id: str = Path(..., description="ID único do usuário a ser consultado")
):
    """
    Busca um usuário específico pelo seu ID.
    
    - **usuario_id**: ID único do usuário
    
    Retorna os detalhes do usuário encontrado.
    """
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuarios_db[usuario_id]

@router.put("/{usuario_id}", response_model=Usuario, summary="Atualizar usuário")
async def atualizar_usuario(
    usuario_id: str = Path(..., description="ID único do usuário a ser atualizado"),
    usuario: Usuario = Body(..., description="Novos dados do usuário")
):
    """
    Atualiza as informações de um usuário existente.
    
    - **usuario_id**: ID único do usuário
    - **usuario**: Objeto com os novos dados do usuário
    
    Retorna o usuário atualizado.
    """
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario.id = usuario_id
    usuarios_db[usuario_id] = usuario
    return usuario

@router.post("/{usuario_id}/alterar-foto", summary="Alterar foto do usuário")
async def alterar_foto(
    usuario_id: str = Path(..., description="ID único do usuário"),
    imagem: UploadFile = File(..., description="Nova foto do usuário")
):
    """
    Altera a foto de perfil de um usuário.
    
    - **usuario_id**: ID único do usuário
    - **imagem**: Arquivo de imagem para o perfil
    
    Retorna uma mensagem de confirmação.
    """
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    conteudo = await imagem.read()
    usuarios_db[usuario_id].foto = conteudo
    return {"message": "Foto atualizada com sucesso"}
