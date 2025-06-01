from abc import ABC, abstractmethod

# Interface Fornecedor
class Fornecedor(ABC):
    @abstractmethod
    def montar_evento(self):
        """
        Método que cada componente (folha) implementa para 'montar' a sua parte do evento.
        """
        pass

# --- Folhas (Componentes individuais) ---
class Banda(Fornecedor):
    def montar_evento(self):
        return "Banda: Montando a estrutura de som e iluminação do show."

class LocacaoLocal(Fornecedor):
    def montar_evento(self):
        return "LocaçãoLocal: Reservando e preparando o espaço para o evento."

class Seguranca(Fornecedor):
    def montar_evento(self):
        return "Segurança: Organizando a equipe e equipamentos de segurança."

class Decoracao(Fornecedor):
    def montar_evento(self):
        return "Decoração: Instalando decoração e ambientação do local."

class Comida(Fornecedor):
    def montar_evento(self):
        return "Comida: Receita e logística de buffet e catering."

# --- Composite (Objeto que pode agrupar múltiplos Fornecedores) ---
class Evento(Fornecedor):
    def __init__(self, nome: str):
        self.nome = nome
        self.leafArrayList = []  # lista de Fornecedores que compõem o evento

    def addEvento(self, componente: Fornecedor):
        """
        Adiciona um fornecedor (folha) ao evento.
        """
        self.leafArrayList.append(componente)

    def removeEvento(self, componente: Fornecedor):
        """
        Remove um fornecedor (folha) do evento, se estiver presente.
        """
        if componente in self.leafArrayList:
            self.leafArrayList.remove(componente)

    def montar_evento(self):
        """
        Para cada fornecedor adicionado, chama seu montar_evento() e retorna a lista de resultados.
        """
        resultados = []
        for child in self.leafArrayList:
            resultados.append(child.montar_evento())
        return resultados

    def calcular_evento(self):
        """
        Exemplo de cálculo agregado: retorna o número de fornecedores que participam do evento.
        """
        total = len(self.leafArrayList)
        return f"Total de fornecedores que participam do evento: {total}"

# --- Demonstração de uso e saída no estilo terminal ---
if __name__ == "__main__":
    # 1) Criar o composite 'Evento'
    evento = Evento("Festa de Aniversário")

    # 2) Instanciar cada folha (Fornecedor)
    banda       = Banda()
    local       = LocacaoLocal()
    seguranca   = Seguranca()
    decoracao   = Decoracao()
    comida      = Comida()

    # 3) Adicionar as folhas ao evento (composite)
    evento.addEvento(banda)
    evento.addEvento(local)
    evento.addEvento(seguranca)
    evento.addEvento(decoracao)
    evento.addEvento(comida)

    # 4) Imprimir saída no estilo do terminal
    print("Evento criado pelo Composite:")
    print(f"Nome: {evento.nome}")
    print("Fornecedores adicionados:")
    for comp in evento.leafArrayList:
        print(f"- {comp.__class__.__name__}")

    print("\nMontagem do Evento:")
    for resultado in evento.montar_evento():
        print(f"> {resultado}")

    print("\nCálculo do Evento:")
    print(f"> {evento.calcular_evento()}")
