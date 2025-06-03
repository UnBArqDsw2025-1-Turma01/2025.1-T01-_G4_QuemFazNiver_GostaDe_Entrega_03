from abc import ABC, abstractmethod

class Quiz(ABC):
    @abstractmethod
    def montar_quiz(self):
        pass
