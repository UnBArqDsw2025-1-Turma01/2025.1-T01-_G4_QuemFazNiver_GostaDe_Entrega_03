from fastapi import APIRouter, HTTPException, Body
from typing import List, Dict, Any
import uuid
from models import Usuario
from database.db import usuarios_db
from decorator import ConviteConcreto, DecoratorInterativo, DecoratorLuxo, TemplateDefault

router = APIRouter(
    prefix="/convites",
    tags=["Convites"]
)

# Storage for created invitations
convites_db = {}

@router.post("/basic/")
async def criar_convite_basico(
    destinatario_ids: List[str], 
    remetente_id: str,
    titulo: str = "Convite",
    mensagem: str = ""
):
    # Verificar se os usuários existem
    if remetente_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Remetente não encontrado")
    
    destinatarios = []
    for dest_id in destinatario_ids:
        if dest_id not in usuarios_db:
            raise HTTPException(status_code=404, detail=f"Destinatário {dest_id} não encontrado")
        destinatarios.append(usuarios_db[dest_id])
    
    remetente = usuarios_db[remetente_id]
    
    # Criar template padrão
    template = TemplateDefault()
    
    # Criar convite básico
    convite = ConviteConcreto(
        destinatario=destinatarios,
        remetente=remetente,
        titulo=titulo,
        template=template,
        mensagem=mensagem
    )
    
    # Salvar convite
    convite_id = str(uuid.uuid4())
    convites_db[convite_id] = convite
    
    response = convite.criar_convite()
    response["id"] = convite_id
    
    return response

@router.post("/interativo/")
async def criar_convite_interativo(
    convite_id: str = None,
    destinatario_ids: List[str] = None, 
    remetente_id: str = None,
    titulo: str = "Convite Interativo",
    mensagem: str = "",
    mapa: Dict[str, Any] = None,
    carousel: List[str] = None,
    comentarios: List[str] = None
):
    convite = None
    
    # Criar novo convite ou decorar existente
    if convite_id:
        if convite_id not in convites_db:
            raise HTTPException(status_code=404, detail=f"Convite {convite_id} não encontrado")
        convite = DecoratorInterativo(convites_db[convite_id])
    else:
        # Verificar parâmetros obrigatórios para novo convite
        if not destinatario_ids or not remetente_id:
            raise HTTPException(status_code=400, detail="Destinatários e remetente são necessários para criar novo convite")
            
        # Verificar se os usuários existem
        if remetente_id not in usuarios_db:
            raise HTTPException(status_code=404, detail="Remetente não encontrado")
        
        destinatarios = []
        for dest_id in destinatario_ids:
            if dest_id not in usuarios_db:
                raise HTTPException(status_code=404, detail=f"Destinatário {dest_id} não encontrado")
            destinatarios.append(usuarios_db[dest_id])
        
        remetente = usuarios_db[remetente_id]
        
        # Criar template padrão
        template = TemplateDefault()
        
        # Criar convite básico primeiro
        convite_base = ConviteConcreto(
            destinatario=destinatarios,
            remetente=remetente,
            titulo=titulo,
            template=template,
            mensagem=mensagem
        )
        
        # Decorar o convite básico
        convite = DecoratorInterativo(convite_base)
    
    # Configurar elementos interativos
    if mapa:
        convite.configurar_mapa(
            latitude=mapa.get("latitude", 0),
            longitude=mapa.get("longitude", 0),
            zoom=mapa.get("zoom", 15)
        )
    
    # Adicionar imagens ao carrossel
    if carousel:
        for imagem_url in carousel:
            convite.adicionar_imagem_carousel(imagem_url)
    
    # Adicionar comentários
    if comentarios:
        for comentario in comentarios:
            convite.adicionar_comentario(comentario)
    
    # Salvar convite
    convite_id = convite_id or str(uuid.uuid4())
    convites_db[convite_id] = convite
    
    response = convite.criar_convite()
    response["id"] = convite_id
    
    return response

@router.post("/luxo/")
async def criar_convite_luxo(
    convite_id: str = None,
    destinatario_ids: List[str] = None, 
    remetente_id: str = None,
    titulo: str = "Convite de Luxo",
    mensagem: str = "",
    carousel: List[str] = None,
    videos: List[str] = None,
    som: Dict[str, Any] = None,
    tipografia: str = None
):
    convite = None
    
    # Criar novo convite ou decorar existente
    if convite_id:
        if convite_id not in convites_db:
            raise HTTPException(status_code=404, detail=f"Convite {convite_id} não encontrado")
        convite = DecoratorLuxo(convites_db[convite_id])
    else:
        # Verificar parâmetros obrigatórios para novo convite
        if not destinatario_ids or not remetente_id:
            raise HTTPException(status_code=400, detail="Destinatários e remetente são necessários para criar novo convite")
            
        # Verificar se os usuários existem
        if remetente_id not in usuarios_db:
            raise HTTPException(status_code=404, detail="Remetente não encontrado")
        
        destinatarios = []
        for dest_id in destinatario_ids:
            if dest_id not in usuarios_db:
                raise HTTPException(status_code=404, detail=f"Destinatário {dest_id} não encontrado")
            destinatarios.append(usuarios_db[dest_id])
        
        remetente = usuarios_db[remetente_id]
        
        # Criar template padrão
        template = TemplateDefault()
        
        # Criar convite básico primeiro
        convite_base = ConviteConcreto(
            destinatario=destinatarios,
            remetente=remetente,
            titulo=titulo,
            template=template,
            mensagem=mensagem
        )
        
        # Decorar o convite básico
        convite = DecoratorLuxo(convite_base)
    
    # Configurar elementos de luxo
    
    # Adicionar imagens ao carrossel
    if carousel:
        for imagem_url in carousel:
            convite.adicionar_imagem_carousel(imagem_url)
    
    # Adicionar vídeos
    if videos:
        for video_url in videos:
            convite.adicionar_video(video_url)
    
    # Configurar som
    if som and "url" in som:
        convite.configurar_som(
            som_url=som["url"],
            autoplay=som.get("autoplay", False)
        )
    
    # Configurar tipografia
    if tipografia:
        convite.configurar_tipografia(tipografia)
    
    # Salvar convite
    convite_id = convite_id or str(uuid.uuid4())
    convites_db[convite_id] = convite
    
    response = convite.criar_convite()
    response["id"] = convite_id
    
    return response

@router.get("/{convite_id}")
async def obter_convite(convite_id: str):
    if convite_id not in convites_db:
        raise HTTPException(status_code=404, detail="Convite não encontrado")
        
    convite = convites_db[convite_id]
    response = convite.criar_convite()
    response["id"] = convite_id
    
    return response

@router.post("/{convite_id}/confirmar")
async def confirmar_convite(convite_id: str):
    if convite_id not in convites_db:
        raise HTTPException(status_code=404, detail="Convite não encontrado")
        
    convite = convites_db[convite_id]
    
    # Verificar se o convite tem o método confirmar_convite
    if hasattr(convite, 'confirmar_convite') and callable(getattr(convite, 'confirmar_convite')):
        convite.confirmar_convite()
        return {"message": "Convite confirmado com sucesso", "status": convite.get_status()}
    else:
        convite.set_status("CONFIRMADO")
        return {"message": "Status do convite atualizado para confirmado", "status": convite.get_status()}
