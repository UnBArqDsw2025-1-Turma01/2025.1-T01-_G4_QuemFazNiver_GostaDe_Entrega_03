from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from patterns.composite.fornecedor.evento import Evento
from patterns.composite.fornecedor.folhas import Banda, LocacaoLocal, Seguranca, Decoracao, Comida

router = APIRouter(
    prefix="/eventos",
    tags=["Eventos - Composite Pattern"]
)

# Storage for created events
eventos_db = {}

@router.post("/")
async def criar_evento(nome: str, tipos_fornecedor: List[str]) -> Dict[str, Any]:
    """
    Cria um evento com diferentes tipos de fornecedores usando o padrão Composite.
    
    - **nome**: Nome do evento
    - **tipos_fornecedor**: Lista de tipos ("banda", "locacao", "seguranca", "decoracao", "comida")
    """
    evento = Evento(nome)
    
    # Mapear tipos de fornecedor para classes
    fornecedor_types = {
        "banda": Banda(),
        "locacao": LocacaoLocal(),
        "seguranca": Seguranca(),
        "decoracao": Decoracao(),
        "comida": Comida()
    }
    
    # Adicionar os tipos de fornecedor solicitados
    fornecedores_adicionados = []
    for tipo in tipos_fornecedor:
        if tipo.lower() in fornecedor_types:
            evento.add(fornecedor_types[tipo.lower()])
            fornecedores_adicionados.append(tipo)
    
    # Salvar evento
    eventos_db[nome] = evento
    
    # Montar evento
    montagem = evento.montar_evento()
    calculo = evento.calcular_evento()
    
    return {
        "evento": nome,
        "fornecedores_adicionados": fornecedores_adicionados,
        "montagem": montagem,
        "calculo": calculo,
        "total_fornecedores": len(evento.fornecedores)
    }

@router.get("/{nome}")
async def obter_evento(nome: str) -> Dict[str, Any]:
    """
    Obtém um evento existente e seus fornecedores.
    """
    if nome not in eventos_db:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    
    evento = eventos_db[nome]
    
    return {
        "evento": evento.nome,
        "fornecedores": [f.__class__.__name__ for f in evento.fornecedores],
        "montagem": evento.montar_evento(),
        "calculo": evento.calcular_evento(),
        "total_fornecedores": len(evento.fornecedores)
    }

@router.post("/{nome}/adicionar-fornecedor")
async def adicionar_fornecedor_evento(nome: str, tipo_fornecedor: str) -> Dict[str, Any]:
    """
    Adiciona um novo fornecedor a um evento existente.
    """
    if nome not in eventos_db:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    
    evento = eventos_db[nome]
    
    fornecedor_types = {
        "banda": Banda(),
        "locacao": LocacaoLocal(),
        "seguranca": Seguranca(),
        "decoracao": Decoracao(),
        "comida": Comida()
    }
    
    if tipo_fornecedor.lower() not in fornecedor_types:
        raise HTTPException(status_code=400, detail="Tipo de fornecedor inválido")
    
    evento.add(fornecedor_types[tipo_fornecedor.lower()])
    
    return {
        "message": f"Fornecedor {tipo_fornecedor} adicionado ao evento {nome}",
        "fornecedores_atuais": [f.__class__.__name__ for f in evento.fornecedores],
        "total_fornecedores": len(evento.fornecedores),
        "calculo_atualizado": evento.calcular_evento()
    }

@router.delete("/{nome}/remover-fornecedor")
async def remover_fornecedor_evento(nome: str, tipo_fornecedor: str) -> Dict[str, Any]:
    """
    Remove um fornecedor de um evento existente.
    """
    if nome not in eventos_db:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    
    evento = eventos_db[nome]
    
    # Encontrar e remover o fornecedor
    fornecedor_removido = None
    for fornecedor in evento.fornecedores:
        if fornecedor.__class__.__name__.lower() == tipo_fornecedor.lower():
            evento.remove(fornecedor)
            fornecedor_removido = fornecedor.__class__.__name__
            break
    
    if not fornecedor_removido:
        raise HTTPException(status_code=404, detail="Tipo de fornecedor não encontrado no evento")
    
    return {
        "message": f"Fornecedor {fornecedor_removido} removido do evento {nome}",
        "fornecedores_restantes": [f.__class__.__name__ for f in evento.fornecedores],
        "total_fornecedores": len(evento.fornecedores),
        "calculo_atualizado": evento.calcular_evento()
    }

@router.get("/")
async def listar_eventos() -> Dict[str, Any]:
    """
    Lista todos os eventos criados.
    """
    eventos_info = {}
    for nome, evento in eventos_db.items():
        eventos_info[nome] = {
            "fornecedores": [f.__class__.__name__ for f in evento.fornecedores],
            "total_fornecedores": len(evento.fornecedores),
            "calculo": evento.calcular_evento()
        }
    
    return {
        "total_eventos": len(eventos_db),
        "eventos": eventos_info
    }

@router.post("/{nome}/executar-montagem")
async def executar_montagem_evento(nome: str) -> Dict[str, Any]:
    """
    Executa a montagem completa do evento, demonstrando o padrão Composite em ação.
    """
    if nome not in eventos_db:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    
    evento = eventos_db[nome]
    
    if not evento.fornecedores:
        raise HTTPException(status_code=400, detail="Evento não possui fornecedores para montagem")
    
    montagem_detalhada = []
    for i, resultado in enumerate(evento.montar_evento(), 1):
        montagem_detalhada.append({
            "etapa": i,
            "acao": resultado,
            "fornecedor": evento.fornecedores[i-1].__class__.__name__
        })
    
    return {
        "evento": evento.nome,
        "status": "Montagem executada com sucesso",
        "etapas_executadas": montagem_detalhada,
        "resumo": evento.calcular_evento(),
        "total_etapas": len(montagem_detalhada)
    }
