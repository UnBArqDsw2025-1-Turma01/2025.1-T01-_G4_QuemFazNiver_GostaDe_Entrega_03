from .interfaces import FornecedorFactory
from .factories import PizzariaFornecedorFactory, ConfeitariaFornecedorFactory, ChurrascariaFornecedorFactory

def get_fornecedor_factory(tipo: str) -> FornecedorFactory:
    """
    Factory Provider - Simplifica a criação da fábrica correta
    
    Args:
        tipo: Tipo de fornecedor ("pizzaria", "confeitaria", "churrascaria")
        
    Returns:
        FornecedorFactory: Instância da fábrica apropriada
        
    Raises:
        ValueError: Se o tipo de fornecedor não for suportado
    """
    factories = {
        "pizzaria": PizzariaFornecedorFactory(),
        "confeitaria": ConfeitariaFornecedorFactory(),
        "churrascaria": ChurrascariaFornecedorFactory()
    }
    
    factory = factories.get(tipo.lower())
    if not factory:
        raise ValueError(f"Tipo de fornecedor não suportado: {tipo}")
    
    return factory
