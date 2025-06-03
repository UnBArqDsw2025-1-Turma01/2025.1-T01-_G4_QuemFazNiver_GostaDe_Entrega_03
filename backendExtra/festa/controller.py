from .builder import FestaPersonalizadaBuilder, Organizador
from .bridge import TipoConviteFesta, TipoListaPreferencias, ConviteFesta, ListaPreferencias

# Armazenamento em memória
festas_organizadas = {}

def organizar_festa_via_terminal(usuario):
    prefs = usuario.get("preferencias")

    if not prefs or not any(prefs.values()):
        print("⚠️ Esse usuário ainda não respondeu o quiz.")
        return

    builder = FestaPersonalizadaBuilder()
    organizador = Organizador(builder)

    from datetime import date, time

    print("\n🎯 Organizando festa para:", usuario["nome"])
    print("👀 Usaremos as preferências abaixo como base:")

    # Mostrar preferências antes de iniciar
    for categoria, itens in prefs.items():
        print(f"- {categoria.capitalize()}: {', '.join(itens)}")

    print("\n🛠️ Agora complete os dados da festa:")

    nome = usuario["nome"]

    # Local
    local = input("📍 Local da festa: ")

    # Buffet (sugestão com base no quiz)
    print(f"🍴 Sugestão de buffet do aniversariante: {', '.join(prefs.get('comidas', []))}")
    buffet = [x.strip() for x in input("Digite o buffet (ou pressione Enter para usar sugestão): ").split(",")]
    if not buffet[0]:  # Usuário pressionou Enter direto
        buffet = prefs.get("comidas", [])

    # Estilos musicais
    print(f"🎵 Estilos musicais preferidos: {', '.join(prefs.get('musicas', []))}")
    estilos = [x.strip() for x in input("Digite os estilos musicais (ou pressione Enter para usar sugestão): ").split(",")]
    if not estilos[0]:
        estilos = prefs.get("musicas", [])

    # Data
    dia = int(input("📅 Dia da festa (DD): "))
    mes = int(input("Mês (MM): "))
    ano = int(input("Ano (YYYY): "))
    data = date(ano, mes, dia)

    # Hora
    hora_str = input("⏰ Horário (HH:MM): ")
    hora = time.fromisoformat(hora_str)

    # Link
    link = input("🔗 Link do grupo (opcional): ")

    # Construir
    festa = organizador.construirFesta(
        nomeAniversariante=nome,
        local=local,
        buffet=buffet,
        estilosMusicais=estilos,
        data=data,
        hora=hora,
        linkGrupo=link
    )

    festas_organizadas[usuario["id"]] = festa

    print("\n✅ Festa criada com sucesso!\n")

    convite = ConviteFesta(festa, TipoConviteFesta())
    preferencias = ListaPreferencias(festa, TipoListaPreferencias())
    print(convite.gerarConvite())
    print(preferencias.gerarConvite())
    

def mostrar_festa(usuario):
    festa = festas_organizadas.get(usuario["id"])
    if not festa:
        print("⚠️ Nenhuma festa organizada ainda para este usuário.")
        return

    convite = ConviteFesta(festa, TipoConviteFesta())
    preferencias = ListaPreferencias(festa, TipoListaPreferencias())
    print(convite.gerarConvite())
    print(preferencias.gerarConvite())
