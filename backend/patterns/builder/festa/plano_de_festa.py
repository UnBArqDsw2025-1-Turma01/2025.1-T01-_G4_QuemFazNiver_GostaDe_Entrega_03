from typing import List
from datetime import date

class PlanoDeFesta:
    def __init__(
        self,
        buffetEscolhidas: List[str],
        bandaEscolhida: str,
        nomeAniversariante: str,
        data: date,
        horario: str,
        localFornecedor: str
    ):
        self.buffetEscolhidas = buffetEscolhidas
        self.bandaEscolhida = bandaEscolhida
        self.nomeAniversariante = nomeAniversariante
        self.data = data
        self.horario = horario
        self.localFornecedor = localFornecedor
