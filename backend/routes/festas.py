from fastapi import APIRouter, HTTPException, Body, Query
from typing import List
import uuid
from datetime import datetime
from models import Festa, Desejo, Convite, TipoNotificacao
from database.db import festas_db, usuarios_db
from patterns.factory_method.notification import (
    NotificationService, 
    EmailNotificationFactory, 
    WhatsAppNotificationFactory, 
    TelegramNotificationFactory
)
from patterns.builder.festa import AniversarioFestaBuilder, CasamentoFestaBuilder, FestaDirector
from patterns.observer.notificacao import notification_publisher
from patterns.observer.notificacao.publisher import notification_publisher

router = APIRouter(
    prefix="/festas",
    tags=["Festas"]
)

@router.post("/", response_model=Festa)
async def criar_festa(
    titulo: str,
    data: datetime,
    tipo_festa: str,  # "aniversario", "casamento", etc.
    descricao: str = None,
    anfitriao: str = None,
    local: str = None,
    convidados: List[str] = []
    
):
    # Seleciona o builder apropriado baseado no tipo da festa
    if tipo_festa == "aniversario":
        builder = AniversarioFestaBuilder()
    elif tipo_festa == "casamento":
        builder = CasamentoFestaBuilder()
    else:
        raise HTTPException(status_code=400, detail="Tipo de festa não suportado")
    
    # Usa o director para construir a festa
    director = FestaDirector(builder)
    
    if descricao and anfitriao and local and convidados:
        director.construir_festa_completa(titulo, data, descricao, anfitriao, local, convidados)
    else:
        director.construir_festa_basica(titulo, data, anfitriao)
        if descricao:
            builder.set_descricao(descricao)
        if local:
            builder.set_local(local)
        for convidado in convidados:
            builder.add_convidado(convidado)
    
    festa = builder.build()
    festa_id = str(uuid.uuid4())
    festa.id = festa_id
    festas_db[festa_id] = festa
    
    return festa

@router.get("/", response_model=List[Festa])
async def listar_festas():
    return list(festas_db.values())

@router.get("/{festa_id}", response_model=Festa)
async def obter_festa(festa_id: str):
    if festa_id not in festas_db:
        raise HTTPException(status_code=404, detail="Festa não encontrada")
    return festas_db[festa_id]

@router.post("/{festa_id}/adicionar-convidado/{usuario_id}")
async def adicionar_convidado(festa_id: str, usuario_id: str):
    if festa_id not in festas_db:
        raise HTTPException(status_code=404, detail="Festa não encontrada")
    
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    if usuario_id not in festas_db[festa_id].listaConvidados:
        festas_db[festa_id].listaConvidados.append(usuario_id)
        
        # Inscrever usuário como observador usando o tipo de notificação preferido
        usuario = usuarios_db[usuario_id]
        # Aqui poderia verificar o tipo de notificação preferida do usuário
        # Por padrão, adicionamos como EmailSubscriber
        email_subscriber = EmailSubscriber(usuario)
        notification_publisher.subscribe(email_subscriber)
        
        # Notificar sobre adição de convidado
        notification_publisher.notify_all_subscribers({
            "tipo": "CONVIDADO_ADICIONADO",
            "mensagem": f"Novo convidado adicionado à festa: {usuario.nome}",
            "festa_id": festa_id,
            "convidado_id": usuario_id
        })
    
    return {"message": "Convidado adicionado com sucesso"}

@router.post("/{festa_id}/adicionar-desejo", response_model=Desejo)
async def adicionar_desejo(festa_id: str, desejo: Desejo):
    if festa_id not in festas_db:
        raise HTTPException(status_code=404, detail="Festa não encontrada")
    
    festas_db[festa_id].desejos.append(desejo)
    
    # Notificar sobre novo desejo
    notification_publisher.notify_all_subscribers({
        "tipo": "DESEJO_ADICIONADO",
        "mensagem": f"Novo desejo adicionado à festa: {desejo.nome}",
        "festa_id": festa_id,
        "desejo": desejo.nome
    })
    
    return desejo

@router.put("/{festa_id}/marcar-desejo-adquirido")
async def marcar_desejo(festa_id: str, nome_desejo: str = Query(...)):
    if festa_id not in festas_db:
        raise HTTPException(status_code=404, detail="Festa não encontrada")
    
    for desejo in festas_db[festa_id].desejos:
        if desejo.nome == nome_desejo:
            desejo.foiAdquirido = True
            
            # Notificar que o desejo foi adquirido
            notification_publisher.notify_all_subscribers({
                "tipo": "DESEJO_ADQUIRIDO",
                "mensagem": f"O desejo '{nome_desejo}' foi adquirido!",
                "festa_id": festa_id,
                "desejo": nome_desejo
            })
            
            return {"message": f"Desejo '{nome_desejo}' marcado como adquirido"}
    
    raise HTTPException(status_code=404, detail="Desejo não encontrado")

@router.post("/{festa_id}/enviar-convites")
async def enviar_convites(festa_id: str):
    if festa_id not in festas_db:
        raise HTTPException(status_code=404, detail="Festa não encontrada")
    
    for usuario_id in festas_db[festa_id].listaConvidados:
        convite = Convite(
            destinatario=usuario_id,
            remetente=festa_id,
            mensagem=f"Você está convidado para a festa!",
            dataEnvio=datetime.now()
        )
        festas_db[festa_id].convites.append(convite)
    
    return {"message": f"{len(festas_db[festa_id].listaConvidados)} convites enviados com sucesso"}

@router.post("/{festa_id}/notificar-convidados")
async def notificar_convidados(
    festa_id: str, 
    mensagem: str = Body(..., embed=True),
    tipo_notificacao: TipoNotificacao = Body(TipoNotificacao.EMAIL, embed=True)
):
    if festa_id not in festas_db:
        raise HTTPException(status_code=404, detail="Festa não encontrada")
    
    # Selecionar a fábrica apropriada com base no tipo de notificação
    factory_map = {
        TipoNotificacao.EMAIL: EmailNotificationFactory(),
        TipoNotificacao.WHATSAPP: WhatsAppNotificationFactory(),
        TipoNotificacao.TELEGRAM: TelegramNotificationFactory()
    }
    
    factory = factory_map.get(tipo_notificacao)
    notification_service = NotificationService(factory)
    
    # Enviar notificação para cada convidado
    for usuario_id in festas_db[festa_id].listaConvidados:
        if usuario_id in usuarios_db:
            notification_service.notify(
                usuarios_db[usuario_id].nome,  # Usando o nome como destinatário para simplificar
                mensagem
            )
    
    return {
        "message": f"{len(festas_db[festa_id].listaConvidados)} convidados notificados com sucesso",
        "tipo_notificacao": tipo_notificacao
    }
