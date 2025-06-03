from abc import ABC, abstractmethod

class Portifolio(ABC):
    def __init__(self, titulo: str, descricao: str, valores: float, funcionamento: str):
        self.titulo = titulo
        self.descricao = descricao
        self.valores = valores
        self.funcionamento = funcionamento

    def gerar_portifolio(self) -> dict:
        self._preparar_titulo()
        self._adicionar_funcionamento()
        self._adicionar_valores()
        descricao_customizada = self.criar_descricao_geral()
        return self._criar_portifolio_final(descricao_customizada)

    def _preparar_titulo(self):
        print(f"Título do Portfólio: {self.titulo}")

    def _adicionar_funcionamento(self):
        print(f"Funcionamento: {self.funcionamento}")

    def _adicionar_valores(self):
        print(f"Valores a partir de: R${self.valores:.2f}")

    def _criar_portifolio_final(self, descricao: str) -> dict:
        return {
            "titulo": self.titulo,
            "descricao_completa": descricao,
            "valores": self.valores,
            "funcionamento": self.funcionamento
        }

    @abstractmethod
    def criar_descricao_geral(self) -> str:
        pass



