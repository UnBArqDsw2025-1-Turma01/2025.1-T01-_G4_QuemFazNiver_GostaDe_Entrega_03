from evento import Evento
from folhas import Banda, LocacaoLocal, Seguranca, Decoracao, Comida

if __name__ == "__main__":
    evento = Evento("Festa de Aniversário")
    evento.add(Banda())
    evento.add(LocacaoLocal())
    evento.add(Seguranca())
    evento.add(Decoracao())
    evento.add(Comida())

    print("Evento criado pelo Composite:")
    print(f"Nome: {evento.nome}")
    print("Fornecedores adicionados:")
    for fornecedor in evento.fornecedores:
        print(f"- {fornecedor.__class__.__name__}")

    print("\nMontagem do Evento:")
    for resultado in evento.montar_evento():
        print(f"> {resultado}")

    print("\nCálculo do Evento:")
    print(f"> {evento.calcular_evento()}")