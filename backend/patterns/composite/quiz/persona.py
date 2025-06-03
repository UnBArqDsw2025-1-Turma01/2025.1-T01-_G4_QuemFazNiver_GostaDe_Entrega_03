from .base import Quiz

class Persona(Quiz):
    def __init__(self, nome):
        self.nome = nome
        self.componentes = []

    def add_question(self, componente: Quiz):
        self.componentes.append(componente)

    def remove_question(self, componente: Quiz):
        if componente in self.componentes:
            self.componentes.remove(componente)

    def montar_quiz(self):
        return [comp.montar_quiz() for comp in self.componentes]
