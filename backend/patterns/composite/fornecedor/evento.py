from .fornecedor import Fornecedor

class Evento(Fornecedor):
    def __init__(self, nome: str):
        self.nome = nome
        self.fornecedores = []

    def add(self, componente: Fornecedor):
        self.fornecedores.append(componente)

    def remove(self, componente: Fornecedor):
        if componente in self.fornecedores:
            self.fornecedores.remove(componente)

    def montar_evento(self):
        return [f.montar_evento() for f in self.fornecedores]

    def calcular_evento(self):
        return f"Total de fornecedores que participam do evento: {len(self.fornecedores)}"
