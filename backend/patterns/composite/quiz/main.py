from persona import Persona
from folhas import Preferencia, Tematica, Localidade, Estilo, Comida

if __name__ == "__main__":
    persona = Persona("Usuário Exemplo")

    # Criar componentes (folhas)
    pref    = Preferencia()
    tema    = Tematica()
    loc     = Localidade()
    estilo  = Estilo()
    comida  = Comida()

    # Adicionar componentes ao composite
    persona.add_question(pref)
    persona.add_question(tema)
    persona.add_question(loc)
    persona.add_question(estilo)
    persona.add_question(comida)

    # Exibir informações
    print("Persona criada pelo Composite:")
    print(f"Nome: {persona.nome}")
    print("Componentes adicionados:")
    for comp in persona.componentes:
        print(f"- {comp.__class__.__name__}")

    print("\nMontagem do Quiz:")
    for resultado in persona.montar_quiz():
        print(f"> {resultado}")
