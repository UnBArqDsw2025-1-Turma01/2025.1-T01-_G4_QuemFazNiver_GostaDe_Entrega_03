from abc import ABC, abstractmethod

class Fornecedor(ABC):
    @abstractmethod
    def montar_evento(self):
        pass
