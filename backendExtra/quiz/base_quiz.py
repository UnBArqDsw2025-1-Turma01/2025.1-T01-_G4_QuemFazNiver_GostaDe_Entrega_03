from abc import ABC, abstractmethod

class QuizTemplate(ABC):
    def executar_quiz(self, usuario):
        self.boas_vindas()
        respostas = self.fazer_perguntas()
        self.salvar_preferencias(usuario, respostas)
        self.finalizar()

    def boas_vindas(self):
        print("\n🎉 Bem-vindo ao quiz de preferências para sua festa!")

    @abstractmethod
    def fazer_perguntas(self):
        pass

    @abstractmethod
    def salvar_preferencias(self, usuario, respostas):
        pass

    def finalizar(self):
        print("✅ Preferências salvas com sucesso!\n")