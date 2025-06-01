"""
Este script testa o padrão Template Method implementado nas classes de portfólio.

O padrão Template Method define o esqueleto de um algoritmo em um método na classe base,
mas permite que as subclasses modifiquem partes específicas do algoritmo sem alterar sua estrutura.

Neste caso:
- A classe base 'Portifolio' define o método 'gerar_portifolio' (o template method)
- As subclasses (PortifolioBuffet, PortifolioFotografia, PortifolioConfeitaria) 
  implementam o método abstrato 'criar_descricao_geral' que é chamado pelo template method.
"""

from portifolio_template import Portifolio
from portifolio_buffet import PortifolioBuffet
from portifolio_fotografia import PortifolioFotografia
from portifolio_confeitaria import PortifolioConfeitaria

def print_divider(title):
    print("\n" + "="*50)
    print(f"   {title}")
    print("="*50)

def print_portfolio(portfolio_type, portfolio_obj):
    print_divider(f"Portfolio de {portfolio_type}")
    
    print("\nResultado do portfólio gerado:")
    portfolio_result = portfolio_obj.gerar_portifolio()
    
    for key, value in portfolio_result.items():
        print(f"  {key}: {value}")

def main():
    print_divider("DEMONSTRAÇÃO DO PADRÃO TEMPLATE METHOD")
    print("Testando as implementações concretas que usam o Template Method\n")
    
    # Exemplo de Buffet
    buffet = PortifolioBuffet(
        titulo="Buffet Delícia Festiva",
        descricao="Especialistas em festas infantis e corporativas.",
        valores=1500.00,
        funcionamento="Segunda a Sábado, 9h às 21h",
        tipo_evento="Aniversários, Casamentos, Formaturas",
        cardapio_pratos=["Salgados variados", "Mini pizza", "Risoto de funghi", "Filé ao molho madeira"]
    )
    print_portfolio("Buffet", buffet)
    
    # Exemplo de Fotografia
    fotografia = PortifolioFotografia(
        titulo="Fotografias Momentos Especiais",
        descricao="Captando momentos únicos com qualidade e emoção.",
        valores=800.00,
        funcionamento="Todos os dias mediante agendamento",
        estilo_fotografia="Contemporâneo, Minimalista, Editorial",
        amostras_fotos=["https://exemplo.com/foto1", "https://exemplo.com/foto2"]
    )
    print_portfolio("Fotografia", fotografia)
    
    # Exemplo de Confeitaria
    confeitaria = PortifolioConfeitaria(
        titulo="Doçuras Encantadas",
        descricao="Doces artesanais para todas as ocasiões",
        valores=500.00,
        funcionamento="Terça a Domingo, 10h às 18h",
        tipo_doce=["Brigadeiros gourmet", "Bolos decorados", "Cupcakes"],
        cardapio_doces=["Brigadeiro tradicional", "Cajuzinho", "Bem-casado"],
        cardapio_restricoes=["Sem glúten", "Sem lactose", "Diet", "Vegano"]
    )
    print_portfolio("Confeitaria", confeitaria)

if __name__ == "__main__":
    main()
