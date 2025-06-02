from typing import List, Optional
from datetime import date

class FestaOrganizada:
    def __init__(
        self,
        nomeAniversariante: str,
        data: date,
        horario: str,
        localFornecedor: str,
        buffet: List[str],
        banda: str,
        linkWhatsapp: Optional[str] = None,
        convite: Optional[str] = None
    ):
        self.nomeAniversariante = nomeAniversariante
        self.data = data
        self.horario = horario
        self.localFornecedor = localFornecedor
        self.buffet = buffet
        self.banda = banda
        self.linkWhatsapp = linkWhatsapp
        self.convite = convite
