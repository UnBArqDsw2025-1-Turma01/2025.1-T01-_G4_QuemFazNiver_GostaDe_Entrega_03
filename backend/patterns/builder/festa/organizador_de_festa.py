from .builder_interface import FestaBuilder
from .festa_organizada import FestaOrganizada

class OrganizadorDeFesta:
    def construirFesta(self, builder: FestaBuilder) -> FestaOrganizada:
        builder.escolherLocalFornecedor()
        builder.selecionarBuffet()
        builder.contratarBanda()
        builder.gerarConvite()
        return builder.getFesta()
