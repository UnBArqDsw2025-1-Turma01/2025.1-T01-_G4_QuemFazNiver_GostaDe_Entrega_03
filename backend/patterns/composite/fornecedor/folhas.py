from .fornecedor import Fornecedor

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
