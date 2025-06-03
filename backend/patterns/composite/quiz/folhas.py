from .base import Quiz

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
