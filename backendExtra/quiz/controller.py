from .quiz_terminal import QuizPreferenciasTerminal

def iniciar_quiz(usuario):
    quiz = QuizPreferenciasTerminal()
    quiz.executar_quiz(usuario)

def mostrar_preferencias(usuario):
    print(f"\n🎯 Preferências de {usuario['nome']}:")
    prefs = usuario.get("preferencias")
    if prefs:
        for categoria, opcoes in prefs.items():
            print(f"- {categoria.capitalize()}: {', '.join(opcoes)}")
    else:
        print("❌ Nenhum quiz respondido ainda.")
