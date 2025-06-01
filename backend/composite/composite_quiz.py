
# para rodar execulte: python3 composite_quiz.py

from abc import ABC, abstractmethod

# Interface Quiz
class Quiz(ABC):
    @abstractmethod
    def montar_quiz(self):
        pass

# --- Leafs (Componentes individuais) ---
class Preferencia(Quiz):
    def montar_quiz(self):
        return "Quiz de Preferência montado."

class Tematica(Quiz):
    def montar_quiz(self):
        return "Quiz de Temática montado."

class Localidade(Quiz):
    def montar_quiz(self):
        return "Quiz de Localidade montado."

class Estilo(Quiz):
    def montar_quiz(self):
        return "Quiz de Estilo montado."

class Comida(Quiz):
    def montar_quiz(self):
        return "Quiz de Comida montado."

# --- Composite (Objeto que pode conter outros objetos Quiz) ---
class Persona(Quiz):
    def __init__(self, nome):
        self.nome = nome
        self.leafArrayList = []  # lista de componentes que implementam 'Quiz'

    def addQuestion(self, componente: Quiz):
        """
        Adiciona um componente (leaf) à lista interna.
        """
        self.leafArrayList.append(componente)

    def removeQuestion(self, componente: Quiz):
        """
        Remove um componente (leaf) da lista interna, se existir.
        """
        if componente in self.leafArrayList:
            self.leafArrayList.remove(componente)

    def montar_quiz(self):
        """
        Percorre todos os componentes (leaves) e invoca 'montar_quiz' em cada um,
        retornando uma lista de resultados.
        """
        resultados = []
        for child in self.leafArrayList:
            resultados.append(child.montar_quiz())
        return resultados

# --- Código de demonstração / saída no terminal ---
if __name__ == "__main__":
    # 1) Criar o composite 'Persona'
    persona = Persona("Usuário Exemplo")
    
    # 2) Instanciar cada leaf
    pref    = Preferencia()
    tema    = Tematica()
    loc     = Localidade()
    estilo  = Estilo()
    comida  = Comida()
    
    # 3) Adicionar as folhas à persona (composite)
    persona.addQuestion(pref)
    persona.addQuestion(tema)
    persona.addQuestion(loc)
    persona.addQuestion(estilo)
    persona.addQuestion(comida)
    
    # 4) Imprimir saída no estilo do terminal
    print("Persona criada pelo Composite:")
    print(f"Nome: {persona.nome}")
    print("Componentes adicionados:")
    for comp in persona.leafArrayList:
        print(f"- {comp.__class__.__name__}")
    
    print("\nMontagem do Quiz:")
    for resultado in persona.montar_quiz():
        print(f"> {resultado}")
