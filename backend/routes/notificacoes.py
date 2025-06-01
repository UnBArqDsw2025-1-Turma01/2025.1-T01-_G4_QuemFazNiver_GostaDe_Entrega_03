from fastapi import APIRouter, HTTPException
from typing import List
from models import MensagemNotificacao, TipoNotificacao
from notification import (
    WhatsAppNotificationFactory,
    TelegramNotificationFactory, 
    EmailNotificationFactory,
    NotificationService
)

router = APIRouter(
    prefix="/notificacoes",
    tags=["Notificações"]
)

@router.post("/")
async def enviar_notificacao(mensagem: MensagemNotificacao):
    # Selecionar a fábrica de notificação adequada
    if mensagem.tipo_notificacao == TipoNotificacao.WHATSAPP:
        factory = WhatsAppNotificationFactory()
    elif mensagem.tipo_notificacao == TipoNotificacao.TELEGRAM:
        factory = TelegramNotificationFactory()
    else:  # Email é o padrão
        factory = EmailNotificationFactory()
    
    # Criar o serviço de notificação com a fábrica selecionada
    notification_service = NotificationService(factory)
    
    # Enviar a notificação
    notification_service.notify(mensagem.destinatario, mensagem.mensagem)
    
    return {
        "mensagem": "Notificação enviada com sucesso",
        "tipo": mensagem.tipo_notificacao,
        "destinatario": mensagem.destinatario
    }
