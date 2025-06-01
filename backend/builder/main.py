from datetime import date
from builder import PlanoDeFesta, FestaPersonalizadaBuilder, OrganizadorDeFesta

# Exemplo de plano de festa
plano = PlanoDeFesta(
    buffetEscolhidas=["Buffet Kids", "Buffet Gourmet"],
    bandaEscolhida="Banda da Felicidade",
    nomeAniversariante="Bruno",
    data=date(2025, 6, 12),
    horario="19:00",
    localFornecedor="Central Festas JK"
)

# Cria o builder e o organizador
builder = FestaPersonalizadaBuilder(plano)
organizador = OrganizadorDeFesta()

# Constrói a festa
festa = organizador.construirFesta(builder)

# Exibe o resultado das opções "escolhidas"
print("Festa organizada:")
print(f"Aniversariante: {festa.nomeAniversariante}")
print(f"Data: {festa.data}")
print(f"Horário: {festa.horario}")
print(f"Local: {festa.localFornecedor}")
print(f"Buffet: {', '.join(festa.buffet)}")
print(f"Banda: {festa.banda}")
print(f"Convite WhatsApp: {festa.linkWhatsapp}")
print(f"Convite: {festa.convite}") # Simula o convite, não temos um front com o convite