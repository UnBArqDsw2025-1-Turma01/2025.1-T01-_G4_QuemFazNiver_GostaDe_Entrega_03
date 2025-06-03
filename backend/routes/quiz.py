from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from patterns.composite.quiz.persona import Persona
from patterns.composite.quiz.folhas import Preferencia, Tematica, Localidade, Estilo, Comida

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz - Composite Pattern"]
)

# Storage for created personas
personas_db = {}

@router.post("/persona")
async def criar_persona_quiz(nome: str, tipos_quiz: List[str]) -> Dict[str, Any]:
    """
    Cria uma persona com diferentes tipos de quiz usando o padrão Composite.
    
    - **nome**: Nome da persona
    - **tipos_quiz**: Lista de tipos de quiz ("preferencia", "tematica", "localidade", "estilo", "comida")
    """
    persona = Persona(nome)
    
    # Mapear tipos de quiz para classes
    quiz_types = {
        "preferencia": Preferencia(),
        "tematica": Tematica(),
        "localidade": Localidade(),
        "estilo": Estilo(),
        "comida": Comida()
    }
    
    # Adicionar os tipos de quiz solicitados
    for tipo in tipos_quiz:
        if tipo.lower() in quiz_types:
            persona.add_question(quiz_types[tipo.lower()])
    
    # Salvar persona
    personas_db[nome] = persona
    
    # Montar e retornar o quiz
    quiz_montado = persona.montar_quiz()
    
    return {
        "persona": nome,
        "tipos_quiz_adicionados": tipos_quiz,
        "quiz_montado": quiz_montado,
        "total_componentes": len(persona.componentes)
    }

@router.get("/persona/{nome}")
async def obter_persona_quiz(nome: str) -> Dict[str, Any]:
    """
    Obtém uma persona existente e seus componentes de quiz.
    """
    if nome not in personas_db:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    
    persona = personas_db[nome]
    
    return {
        "persona": persona.nome,
        "componentes": [comp.__class__.__name__ for comp in persona.componentes],
        "quiz_montado": persona.montar_quiz(),
        "total_componentes": len(persona.componentes)
    }

@router.post("/persona/{nome}/adicionar-quiz")
async def adicionar_quiz_persona(nome: str, tipo_quiz: str) -> Dict[str, Any]:
    """
    Adiciona um novo tipo de quiz a uma persona existente.
    """
    if nome not in personas_db:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    
    persona = personas_db[nome]
    
    quiz_types = {
        "preferencia": Preferencia(),
        "tematica": Tematica(),
        "localidade": Localidade(),
        "estilo": Estilo(),
        "comida": Comida()
    }
    
    if tipo_quiz.lower() not in quiz_types:
        raise HTTPException(status_code=400, detail="Tipo de quiz inválido")
    
    persona.add_question(quiz_types[tipo_quiz.lower()])
    
    return {
        "message": f"Quiz {tipo_quiz} adicionado à persona {nome}",
        "componentes_atuais": [comp.__class__.__name__ for comp in persona.componentes],
        "total_componentes": len(persona.componentes)
    }

@router.delete("/persona/{nome}/remover-quiz")
async def remover_quiz_persona(nome: str, tipo_quiz: str) -> Dict[str, Any]:
    """
    Remove um tipo de quiz de uma persona existente.
    """
    if nome not in personas_db:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    
    persona = personas_db[nome]
    
    # Encontrar e remover o componente
    componente_removido = None
    for comp in persona.componentes:
        if comp.__class__.__name__.lower() == tipo_quiz.lower():
            persona.remove_question(comp)
            componente_removido = comp.__class__.__name__
            break
    
    if not componente_removido:
        raise HTTPException(status_code=404, detail="Tipo de quiz não encontrado na persona")
    
    return {
        "message": f"Quiz {componente_removido} removido da persona {nome}",
        "componentes_restantes": [comp.__class__.__name__ for comp in persona.componentes],
        "total_componentes": len(persona.componentes)
    }

@router.get("/personas")
async def listar_personas() -> Dict[str, Any]:
    """
    Lista todas as personas criadas.
    """
    personas_info = {}
    for nome, persona in personas_db.items():
        personas_info[nome] = {
            "componentes": [comp.__class__.__name__ for comp in persona.componentes],
            "total_componentes": len(persona.componentes)
        }
    
    return {
        "total_personas": len(personas_db),
        "personas": personas_info
    }
