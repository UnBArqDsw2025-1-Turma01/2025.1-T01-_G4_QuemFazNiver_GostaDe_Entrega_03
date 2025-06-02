from datetime import date, time
from builder import FestaPersonalizadaBuilder, Organizador
from festaUtils import FestaUtils

# Criar o builder
builder = FestaPersonalizadaBuilder()

# Criar o director (Organizador)
organizador = Organizador(builder)

# Dados da festa inserido pelo usuário
nome_aniversariante = input("Digite o nome do aniversariante: ")
local = input("Digite o local da festa: ")
buffet = [item.strip() for item in input("Digite os itens do buffet (separados por vírgula): ").split(",")]
estilos_musicais = [item.strip() for item in input("Digite os estilos musicais (separados por vírgula): ").split(",")]

# Solicita dia, mês e ano separadamente
dia = int(input("Digite o dia da festa (DD): "))
mes = int(input("Digite o mês da festa (MM): "))
ano = int(input("Digite o ano da festa (YYYY): "))
data = date(ano, mes, dia)  # Criar a data a partir dos valores fornecidos

# Solicita a hora no formato HH:MM
hora_input = input("Digite o horário da festa (formato HH:MM): ")
hora = time.fromisoformat(hora_input)

# Solicita o link do grupo
link_grupo = input("Digite o link do grupo (opcional): ")

# Construir a festa
festa = organizador.construirFesta(
    nomeAniversariante=nome_aniversariante,
    local=local,
    buffet=buffet,
    estilosMusicais=estilos_musicais,
    data=data,
    hora=hora,
    linkGrupo=link_grupo
)

# Gerar o convite
convite = FestaUtils.gerarConvite(festa)
print(convite)

# Gerar as preferências
preferencias = FestaUtils.gerarPreferencias(festa)
print(preferencias)