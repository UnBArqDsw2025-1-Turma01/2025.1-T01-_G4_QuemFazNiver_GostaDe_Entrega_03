import sys
import os
from datetime import date, datetime
from typing import List, Dict, Optional
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.usuario import Usuario
from models.perfil import Perfil
from models.endereco import Endereco
from models.quiz import Quiz, Pergunta, Opcao
from patterns.composite.quiz.persona import Persona
from patterns.composite.quiz.folhas import Preferencia, Tematica, Localidade, Estilo, Comida
from patterns.factory_method.fornecedor.provider import get_fornecedor_factory
from patterns.template_method.portifolio_buffet import PortifolioBuffet
from patterns.template_method.portifolio_confeitaria import PortifolioConfeitaria
from patterns.builder.festa import FestaBasicaBuilder, FestaPersonalizadaBuilder, OrganizadorDeFesta, PlanoDeFesta
from patterns.composite.fornecedor.evento import Evento
from patterns.composite.fornecedor.folhas import Banda, LocacaoLocal, Seguranca, Decoracao, Comida
from patterns.decorator.convite.convite_concreto import ConviteConcreto, TemplateDefault
from patterns.decorator.convite.decorator_interativo import DecoratorInterativo
from patterns.decorator.convite.decorator_luxo import DecoratorLuxo

class SistemaLogin:
    def __init__(self):
        self.usuarios_login: Dict[str, Dict] = {}  
        self.usuario_logado: Optional[Usuario] = None
        self.quiz_realizado: bool = False
        self.fornecedores_selecionados: bool = False
        self.buffet_selecionado: bool = False
        self.festa_criada: bool = False
        self.evento_organizado: bool = False
        self.convites_criados: bool = False
        
    def criar_credenciais(self, usuario: Usuario) -> Dict[str, str]:
        """Cria credenciais de login para um usuário"""
        username = usuario.nome.split()[0].lower()
        
        base_username = username
        counter = 1
        while username in self.usuarios_login:
            username = f"{base_username}{counter}"
            counter += 1
        
        password = f"{usuario.nome.split()[0].lower()}{usuario.dataNascimento.year}"

        self.usuarios_login[username] = {
            'password': password,
            'usuario': usuario
        }
        
        return {'username': username, 'password': password}
    
    def fazer_login(self, username: str, password: str) -> bool:
        """Realiza login do usuário"""
        if username in self.usuarios_login:
            if self.usuarios_login[username]['password'] == password:
                self.usuario_logado = self.usuarios_login[username]['usuario']
                self.quiz_realizado = False  
                self.fornecedores_selecionados = False  
                self.buffet_selecionado = False  
                self.festa_criada = False  
                self.evento_organizado = False  
                return True
        return False
    
    def fazer_logout(self):
        """Realiza logout do usuário"""
        self.usuario_logado = None
        self.quiz_realizado = False
        self.fornecedores_selecionados = False
        self.buffet_selecionado = False
        self.festa_criada = False
        self.evento_organizado = False
        self.convites_criados = False

    def esta_logado(self) -> bool:
        """Verifica se há usuário logado"""
        return self.usuario_logado is not None

sistema_login = SistemaLogin()

def criar_quiz_com_composite():
    """Cria um quiz usando o padrão Composite"""
    print("\n" + "="*50)
    print("    QUIZ DE PERSONALIDADE PARA FESTAS")
    print("    (Usando Padrão Composite)")
    print("="*50)
    print("Vamos montar seu perfil personalizado!")
    print()
    
    usuario = sistema_login.usuario_logado
    persona = Persona(f"Persona_{usuario.nome}")
    
    tipos_quiz = {
        "1": ("Preferências Gerais", Preferencia()),
        "2": ("Temática de Festa", Tematica()),
        "3": ("Localidade Preferida", Localidade()),
        "4": ("Estilo de Evento", Estilo()),
        "5": ("Preferências Culinárias", Comida())
    }
    
    print("Escolha os tipos de quiz que deseja responder:")
    for key, (nome, _) in tipos_quiz.items():
        print(f"{key}. {nome}")
    
    print("\nDigite os números separados por vírgula (ex: 1,2,3):")
    escolhas = input("Sua escolha: ").split(',')
    
    componentes_adicionados = []
    for escolha in escolhas:
        escolha = escolha.strip()
        if escolha in tipos_quiz:
            nome_componente, componente = tipos_quiz[escolha]
            persona.add_question(componente)
            componentes_adicionados.append(nome_componente)
    
    if not componentes_adicionados:
        print("ERRO: Nenhum quiz válido selecionado!")
        return False
    
    print(f"\nQuiz montado com os componentes: {', '.join(componentes_adicionados)}")
    
    print("\nExecutando quiz composite...")
    resultados_quiz = persona.montar_quiz()
    
    for i, resultado in enumerate(resultados_quiz, 1):
        print(f"{i}. {resultado}")
    
    tags_coletadas = []
    
    if any("Preferencia" in comp.__class__.__name__ for comp in persona.componentes):
        tags_coletadas.extend(["personalizado", "preferencias"])
    
    if any("Tematica" in comp.__class__.__name__ for comp in persona.componentes):
        tags_coletadas.extend(["tematico", "criativo"])
    
    if any("Localidade" in comp.__class__.__name__ for comp in persona.componentes):
        tags_coletadas.extend(["local-especifico", "ambiente"])
    
    if any("Estilo" in comp.__class__.__name__ for comp in persona.componentes):
        tags_coletadas.extend(["estiloso", "design"])
    
    if any("Comida" in comp.__class__.__name__ for comp in persona.componentes):
        tags_coletadas.extend(["gastronomia", "culinaria"])
    
    print("\n" + "="*50)
    print("PERGUNTAS PERSONALIZADAS")
    print("="*50)
    
    for componente in persona.componentes:
        resultado_pergunta = fazer_pergunta_por_componente(componente)
        if resultado_pergunta:
            tags_coletadas.extend(resultado_pergunta)
    
    atualizar_perfil_com_composite(tags_coletadas, len(persona.componentes))
    
    return True

def fazer_pergunta_por_componente(componente):
    """Faz perguntas específicas baseadas no tipo de componente"""
    tipo = componente.__class__.__name__
    
    if tipo == "Preferencia":
        print("\nQUIZ DE PREFERÊNCIAS")
        print("1. Festas íntimas e familiares")
        print("2. Festas grandes e sociais")
        print("3. Festas temáticas")
        print("4. Festas casuais")
        
        escolha = input("Sua preferência (1-4): ")
        opcoes = {
            "1": ["intimo", "familiar"],
            "2": ["social", "grande"],
            "3": ["tematico", "criativo"],
            "4": ["casual", "descontraido"]
        }
        return opcoes.get(escolha, ["personalizado"])
    
    elif tipo == "Tematica":
        print("\nQUIZ DE TEMÁTICA")
        print("1. Temas clássicos (elegante, formal)")
        print("2. Temas modernos (contemporâneo, tecnológico)")
        print("3. Temas divertidos (colorido, animado)")
        print("4. Temas naturais (rústico, outdoor)")
        
        escolha = input("Sua preferência (1-4): ")
        opcoes = {
            "1": ["classico", "elegante", "formal"],
            "2": ["moderno", "contemporaneo"],
            "3": ["divertido", "colorido", "animado"],
            "4": ["natural", "rustico", "outdoor"]
        }
        return opcoes.get(escolha, ["tematico"])
    
    elif tipo == "Localidade":
        print("\nQUIZ DE LOCALIDADE")
        print("1. Em casa ou residência")
        print("2. Salão de festas")
        print("3. Espaços ao ar livre")
        print("4. Locais inusitados")
        
        escolha = input("Sua preferência (1-4): ")
        opcoes = {
            "1": ["casa", "residencial", "familiar"],
            "2": ["salao", "tradicional", "formal"],
            "3": ["outdoor", "natureza", "ar-livre"],
            "4": ["inusitado", "criativo", "diferente"]
        }
        return opcoes.get(escolha, ["localidade"])
    
    elif tipo == "Estilo":
        print("\nQUIZ DE ESTILO")
        print("1. Estilo minimalista")
        print("2. Estilo luxuoso")
        print("3. Estilo vintage")
        print("4. Estilo moderno")
        
        escolha = input("Sua preferência (1-4): ")
        opcoes = {
            "1": ["minimalista", "clean", "simples"],
            "2": ["luxuoso", "sofisticado", "premium"],
            "3": ["vintage", "retrô", "clássico"],
            "4": ["moderno", "contemporâneo", "atual"]
        }
        return opcoes.get(escolha, ["estilo"])
    
    elif tipo == "Comida":
        print("\nQUIZ DE CULINÁRIA")
        print("1. Buffet completo")
        print("2. Finger food")
        print("3. Churrasco")
        print("4. Doces e confeitaria")
        
        escolha = input("Sua preferência (1-4): ")
        opcoes = {
            "1": ["buffet", "completo", "variado"],
            "2": ["finger-food", "elegante", "prático"],
            "3": ["churrasco", "informal", "tradicional"],
            "4": ["doces", "confeitaria", "sobremesas"]
        }
        return opcoes.get(escolha, ["culinaria"])
    
    return ["composite"]

def atualizar_perfil_com_composite(tags_coletadas, num_componentes):
    """Atualiza o perfil do usuário com dados do quiz composite"""
    usuario = sistema_login.usuario_logado
    
    tags_unicas = list(set(tags_coletadas + usuario.tagsDePreferencias))
    usuario.tagsDePreferencias = tags_unicas
    
    if not usuario.perfil:
        usuario.perfil = Perfil(
            biografia=f"Perfil criado via Quiz Composite com {num_componentes} componentes. Preferências: {', '.join(tags_coletadas[:3])}",
            interesses=tags_unicas,
            visibilidade="publico",
            quiz_realizado=True
        )
    else:
        usuario.perfil.interesses = tags_unicas
        usuario.perfil.quiz_realizado = True
        usuario.perfil.biografia = f"Perfil atualizado via Quiz Composite. Componentes utilizados: {num_componentes}"
    
    sistema_login.quiz_realizado = True
    
    print(f"\nQuiz Composite finalizado!")
    print(f"Componentes utilizados: {num_componentes}")
    print(f"Tags coletadas: {', '.join(tags_coletadas)}")
    print("Perfil personalizado criado com sucesso!")

def realizar_quiz():
    """Função principal para realizar quiz - agora usando Composite"""
    return criar_quiz_com_composite()

def fazer_login():
    """Função para realizar login"""
    print("\n=== LOGIN ===")
    print()
    
    username = input("Username: ")
    password = input("Password: ")
    
    if sistema_login.fazer_login(username, password):
        print(f"\nLogin realizado com sucesso!")
        print(f"Bem-vindo(a), {sistema_login.usuario_logado.nome}!")
        return True
    else:
        print("\nERRO: Username ou password incorretos!")
        return False

def selecionar_fornecedores_com_factory():
    """Sistema de seleção de fornecedores usando Factory Method"""
    print("\n" + "="*60)
    print("    SELEÇÃO DE FORNECEDORES PARA SUA FESTA")
    print("    (Usando Padrão Factory Method)")
    print("="*60)
    print("Com base no seu perfil, vamos selecionar fornecedores!")
    print()
    
    usuario = sistema_login.usuario_logado
    fornecedores_selecionados = []
    
    tipos_fornecedores = {
        "1": ("Pizzaria", "pizzaria"),
        "2": ("Confeitaria", "confeitaria"), 
        "3": ("Churrascaria", "churrascaria")
    }
    
    print("Tipos de fornecedores disponíveis:")
    for key, (nome, _) in tipos_fornecedores.items():
        print(f"{key}. {nome}")
    
    print("\nDigite os números dos fornecedores que deseja contratar (separados por vírgula):")
    print("Ex: 1,2 para Pizzaria e Confeitaria")
    escolhas = input("Sua escolha: ").split(',')
    
    for escolha in escolhas:
        escolha = escolha.strip()
        if escolha in tipos_fornecedores:
            nome_tipo, tipo = tipos_fornecedores[escolha]
            
            print(f"\nConfigurando {nome_tipo}...")
            fornecedor_info = configurar_fornecedor_com_factory(tipo, nome_tipo)
            
            if fornecedor_info:
                fornecedores_selecionados.append(fornecedor_info)
                print(f"{nome_tipo} adicionado com sucesso!")
    
    if not fornecedores_selecionados:
        print("ERRO: Nenhum fornecedor válido selecionado!")
        return False
    
    salvar_fornecedores_no_perfil(fornecedores_selecionados)
    
    return True

def configurar_fornecedor_com_factory(tipo_fornecedor: str, nome_tipo: str):
    try:
        factory = get_fornecedor_factory(tipo_fornecedor)
        
        print(f"\nConfiguração do {nome_tipo}:")
        nome = input(f"Nome do {nome_tipo}: ")
        
        tags_sugeridas = {
            "pizzaria": ["pizza", "italiana", "delivery", "massa"],
            "confeitaria": ["bolos", "doces", "festa", "personalizado"],
            "churrascaria": ["churrasco", "carnes", "espetos", "tradicional"]
        }
        
        print(f"Tags sugeridas: {', '.join(tags_sugeridas.get(tipo_fornecedor, []))}")
        tags_input = input("Tags personalizadas (separadas por vírgula, ou Enter para usar sugeridas): ")
        
        if tags_input.strip():
            tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
        else:
            tags = tags_sugeridas.get(tipo_fornecedor, [])
        
        contato = input("Contato (telefone/email): ")
        portfolio = input("Descrição do portfólio (opcional): ")
        
        fornecedor_obj = factory.create_fornecedor(
            nome=nome,
            tags=tags,
            contato=contato,
            portfolio=portfolio if portfolio.strip() else None
        )
        
        print(f"\nResumo do {nome_tipo}:")
        print(f"- {fornecedor_obj.exibir_info()}")
        print(f"- Preço estimado: R$ {fornecedor_obj.calcular_preco():.2f}")
        print(f"- Serviços: {', '.join(fornecedor_obj.listar_servicos())}")
        
        return {
            "tipo": tipo_fornecedor,
            "nome": fornecedor_obj.nome,
            "tags": fornecedor_obj.tags,
            "contato": fornecedor_obj.contato,
            "portfolio": fornecedor_obj.portfolio,
            "preco_estimado": fornecedor_obj.calcular_preco(),
            "servicos": fornecedor_obj.listar_servicos(),
            "informacoes": fornecedor_obj.exibir_info()
        }
        
    except ValueError as e:
        print(f"ERRO ao criar fornecedor: {e}")
        return None
    except Exception as e:
        print(f"ERRO inesperado: {e}")
        return None

def salvar_fornecedores_no_perfil(fornecedores):
    """Salva os fornecedores selecionados no perfil do usuário"""
    usuario = sistema_login.usuario_logado
    
    tags_fornecedores = []
    for fornecedor in fornecedores:
        tags_fornecedores.extend(fornecedor["tags"])
    
    tags_unicas = list(set(usuario.tagsDePreferencias + tags_fornecedores))
    usuario.tagsDePreferencias = tags_unicas
    
    if not usuario.perfil:
        usuario.perfil = Perfil(
            biografia=f"Usuário com {len(fornecedores)} fornecedores selecionados",
            interesses=tags_unicas,
            visibilidade="publico",
            fornecedores_contratados=fornecedores
        )
    else:
        usuario.perfil.interesses = tags_unicas
        usuario.perfil.fornecedores_contratados = fornecedores
    
    sistema_login.fornecedores_selecionados = True
    
    print(f"\nFornecedores salvos no perfil!")
    print(f"Total de fornecedores: {len(fornecedores)}")
    print(f"Tags atualizadas: {', '.join(tags_fornecedores)}")

def selecionar_buffet_com_template_method():
    """Sistema de seleção de buffet usando Template Method"""
    print("\n" + "="*60)
    print("    SELEÇÃO DE BUFFET PARA SUA FESTA")
    print("    (Usando Padrão Template Method)")
    print("="*60)
    print("Vamos criar um portfólio personalizado para seu buffet!")
    print()
    
    usuario = sistema_login.usuario_logado
    
    tipos_buffet = {
        "1": ("Buffet Tradicional", "buffet"),
        "2": ("Confeitaria Especializada", "confeitaria")
    }
    
    print("Tipos de buffet disponíveis:")
    for key, (nome, _) in tipos_buffet.items():
        print(f"{key}. {nome}")
    
    while True:
        escolha = input("\nEscolha o tipo de buffet (1-2): ").strip()
        if escolha in tipos_buffet:
            nome_tipo, tipo = tipos_buffet[escolha]
            break
        else:
            print("ERRO: Escolha inválida! Digite 1 ou 2.")
    
    print(f"\nConfigurando {nome_tipo}...")
    
    if tipo == "buffet":
        buffet_info = configurar_buffet_tradicional()
    else: 
        buffet_info = configurar_confeitaria_especializada()
    
    if buffet_info:
        salvar_buffet_no_perfil(buffet_info)
        return True
    
    return False

def configurar_buffet_tradicional():
    """Configura buffet tradicional usando Template Method"""
    print("\nConfiguração do Buffet Tradicional:")
    
    titulo = input("Título do buffet: ")
    descricao = input("Descrição geral: ")
    
    while True:
        try:
            valores = float(input("Valor base (R$): "))
            break
        except ValueError:
            print("ERRO: Digite um valor numérico válido!")
    
    funcionamento = input("Horário de funcionamento: ")
    tipo_evento = input("Tipo de evento atendido: ")
    
    print("\nDigite os pratos do cardápio (separados por vírgula):")
    cardapio_input = input("Ex: Lasanha, Frango assado, Salada: ")
    cardapio_pratos = [prato.strip() for prato in cardapio_input.split(',') if prato.strip()]
    
    try:
        portifolio_buffet = PortifolioBuffet(
            titulo=titulo,
            descricao=descricao,
            valores=valores,
            funcionamento=funcionamento,
            tipo_evento=tipo_evento,
            cardapio_pratos=cardapio_pratos
        )
        
        portifolio_gerado = portifolio_buffet.gerar_portifolio()
        
        print(f"\nPortfólio do Buffet criado:")
        print(f"- Título: {portifolio_gerado['titulo']}")
        print(f"- Descrição: {portifolio_gerado['descricao_completa']}")
        print(f"- Valores: R$ {portifolio_gerado['valores']}")
        print(f"- Funcionamento: {portifolio_gerado['funcionamento']}")
        
        return {
            "tipo": "buffet_tradicional",
            "titulo": titulo,
            "portifolio": portifolio_gerado,
            "cardapio_pratos": cardapio_pratos,
            "tipo_evento": tipo_evento,
            "valor_base": valores
        }
        
    except Exception as e:
        print(f"ERRO ao criar portfólio do buffet: {e}")
        return None

def configurar_confeitaria_especializada():
    """Configura confeitaria especializada usando Template Method"""
    print("\nConfiguração da Confeitaria Especializada:")
    

    titulo = input("Título da confeitaria: ")
    descricao = input("Descrição geral: ")
    
    while True:
        try:
            valores = float(input("Valor base (R$): "))
            break
        except ValueError:
            print("ERRO: Digite um valor numérico válido!")
    
    funcionamento = input("Horário de funcionamento: ")
    
  
    print("\nTipos de doces oferecidos (separados por vírgula):")
    tipos_input = input("Ex: Bolos, Tortas, Docinhos: ")
    tipo_doce = [tipo.strip() for tipo in tipos_input.split(',') if tipo.strip()]
    
    print("\nCardápio de doces (separados por vírgula):")
    doces_input = input("Ex: Brigadeiro, Beijinho, Trufa: ")
    cardapio_doces = [doce.strip() for doce in doces_input.split(',') if doce.strip()]
    
    print("\nOpções para restrições alimentares (separados por vírgula):")
    restricoes_input = input("Ex: Sem glúten, Sem lactose, Vegano: ")
    cardapio_restricoes = [restricao.strip() for restricao in restricoes_input.split(',') if restricao.strip()]
    

    try:
        portifolio_confeitaria = PortifolioConfeitaria(
            titulo=titulo,
            descricao=descricao,
            valores=valores,
            funcionamento=funcionamento,
            tipo_doce=tipo_doce,
            cardapio_doces=cardapio_doces,
            cardapio_restricoes=cardapio_restricoes
        )
        
        portifolio_gerado = portifolio_confeitaria.gerar_portifolio()
        
        print(f"\nPortfólio da Confeitaria criado:")
        print(f"- Título: {portifolio_gerado['titulo']}")
        print(f"- Descrição: {portifolio_gerado['descricao_completa']}")
        print(f"- Valores: R$ {portifolio_gerado['valores']}")
        print(f"- Funcionamento: {portifolio_gerado['funcionamento']}")
        
        return {
            "tipo": "confeitaria_especializada",
            "titulo": titulo,
            "portifolio": portifolio_gerado,
            "tipo_doce": tipo_doce,
            "cardapio_doces": cardapio_doces,
            "cardapio_restricoes": cardapio_restricoes,
            "valor_base": valores
        }
        
    except Exception as e:
        print(f"ERRO ao criar portfólio da confeitaria: {e}")
        return None

def salvar_buffet_no_perfil(buffet_info):
    """Salva o buffet selecionado no perfil do usuário"""
    usuario = sistema_login.usuario_logado
    
    tags_buffet = ["buffet", "gastronomia"]
    if buffet_info["tipo"] == "confeitaria_especializada":
        tags_buffet.extend(["confeitaria", "doces"])
    else:
        tags_buffet.extend(["refeicoes", "tradicional"])
    
    tags_unicas = list(set(usuario.tagsDePreferencias + tags_buffet))
    usuario.tagsDePreferencias = tags_unicas
    

    if not usuario.perfil:
        usuario.perfil = Perfil(
            biografia=f"Usuário com buffet {buffet_info['tipo']} selecionado",
            interesses=tags_unicas,
            visibilidade="publico",
            buffet_contratado=buffet_info
        )
    else:
        usuario.perfil.interesses = tags_unicas
        usuario.perfil.buffet_contratado = buffet_info
    
    sistema_login.buffet_selecionado = True
    
    print(f"\nBuffet salvo no perfil!")
    print(f"Tipo: {buffet_info['tipo']}")
    print(f"Título: {buffet_info['titulo']}")
    print(f"Tags atualizadas: {', '.join(tags_buffet)}")

def criar_festa_com_builder():
    """Sistema de criação de festa usando Builder Pattern"""
    print("\n" + "="*60)
    print("    CRIAÇÃO DE FESTA")
    print("    (Usando Padrão Builder)")
    print("="*60)
    print("Vamos criar sua festa personalizada!")
    print()
    
    usuario = sistema_login.usuario_logado
    
    tipos_festa = {
        "1": ("Festa Básica", "basica"),
        "2": ("Festa Personalizada", "personalizada")
    }
    
    print("Tipos de festa disponíveis:")
    for key, (nome, _) in tipos_festa.items():
        print(f"{key}. {nome}")
    
    while True:
        escolha = input("\nEscolha o tipo de festa (1-2): ").strip()
        if escolha in tipos_festa:
            nome_tipo, tipo = tipos_festa[escolha]
            break
        else:
            print("ERRO: Escolha inválida! Digite 1 ou 2.")
    
    print(f"\nConfigurando {nome_tipo}...")
    

    nome_aniversariante = input("Nome do aniversariante: ")
    
    while True:
        try:
            data_str = input("Data da festa (DD/MM/AAAA): ")
            dia, mes, ano = map(int, data_str.split('/'))
            data_festa = date(ano, mes, dia)
            break
        except ValueError:
            print("ERRO: Formato inválido! Use DD/MM/AAAA")
    
    if tipo == "basica":
        festa_info = criar_festa_basica(nome_aniversariante, data_festa)
    else:  
        festa_info = criar_festa_personalizada(nome_aniversariante, data_festa)
    
    if festa_info:
        salvar_festa_no_perfil(festa_info)
        return True
    
    return False

def criar_festa_basica(nome_aniversariante: str, data_festa: date):
    """Cria festa básica usando Builder Pattern"""
    print("\nCriando Festa Básica...")
    print("(Configurações padrão serão aplicadas)")
    
    try:
        builder = FestaBasicaBuilder(nome_aniversariante, data_festa)
        organizador = OrganizadorDeFesta()
        
        festa_organizada = organizador.construirFesta(builder)
        
        print(f"\nFesta Básica criada com sucesso!")
        print(f"- Aniversariante: {festa_organizada.nomeAniversariante}")
        print(f"- Data: {festa_organizada.data}")
        print(f"- Horário: {festa_organizada.horario}")
        print(f"- Local: {festa_organizada.localFornecedor}")
        print(f"- Banda/Música: {festa_organizada.banda}")
        print(f"- Buffet: {', '.join(festa_organizada.buffet)}")
        
        return {
            "tipo": "festa_basica",
            "nome_aniversariante": festa_organizada.nomeAniversariante,
            "data": festa_organizada.data,
            "horario": festa_organizada.horario,
            "local": festa_organizada.localFornecedor,
            "banda": festa_organizada.banda,
            "buffet": festa_organizada.buffet,
            "convite": festa_organizada.convite,
            "link_whatsapp": festa_organizada.linkWhatsapp,
            "festa_organizada": festa_organizada
        }
        
    except Exception as e:
        print(f"ERRO ao criar festa básica: {e}")
        return None

def criar_festa_personalizada(nome_aniversariante: str, data_festa: date):
    """Cria festa personalizada usando Builder Pattern"""
    print("\nCriando Festa Personalizada...")
    print("Você pode configurar todos os detalhes!")
    
    horario = input("Horário da festa (ex: 15:00): ")
    local = input("Local da festa: ")
    
    print("\nBanda/Música (digite as opções separadas por vírgula):")
    banda_input = input("Ex: DJ João, Banda Rock, Playlist: ")
    banda = banda_input.strip() if banda_input.strip() else "Música ambiente"
    
    print("\nBuffet (digite os itens separados por vírgula):")
    buffet_input = input("Ex: Bolo, Pizza, Refrigerante: ")
    buffet_lista = [item.strip() for item in buffet_input.split(',') if item.strip()]
    
    try:
        plano = PlanoDeFesta(
            buffetEscolhidas=buffet_lista,
            bandaEscolhida=banda,
            nomeAniversariante=nome_aniversariante,
            data=data_festa,
            horario=horario,
            localFornecedor=local
        )
    
        builder = FestaPersonalizadaBuilder(plano)
        organizador = OrganizadorDeFesta()
        
        festa_organizada = organizador.construirFesta(builder)
        
        print(f"\nFesta Personalizada criada com sucesso!")
        print(f"- Aniversariante: {festa_organizada.nomeAniversariante}")
        print(f"- Data: {festa_organizada.data}")
        print(f"- Horário: {festa_organizada.horario}")
        print(f"- Local: {festa_organizada.localFornecedor}")
        print(f"- Banda/Música: {festa_organizada.banda}")
        print(f"- Buffet: {', '.join(festa_organizada.buffet)}")
        
        return {
            "tipo": "festa_personalizada",
            "nome_aniversariante": festa_organizada.nomeAniversariante,
            "data": festa_organizada.data,
            "horario": festa_organizada.horario,
            "local": festa_organizada.localFornecedor,
            "banda": festa_organizada.banda,
            "buffet": festa_organizada.buffet,
            "convite": festa_organizada.convite,
            "link_whatsapp": festa_organizada.linkWhatsapp,
            "festa_organizada": festa_organizada,
            "plano": plano
        }
        
    except Exception as e:
        print(f"ERRO ao criar festa personalizada: {e}")
        return None

def salvar_festa_no_perfil(festa_info):
    """Salva a festa criada no perfil do usuário"""
    usuario = sistema_login.usuario_logado
    
    tags_festa = ["festa", "evento", "aniversario"]
    if festa_info["tipo"] == "festa_personalizada":
        tags_festa.extend(["personalizada", "customizada"])
    else:
        tags_festa.extend(["basica", "simples"])
    
    tags_unicas = list(set(usuario.tagsDePreferencias + tags_festa))
    usuario.tagsDePreferencias = tags_unicas
    
    if not usuario.perfil:
        usuario.perfil = Perfil(
            biografia=f"Usuário com festa {festa_info['tipo']} criada",
            interesses=tags_unicas,
            visibilidade="publico",
            festa_criada=festa_info
        )
    else:
        usuario.perfil.interesses = tags_unicas
        usuario.perfil.festa_criada = festa_info
    
    sistema_login.festa_criada = True
    
    print(f"\nFesta salva no perfil!")
    print(f"Tipo: {festa_info['tipo']}")
    print(f"Aniversariante: {festa_info['nome_aniversariante']}")
    print(f"Tags atualizadas: {', '.join(tags_festa)}")

def organizar_evento_com_composite():
    """Sistema de organização de evento usando Composite Pattern"""
    print("\n" + "="*60)
    print("    ORGANIZAÇÃO DE EVENTO")
    print("    (Usando Padrão Composite)")
    print("="*60)
    print("Vamos organizar todos os fornecedores para seu evento!")
    print()
    
    usuario = sistema_login.usuario_logado
    
    nome_evento = input("Nome do evento: ")
    evento = Evento(nome_evento)
    
    tipos_fornecedores_evento = {
        "1": ("Banda/Música", Banda()),
        "2": ("Locação de Local", LocacaoLocal()),
        "3": ("Segurança", Seguranca()),
        "4": ("Decoração", Decoracao()),
        "5": ("Comida/Catering", Comida())
    }
    
    print("Tipos de fornecedores disponíveis para o evento:")
    for key, (nome, _) in tipos_fornecedores_evento.items():
        print(f"{key}. {nome}")
    
    print("\nDigite os números dos fornecedores que deseja adicionar ao evento (separados por vírgula):")
    print("Ex: 1,2,3 para Banda, Locação e Segurança")
    escolhas = input("Sua escolha: ").split(',')
    
    fornecedores_adicionados = []
    for escolha in escolhas:
        escolha = escolha.strip()
        if escolha in tipos_fornecedores_evento:
            nome_fornecedor, fornecedor_obj = tipos_fornecedores_evento[escolha]
            evento.add(fornecedor_obj)
            fornecedores_adicionados.append(nome_fornecedor)
    
    if not fornecedores_adicionados:
        print("ERRO: Nenhum fornecedor válido selecionado!")
        return False
    
    print(f"\nFornecedores adicionados ao evento: {', '.join(fornecedores_adicionados)}")
    
    print("\n" + "="*50)
    print("EXECUTANDO MONTAGEM DO EVENTO")
    print("="*50)
    
    montagem_resultados = evento.montar_evento()
    for i, resultado in enumerate(montagem_resultados, 1):
        print(f"{i}. {resultado}")
    
    resumo_evento = evento.calcular_evento()
    print(f"\nResumo: {resumo_evento}")
    
    evento_info = {
        "nome": nome_evento,
        "fornecedores": [f.__class__.__name__ for f in evento.fornecedores],
        "fornecedores_nomes": fornecedores_adicionados,
        "montagem": montagem_resultados,
        "resumo": resumo_evento,
        "total_fornecedores": len(evento.fornecedores),
        "evento_obj": evento
    }
    
    salvar_evento_no_perfil(evento_info)
    
    return True

def adicionar_fornecedor_ao_evento():
    """Adiciona fornecedor adicional ao evento já criado"""
    usuario = sistema_login.usuario_logado
    
    if not usuario.perfil or not hasattr(usuario.perfil, 'evento_organizado') or not usuario.perfil.evento_organizado:
        print("\nNenhum evento organizado ainda.")
        return False
    
    evento_info = usuario.perfil.evento_organizado
    evento_obj = evento_info["evento_obj"]
    
    print(f"\nAdicionando fornecedor ao evento: {evento_info['nome']}")
    print("Fornecedores atuais:")
    for i, nome in enumerate(evento_info['fornecedores_nomes'], 1):
        print(f"{i}. {nome}")
    
    tipos_fornecedores_evento = {
        "1": ("Banda/Música", Banda()),
        "2": ("Locação de Local", LocacaoLocal()),
        "3": ("Segurança", Seguranca()),
        "4": ("Decoração", Decoracao()),
        "5": ("Comida/Catering", Comida())
    }
    
    print("\nTipos de fornecedores disponíveis:")
    for key, (nome, _) in tipos_fornecedores_evento.items():
        print(f"{key}. {nome}")
    
    escolha = input("\nEscolha um fornecedor para adicionar (1-5): ").strip()
    
    if escolha in tipos_fornecedores_evento:
        nome_fornecedor, fornecedor_obj = tipos_fornecedores_evento[escolha]
        evento_obj.add(fornecedor_obj)
        
        evento_info["fornecedores"].append(fornecedor_obj.__class__.__name__)
        evento_info["fornecedores_nomes"].append(nome_fornecedor)
        evento_info["total_fornecedores"] = len(evento_obj.fornecedores)
        evento_info["montagem"] = evento_obj.montar_evento()
        evento_info["resumo"] = evento_obj.calcular_evento()
        
        usuario.perfil.evento_organizado = evento_info
        
        print(f"\n{nome_fornecedor} adicionado com sucesso!")
        print(f"Total de fornecedores: {evento_info['total_fornecedores']}")
        print(f"Novo resumo: {evento_info['resumo']}")
        
        return True
    else:
        print("ERRO: Escolha inválida!")
        return False

def remover_fornecedor_do_evento():
    """Remove fornecedor do evento já criado"""
    usuario = sistema_login.usuario_logado
    
    if not usuario.perfil or not hasattr(usuario.perfil, 'evento_organizado') or not usuario.perfil.evento_organizado:
        print("\nNenhum evento organizado ainda.")
        return False
    
    evento_info = usuario.perfil.evento_organizado
    evento_obj = evento_info["evento_obj"]
    
    if not evento_obj.fornecedores:
        print("\nEvento não possui fornecedores para remover.")
        return False
    
    print(f"\nRemoção de fornecedor do evento: {evento_info['nome']}")
    print("Fornecedores atuais:")
    for i, nome in enumerate(evento_info['fornecedores_nomes'], 1):
        print(f"{i}. {nome}")
    
    while True:
        try:
            escolha = int(input("\nEscolha o número do fornecedor para remover: ")) - 1
            if 0 <= escolha < len(evento_obj.fornecedores):
                break
            else:
                print("ERRO: Número inválido!")
        except ValueError:
            print("ERRO: Digite um número válido!")
    
    fornecedor_removido = evento_obj.fornecedores[escolha]
    nome_removido = evento_info["fornecedores_nomes"][escolha]
    
    evento_obj.remove(fornecedor_removido)

    evento_info["fornecedores"].pop(escolha)
    evento_info["fornecedores_nomes"].pop(escolha)
    evento_info["total_fornecedores"] = len(evento_obj.fornecedores)
    evento_info["montagem"] = evento_obj.montar_evento()
    evento_info["resumo"] = evento_obj.calcular_evento()
    
    usuario.perfil.evento_organizado = evento_info
    
    print(f"\n{nome_removido} removido com sucesso!")
    print(f"Total de fornecedores restantes: {evento_info['total_fornecedores']}")
    print(f"Novo resumo: {evento_info['resumo']}")
    
    return True

def salvar_evento_no_perfil(evento_info):
    """Salva o evento organizado no perfil do usuário"""
    usuario = sistema_login.usuario_logado
    
    tags_evento = ["evento", "organizacao", "fornecedores"]
    tags_evento.extend([f.lower() for f in evento_info["fornecedores_nomes"]])

    tags_unicas = list(set(usuario.tagsDePreferencias + tags_evento))
    usuario.tagsDePreferencias = tags_unicas
    

    if not usuario.perfil:
        usuario.perfil = Perfil(
            biografia=f"Usuário com evento {evento_info['nome']} organizado",
            interesses=tags_unicas,
            visibilidade="publico",
            evento_organizado=evento_info
        )
    else:

        usuario.perfil.interesses = tags_unicas
        usuario.perfil.evento_organizado = evento_info
    
    sistema_login.evento_organizado = True
    
    print(f"\nEvento salvo no perfil!")
    print(f"Nome: {evento_info['nome']}")
    print(f"Fornecedores: {', '.join(evento_info['fornecedores_nomes'])}")
    print(f"Tags atualizadas: {', '.join(tags_evento[:5])}...")

def criar_convites_com_decorator():
    """Sistema de criação de convites usando Decorator Pattern"""
    print("\n" + "="*60)
    print("    CRIAÇÃO DE CONVITES PARA SEU EVENTO")
    print("    (Usando Padrão Decorator)")
    print("="*60)
    print("Vamos criar convites personalizados para seu evento!")
    print()
    
    usuario = sistema_login.usuario_logado
    
    if not usuario.perfil or not hasattr(usuario.perfil, 'evento_organizado') or not usuario.perfil.evento_organizado:
        print("ERRO: Você precisa organizar um evento primeiro!")
        return False
    
    evento_info = usuario.perfil.evento_organizado
    
    tipos_convites = {
        "1": ("Convite Básico", "basico"),
        "2": ("Convite Interativo", "interativo"),
        "3": ("Convite de Luxo", "luxo"),
        "4": ("Convite Completo (Interativo + Luxo)", "completo")
    }
    
    print(f"Criando convites para o evento: {evento_info['nome']}")
    print("Tipos de convites disponíveis:")
    for key, (nome, _) in tipos_convites.items():
        print(f"{key}. {nome}")
    
    while True:
        escolha = input("\nEscolha o tipo de convite (1-4): ").strip()
        if escolha in tipos_convites:
            nome_tipo, tipo = tipos_convites[escolha]
            break
        else:
            print("ERRO: Escolha inválida! Digite 1-4.")
    
    print(f"\nCriando {nome_tipo}...")
    
    titulo = input("Título do convite: ")
    mensagem = input("Mensagem do convite: ")
    

    print("\nSimulando lista de convidados...")
    destinatarios = [usuario]  
    
    convite_info = None
    
    if tipo == "basico":
        convite_info = criar_convite_basico(destinatarios, usuario, titulo, mensagem)
    elif tipo == "interativo":
        convite_info = criar_convite_interativo(destinatarios, usuario, titulo, mensagem)
    elif tipo == "luxo":
        convite_info = criar_convite_luxo(destinatarios, usuario, titulo, mensagem)
    elif tipo == "completo":
        convite_info = criar_convite_completo(destinatarios, usuario, titulo, mensagem)
    
    if convite_info:
        salvar_convite_no_perfil(convite_info, evento_info)
        return True
    
    return False

def criar_convite_basico(destinatarios, remetente, titulo, mensagem):
    """Cria convite básico usando Decorator Pattern"""
    print("\nCriando Convite Básico...")
    
    try:
        template = TemplateDefault()
        
        convite = ConviteConcreto(
            destinatario=destinatarios,
            remetente=remetente,
            titulo=titulo,
            template=template,
            mensagem=mensagem
        )
        
        convite_gerado = convite.criar_convite()
        
        print(f"\nConvite Básico criado:")
        print(f"- Título: {convite_gerado['titulo']}")
        print(f"- Mensagem: {convite_gerado['mensagem']}")
        print(f"- Template: {convite_gerado['template']['tema']}")
        print(f"- Status: {convite_gerado['status']}")
        
        return {
            "tipo": "convite_basico",
            "titulo": titulo,
            "mensagem": mensagem,
            "convite_obj": convite,
            "convite_gerado": convite_gerado
        }
        
    except Exception as e:
        print(f"ERRO ao criar convite básico: {e}")
        return None

def criar_convite_interativo(destinatarios, remetente, titulo, mensagem):
    """Cria convite interativo usando Decorator Pattern"""
    print("\nCriando Convite Interativo...")
    
    try:
        template = TemplateDefault()
        convite_base = ConviteConcreto(
            destinatario=destinatarios,
            remetente=remetente,
            titulo=titulo,
            template=template,
            mensagem=mensagem
        )
        
        convite_interativo = DecoratorInterativo(convite_base)
        
        print("\nConfigurações Interativas:")
        
      
        usar_mapa = input("Adicionar mapa da localização? (s/n): ").lower() in ['s', 'sim']
        if usar_mapa:
            try:
                lat = float(input("Latitude (ex: -23.5505): "))
                lng = float(input("Longitude (ex: -46.6333): "))
                zoom = int(input("Zoom (10-20, padrão 15): ") or "15")
                convite_interativo.configurar_mapa(lat, lng, zoom)
            except ValueError:
                print("Valores inválidos para mapa, usando configuração padrão.")
                convite_interativo.configurar_mapa(-23.5505, -46.6333, 15)
        

        usar_carousel = input("Adicionar carrossel de imagens? (s/n): ").lower() in ['s', 'sim']
        if usar_carousel:
            print("Digite URLs das imagens (uma por linha, linha vazia para terminar):")
            while True:
                url = input("URL da imagem: ").strip()
                if not url:
                    break
                convite_interativo.adicionar_imagem_carousel(url)
        
       
        usar_comentarios = input("Adicionar seção de comentários? (s/n): ").lower() in ['s', 'sim']
        if usar_comentarios:
            print("Digite comentários iniciais (um por linha, linha vazia para terminar):")
            while True:
                comentario = input("Comentário: ").strip()
                if not comentario:
                    break
                convite_interativo.adicionar_comentario(comentario)
        
     
        convite_gerado = convite_interativo.criar_convite()
        
        print(f"\nConvite Interativo criado:")
        print(f"- Título: {convite_gerado['titulo']}")
        print(f"- Funcionalidades interativas: {list(convite_gerado.get('interativo', {}).keys())}")
        print(f"- Status: {convite_gerado['status']}")
        
        return {
            "tipo": "convite_interativo",
            "titulo": titulo,
            "mensagem": mensagem,
            "convite_obj": convite_interativo,
            "convite_gerado": convite_gerado
        }
        
    except Exception as e:
        print(f"ERRO ao criar convite interativo: {e}")
        return None

def criar_convite_luxo(destinatarios, remetente, titulo, mensagem):
    """Cria convite de luxo usando Decorator Pattern"""
    print("\nCriando Convite de Luxo...")
    
    try:
     
        template = TemplateDefault()
        convite_base = ConviteConcreto(
            destinatario=destinatarios,
            remetente=remetente,
            titulo=titulo,
            template=template,
            mensagem=mensagem
        )
        

        convite_luxo = DecoratorLuxo(convite_base)
        
  
        print("\nConfigurações de Luxo:")
        

        usar_carousel = input("Adicionar carrossel de imagens? (s/n): ").lower() in ['s', 'sim']
        if usar_carousel:
            print("Digite URLs das imagens (uma por linha, linha vazia para terminar):")
            while True:
                url = input("URL da imagem: ").strip()
                if not url:
                    break
                convite_luxo.adicionar_imagem_carousel(url)
        
     
        usar_videos = input("Adicionar vídeos? (s/n): ").lower() in ['s', 'sim']
        if usar_videos:
            print("Digite URLs dos vídeos (uma por linha, linha vazia para terminar):")
            while True:
                url = input("URL do vídeo: ").strip()
                if not url:
                    break
                convite_luxo.adicionar_video(url)
        
  
        usar_som = input("Adicionar música de fundo? (s/n): ").lower() in ['s', 'sim']
        if usar_som:
            url_som = input("URL da música: ").strip()
            autoplay = input("Reprodução automática? (s/n): ").lower() in ['s', 'sim']
            if url_som:
                convite_luxo.configurar_som(url_som, autoplay)
        
        usar_tipografia = input("Personalizar tipografia? (s/n): ").lower() in ['s', 'sim']
        if usar_tipografia:
            fonte = input("Nome da fonte (ex: Georgia, Times, Arial): ").strip()
            if fonte:
                convite_luxo.configurar_tipografia(fonte)
        
   
        convite_gerado = convite_luxo.criar_convite()
        
        print(f"\nConvite de Luxo criado:")
        print(f"- Título: {convite_gerado['titulo']}")
        print(f"- Funcionalidades de luxo: {list(convite_gerado.get('luxo', {}).keys())}")
        print(f"- Status: {convite_gerado['status']}")
        
        return {
            "tipo": "convite_luxo",
            "titulo": titulo,
            "mensagem": mensagem,
            "convite_obj": convite_luxo,
            "convite_gerado": convite_gerado
        }
        
    except Exception as e:
        print(f"ERRO ao criar convite de luxo: {e}")
        return None

def criar_convite_completo(destinatarios, remetente, titulo, mensagem):
    """Cria convite completo (Interativo + Luxo) usando Decorator Pattern"""
    print("\nCriando Convite Completo (Interativo + Luxo)...")
    
    try:
 
        template = TemplateDefault()
        convite_base = ConviteConcreto(
            destinatario=destinatarios,
            remetente=remetente,
            titulo=titulo,
            template=template,
            mensagem=mensagem
        )
        

        convite_interativo = DecoratorInterativo(convite_base)
        
 
        convite_completo = DecoratorLuxo(convite_interativo)
        
        print("\nConfigurando funcionalidades Interativas e de Luxo...")
        
 
        convite_interativo.configurar_mapa(-23.5505, -46.6333, 15)
        convite_interativo.adicionar_imagem_carousel("https://exemplo.com/imagem1.jpg")
        convite_interativo.adicionar_comentario("Esperamos por você!")
        
        convite_completo.adicionar_video("https://exemplo.com/video.mp4")
        convite_completo.configurar_som("https://exemplo.com/musica.mp3", False)
        convite_completo.configurar_tipografia("Georgia")
        

        convite_gerado = convite_completo.criar_convite()
        
        print(f"\nConvite Completo criado:")
        print(f"- Título: {convite_gerado['titulo']}")
        print(f"- Funcionalidades interativas: {list(convite_gerado.get('interativo', {}).keys())}")
        print(f"- Funcionalidades de luxo: {list(convite_gerado.get('luxo', {}).keys())}")
        print(f"- Status: {convite_gerado['status']}")
        
        return {
            "tipo": "convite_completo",
            "titulo": titulo,
            "mensagem": mensagem,
            "convite_obj": convite_completo,
            "convite_gerado": convite_gerado
        }
        
    except Exception as e:
        print(f"ERRO ao criar convite completo: {e}")
        return None

def salvar_convite_no_perfil(convite_info, evento_info):
    """Salva o convite criado no perfil do usuário"""
    usuario = sistema_login.usuario_logado
    

    tags_convite = ["convite", "evento", "comunicacao"]
    if "interativo" in convite_info["tipo"]:
        tags_convite.extend(["interativo", "digital"])
    if "luxo" in convite_info["tipo"]:
        tags_convite.extend(["luxo", "premium", "personalizado"])
    

    tags_unicas = list(set(usuario.tagsDePreferencias + tags_convite))
    usuario.tagsDePreferencias = tags_unicas
    

    if not usuario.perfil:
        usuario.perfil = Perfil(
            biografia=f"Usuário com convite {convite_info['tipo']} criado",
            interesses=tags_unicas,
            visibilidade="publico",
            convite_criado=convite_info
        )
    else:

        usuario.perfil.interesses = tags_unicas
        usuario.perfil.convite_criado = convite_info
    
 
    sistema_login.convites_criados = True
    
    print(f"\nConvite salvo no perfil!")
    print(f"Tipo: {convite_info['tipo']}")
    print(f"Título: {convite_info['titulo']}")
    print(f"Para evento: {evento_info['nome']}")
    print(f"Tags atualizadas: {', '.join(tags_convite)}")

def ver_convite_usuario():
    """Exibe o convite criado pelo usuário"""
    usuario = sistema_login.usuario_logado
    
    if not usuario.perfil or not hasattr(usuario.perfil, 'convite_criado') or not usuario.perfil.convite_criado:
        print("\nNenhum convite criado ainda.")
        return
    
    convite = usuario.perfil.convite_criado
    print("\nMEU CONVITE")
    print("-" * 50)
    
    print(f"\n{convite['tipo'].replace('_', ' ').title()}")
    print(f"Título: {convite['titulo']}")
    print(f"Mensagem: {convite['mensagem']}")
    

    convite_gerado = convite['convite_gerado']
    
    if 'interativo' in convite_gerado:
        print("\nFuncionalidades Interativas:")
        interativo = convite_gerado['interativo']
        if 'googleMaps' in interativo:
            print(f"- Mapa: Lat {interativo['googleMaps']['latitude']}, Lng {interativo['googleMaps']['longitude']}")
        if 'carousel' in interativo:
            print(f"- Carrossel: {len(interativo['carousel'])} imagens")
        if 'comentarios' in interativo:
            print(f"- Comentários: {len(interativo['comentarios'])} comentários")
    
    if 'luxo' in convite_gerado:
        print("\nFuncionalidades de Luxo:")
        luxo = convite_gerado['luxo']
        if 'carousel' in luxo:
            print(f"- Carrossel de luxo: {len(luxo['carousel'])} imagens")
        if 'videos' in luxo:
            print(f"- Vídeos: {len(luxo['videos'])} vídeos")
        if 'sons' in luxo:
            print(f"- Música de fundo: {luxo['sons']['url']}")
        if 'tipografia' in luxo:
            print(f"- Fonte personalizada: {luxo['tipografia']}")

def menu_usuario_logado():
    """Menu para usuário logado"""
    while True:
        usuario = sistema_login.usuario_logado

        if not sistema_login.quiz_realizado:
            print("\nAntes de acessar seu perfil, vamos fazer um quiz rápido!")
            print("Isso nos ajudará a personalizar suas preferências de festa.")
            print("O quiz utiliza o padrão Composite para flexibilidade!")
            print("\n1. Fazer quiz agora (Composite Pattern)")
            print("2. Pular quiz (não recomendado)")
            print("3. Fazer logout")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                if realizar_quiz():
                    continue
                else:
                    print("ERRO ao realizar quiz. Tente novamente.")
            elif opcao == "2":
                sistema_login.quiz_realizado = True
                print("AVISO: Quiz pulado. Você pode fazer mais tarde nas configurações.")
                continue
            elif opcao == "3":
                sistema_login.fazer_logout()
                print("Logout realizado com sucesso!")
                break
            else:
                print("ERRO: Opção inválida!")
                continue

        if not sistema_login.fornecedores_selecionados:
            print("\nAgora vamos selecionar fornecedores para sua festa!")
            print("Isso nos ajudará a criar um evento personalizado.")
            print("O sistema utiliza o padrão Factory Method!")
            print("\n1. Selecionar fornecedores agora (Factory Method)")
            print("2. Pular seleção (não recomendado)")
            print("3. Fazer logout")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                if selecionar_fornecedores_com_factory():
                    continue
                else:
                    print("ERRO ao selecionar fornecedores. Tente novamente.")
            elif opcao == "2":
                sistema_login.fornecedores_selecionados = True
                print("AVISO: Seleção de fornecedores pulada. Você pode fazer mais tarde.")
                continue
            elif opcao == "3":
                sistema_login.fazer_logout()
                print("Logout realizado com sucesso!")
                break
            else:
                print("ERRO: Opção inválida!")
                continue
        
   
        if not sistema_login.buffet_selecionado:
            print("\nAgora vamos selecionar o buffet para sua festa!")
            print("Isso completará o planejamento do seu evento.")
            print("O sistema utiliza o padrão Template Method para portfólios!")
            print("\n1. Selecionar buffet agora (Template Method)")
            print("2. Pular seleção (não recomendado)")
            print("3. Fazer logout")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                if selecionar_buffet_com_template_method():
                    continue
                else:
                    print("ERRO ao selecionar buffet. Tente novamente.")
            elif opcao == "2":
                sistema_login.buffet_selecionado = True
                print("AVISO: Seleção de buffet pulada. Você pode fazer mais tarde.")
                continue
            elif opcao == "3":
                sistema_login.fazer_logout()
                print("Logout realizado com sucesso!")
                break
            else:
                print("ERRO: Opção inválida!")
                continue
        

        if not sistema_login.festa_criada:
            print("\nAgora vamos criar sua festa!")
            print("Este é o passo final para completar o planejamento.")
            print("O sistema utiliza o padrão Builder para criação de festas!")
            print("\n1. Criar festa agora (Builder Pattern)")
            print("2. Pular criação (não recomendado)")
            print("3. Fazer logout")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                if criar_festa_com_builder():
                    continue
                else:
                    print("ERRO ao criar festa. Tente novamente.")
            elif opcao == "2":
                sistema_login.festa_criada = True
                print("AVISO: Criação de festa pulada. Você pode fazer mais tarde.")
                continue
            elif opcao == "3":
                sistema_login.fazer_logout()
                print("Logout realizado com sucesso!")
                break
            else:
                print("ERRO: Opção inválida!")
                continue
        

        if not sistema_login.evento_organizado:
            print("\nAgora vamos organizar seu evento completo!")
            print("Este sistema coordena todos os fornecedores usando Composite.")
            print("O sistema utiliza o padrão Composite para organização de eventos!")
            print("\n1. Organizar evento agora (Composite Pattern)")
            print("2. Pular organização (não recomendado)")
            print("3. Fazer logout")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                if organizar_evento_com_composite():
                    continue
                else:
                    print("ERRO ao organizar evento. Tente novamente.")
            elif opcao == "2":
                sistema_login.evento_organizado = True
                print("AVISO: Organização de evento pulada. Você pode fazer mais tarde.")
                continue
            elif opcao == "3":
                sistema_login.fazer_logout()
                print("Logout realizado com sucesso!")
                break
            else:
                print("ERRO: Opção inválida!")
                continue
        

        if sistema_login.evento_organizado and not sistema_login.convites_criados:
            print("\nPor fim, vamos criar convites para seu evento!")
            print("Este sistema usa o padrão Decorator para personalizar convites.")
            print("O sistema utiliza o padrão Decorator para criação de convites!")
            print("\n1. Criar convites agora (Decorator Pattern)")
            print("2. Pular criação (não recomendado)")
            print("3. Fazer logout")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                if criar_convites_com_decorator():
                    continue
                else:
                    print("ERRO ao criar convites. Tente novamente.")
            elif opcao == "2":
                sistema_login.convites_criados = True
                print("AVISO: Criação de convites pulada. Você pode fazer mais tarde.")
                continue
            elif opcao == "3":
                sistema_login.fazer_logout()
                print("Logout realizado com sucesso!")
                break
            else:
                print("ERRO: Opção inválida!")
                continue
        

        print("\n" + "="*50)
        print(f"    ÁREA DO USUÁRIO - {usuario.nome}")
        print("="*50)
        print("1. Ver meu perfil completo")
        print("2. Editar preferências")
        print("3. Refazer quiz de personalidade (Composite)")
        print("4. Reselecionar fornecedores (Factory Method)")
        print("5. Ver meus fornecedores")
        print("6. Reselecionar buffet (Template Method)")
        print("7. Ver meu buffet")
        print("8. Recriar festa (Builder Pattern)")
        print("9. Ver minha festa")
        print("10. Reorganizar evento (Composite Pattern)")
        print("11. Ver meu evento")
        print("12. Adicionar fornecedor ao evento")
        print("13. Remover fornecedor do evento")
        print("14. Recriar convites (Decorator Pattern)")
        print("15. Ver meu convite")
        print("16. Fazer logout")
        print("="*50)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            ver_perfil_usuario()
        elif opcao == "2":
            editar_preferencias()
        elif opcao == "3":
            sistema_login.quiz_realizado = False
            print("Quiz resetado. Você será direcionado para refazê-lo usando Composite Pattern.")
        elif opcao == "4":
            sistema_login.fornecedores_selecionados = False
            print("Fornecedores resetados. Você será direcionado para reselecioná-los usando Factory Method.")
        elif opcao == "5":
            ver_fornecedores_usuario()
        elif opcao == "6":
            sistema_login.buffet_selecionado = False
            print("Buffet resetado. Você será direcionado para reselecioná-lo usando Template Method.")
        elif opcao == "7":
            ver_buffet_usuario()
        elif opcao == "8":
            sistema_login.festa_criada = False
            print("Festa resetada. Você será direcionado para recriá-la usando Builder Pattern.")
        elif opcao == "9":
            ver_festa_usuario()
        elif opcao == "10":
            sistema_login.evento_organizado = False
            print("Evento resetado. Você será direcionado para reorganizá-lo usando Composite Pattern.")
        elif opcao == "11":
            ver_evento_usuario()
        elif opcao == "12":
            adicionar_fornecedor_ao_evento()
        elif opcao == "13":
            remover_fornecedor_do_evento()
        elif opcao == "14":
            sistema_login.convites_criados = False
            print("Convites resetados. Você será direcionado para recriá-los usando Decorator Pattern.")
        elif opcao == "15":
            ver_convite_usuario()
        elif opcao == "16":
            sistema_login.fazer_logout()
            print("Logout realizado com sucesso!")
            break
        else:
            print("ERRO: Opção inválida!")

def ver_fornecedores_usuario():
    """Exibe os fornecedores selecionados pelo usuário"""
    usuario = sistema_login.usuario_logado
    
    if not usuario.perfil or not usuario.perfil.fornecedores_contratados:
        print("\nNenhum fornecedor selecionado ainda.")
        return
    
    print("\nMEUS FORNECEDORES")
    print("-" * 50)
    
    total_preco = 0
    for i, fornecedor in enumerate(usuario.perfil.fornecedores_contratados, 1):
        print(f"\n{i}. {fornecedor['nome']} ({fornecedor['tipo'].title()})")
        print(f"   Contato: {fornecedor['contato']}")
        print(f"   Tags: {', '.join(fornecedor['tags'])}")
        print(f"   Preço estimado: R$ {fornecedor['preco_estimado']:.2f}")
        print(f"   Serviços: {', '.join(fornecedor['servicos'])}")
        if fornecedor['portfolio']:
            print(f"   Portfolio: {fornecedor['portfolio']}")
        
        total_preco += fornecedor['preco_estimado']
    
    print(f"\nTOTAL ESTIMADO: R$ {total_preco:.2f}")
    print(f"Total de fornecedores: {len(usuario.perfil.fornecedores_contratados)}")

def ver_buffet_usuario():
    """Exibe o buffet selecionado pelo usuário"""
    usuario = sistema_login.usuario_logado
    
    if not usuario.perfil or not hasattr(usuario.perfil, 'buffet_contratado') or not usuario.perfil.buffet_contratado:
        print("\nNenhum buffet selecionado ainda.")
        return
    
    buffet = usuario.perfil.buffet_contratado
    print("\nMEU BUFFET")
    print("-" * 50)
    
    print(f"\n{buffet['titulo']} ({buffet['tipo'].replace('_', ' ').title()})")
    print(f"Valor base: R$ {buffet['valor_base']:.2f}")
    print(f"Portfólio: {buffet['portifolio']['descricao_completa']}")
    
    if buffet['tipo'] == 'buffet_tradicional':
        print(f"Tipo de evento: {buffet['tipo_evento']}")
        print(f"Pratos: {', '.join(buffet['cardapio_pratos'])}")
    else:  
        print(f"Tipos de doce: {', '.join(buffet['tipo_doce'])}")
        print(f"Cardápio: {', '.join(buffet['cardapio_doces'])}")
        if buffet['cardapio_restricoes']:
            print(f"Restrições atendidas: {', '.join(buffet['cardapio_restricoes'])}")

def ver_festa_usuario():
    """Exibe a festa criada pelo usuário"""
    usuario = sistema_login.usuario_logado
    
    if not usuario.perfil or not hasattr(usuario.perfil, 'festa_criada') or not usuario.perfil.festa_criada:
        print("\nNenhuma festa criada ainda.")
        return
    
    festa = usuario.perfil.festa_criada
    print("\nMINHA FESTA")
    print("-" * 50)
    
    print(f"\n{festa['tipo'].replace('_', ' ').title()}")
    print(f"Aniversariante: {festa['nome_aniversariante']}")
    print(f"Data: {festa['data']}")
    print(f"Horário: {festa['horario']}")
    print(f"Local: {festa['local']}")
    print(f"Banda/Música: {festa['banda']}")
    print(f"Buffet: {', '.join(festa['buffet'])}")
    
    if festa.get('convite'):
        print(f"Convite: {festa['convite']}")
    
    if festa.get('link_whatsapp'):
        print(f"Link WhatsApp: {festa['link_whatsapp']}")

def ver_evento_usuario():
    """Exibe o evento organizado pelo usuário"""
    usuario = sistema_login.usuario_logado
    
    if not usuario.perfil or not hasattr(usuario.perfil, 'evento_organizado') or not usuario.perfil.evento_organizado:
        print("\nNenhum evento organizado ainda.")
        return
    
    evento = usuario.perfil.evento_organizado
    print("\nMEU EVENTO ORGANIZADO")
    print("-" * 50)
    
    print(f"\nNome do Evento: {evento['nome']}")
    print(f"Total de Fornecedores: {evento['total_fornecedores']}")
    print(f"Resumo: {evento['resumo']}")
    
    print("\nFornecedores do Evento:")
    for i, nome in enumerate(evento['fornecedores_nomes'], 1):
        print(f"{i}. {nome}")
    
    print("\nMontagem do Evento:")
    for i, montagem in enumerate(evento['montagem'], 1):
        print(f"{i}. {montagem}")

def ver_perfil_usuario():
    """Exibe o perfil do usuário logado"""
    usuario = sistema_login.usuario_logado
    print("\nMEU PERFIL PERSONALIZADO")
    print("-" * 40)
    print(f"Nome: {usuario.nome}")
    print(f"Data de Nascimento: {usuario.dataNascimento}")
    print(f"Idade: {(date.today() - usuario.dataNascimento).days // 365} anos")
    
    if usuario.sobreMim:
        print(f"Sobre mim: {usuario.sobreMim}")
    
    if usuario.perfil:
        print(f"Biografia: {usuario.perfil.biografia}")
        print(f"Visibilidade: {usuario.perfil.visibilidade}")
        if usuario.perfil.interesses:
            print(f"Interesses do Perfil: {', '.join(usuario.perfil.interesses)}")
    
    if usuario.tagsDePreferencias:
        print(f"Preferências de Festa: {', '.join(usuario.tagsDePreferencias)}")
    else:
        print("Preferências: Nenhuma cadastrada")
    

    quiz_status = "Realizado" if sistema_login.quiz_realizado else "Não realizado"
    print(f"Status do Quiz: {quiz_status}")
    
    fornecedores_status = "Selecionados" if sistema_login.fornecedores_selecionados else "Não selecionados"
    print(f"Status dos Fornecedores: {fornecedores_status}")
    
    buffet_status = "Selecionado" if sistema_login.buffet_selecionado else "Não selecionado"
    print(f"Status do Buffet: {buffet_status}")
    
    festa_status = "Criada" if sistema_login.festa_criada else "Não criada"
    print(f"Status da Festa: {festa_status}")
    
    evento_status = "Organizado" if sistema_login.evento_organizado else "Não organizado"
    print(f"Status do Evento: {evento_status}")
    
    convites_status = "Criados" if sistema_login.convites_criados else "Não criados"
    print(f"Status dos Convites: {convites_status}")

    if usuario.perfil and usuario.perfil.fornecedores_contratados:
        tipos_fornecedores = [f['tipo'].title() for f in usuario.perfil.fornecedores_contratados]
        print(f"Fornecedores Contratados: {', '.join(tipos_fornecedores)}")
    
    if usuario.perfil and hasattr(usuario.perfil, 'buffet_contratado') and usuario.perfil.buffet_contratado:
        buffet_tipo = usuario.perfil.buffet_contratado['tipo'].replace('_', ' ').title()
        print(f"Buffet Contratado: {buffet_tipo}")
    
    if usuario.perfil and hasattr(usuario.perfil, 'festa_criada') and usuario.perfil.festa_criada:
        festa_tipo = usuario.perfil.festa_criada['tipo'].replace('_', ' ').title()
        festa_nome = usuario.perfil.festa_criada['nome_aniversariante']
        print(f"Festa Criada: {festa_tipo} para {festa_nome}")
    
    if usuario.perfil and hasattr(usuario.perfil, 'evento_organizado') and usuario.perfil.evento_organizado:
        evento_nome = usuario.perfil.evento_organizado['nome']
        evento_fornecedores = usuario.perfil.evento_organizado['total_fornecedores']
        print(f"Evento Organizado: {evento_nome} ({evento_fornecedores} fornecedores)")
    
    if usuario.perfil and hasattr(usuario.perfil, 'convite_criado') and usuario.perfil.convite_criado:
        convite_tipo = usuario.perfil.convite_criado['tipo'].replace('_', ' ').title()
        convite_titulo = usuario.perfil.convite_criado['titulo']
        print(f"Convite Criado: {convite_tipo} - {convite_titulo}")

def editar_preferencias():
    """Permite editar as preferências do usuário"""
    usuario = sistema_login.usuario_logado
    print("\nEDITAR PREFERÊNCIAS")
    print(f"Preferências atuais: {', '.join(usuario.tagsDePreferencias)}")
    print()
    
    print("Digite suas novas preferências (separadas por vírgula):")
    tags_input = input("Ex: música, gastronomia, esportes: ")
    
    if tags_input.strip():
        novas_tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
        usuario.tagsDePreferencias = novas_tags
        print("Preferências atualizadas com sucesso!")
    else:
        print("ERRO: Nenhuma preferência informada.")

def criar_usuario_teste():
    """Função para criar um usuário através do terminal"""
    print("=== CADASTRO DE USUÁRIO ===")
    print()
    
    nome = input("Digite o nome: ")
    
    while True:
        try:
            data_str = input("Digite a data de nascimento (DD/MM/AAAA): ")
            dia, mes, ano = map(int, data_str.split('/'))
            data_nascimento = date(ano, mes, dia)
            break
        except ValueError:
            print("Formato inválido! Use DD/MM/AAAA")
    
    sobre_mim = input("Sobre você (opcional): ")
    if not sobre_mim.strip():
        sobre_mim = None
    
    print("Digite suas preferências (separadas por vírgula):")
    tags_input = input("Ex: música, gastronomia, esportes: ")
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
    
    try:
        usuario = Usuario(
            nome=nome,
            dataNascimento=data_nascimento,
            sobreMim=sobre_mim,
            tagsDePreferencias=tags
        )
        
        print("\nUsuário criado com sucesso!")
        print(f"Nome: {usuario.nome}")
        print(f"Data de Nascimento: {usuario.dataNascimento}")
        print(f"Sobre: {usuario.sobreMim}")
        print(f"Preferências: {', '.join(usuario.tagsDePreferencias)}")
        
        credenciais = sistema_login.criar_credenciais(usuario)
        print("\nCredenciais de login criadas:")
        print(f"Username: {credenciais['username']}")
        print(f"Password: {credenciais['password']}")
        print("(Anote essas informações para fazer login)")
        
        return usuario
        
    except Exception as e:
        print(f"ERRO ao criar usuário: {e}")
        return None

def menu_principal():
    """Menu principal do programa"""
    usuarios_cadastrados = []
    
    while True:
        if sistema_login.esta_logado():
            menu_usuario_logado()
            continue
            
        print("\n" + "="*40)
        print("    SISTEMA DE CADASTRO DE USUÁRIOS")
        print("="*40)
        print("1. Cadastrar novo usuário")
        print("2. Fazer login")
        print("3. Listar usuários cadastrados")
        print("4. Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            usuario = criar_usuario_teste()
            if usuario:
                usuarios_cadastrados.append(usuario)
                
                print("\nDeseja fazer login agora? (s/n)")
                if input().lower() in ['s', 'sim', 'y', 'yes']:
                    fazer_login()
                    
        elif opcao == "2":
            if not sistema_login.usuarios_login:
                print("\nNenhum usuário cadastrado ainda.")
            else:
                fazer_login()
                
        elif opcao == "3":
            if not usuarios_cadastrados:
                print("\nNenhum usuário cadastrado.")
            else:
                print(f"\nUsuários cadastrados ({len(usuarios_cadastrados)}):")
                print("-" * 50)
                for i, usuario in enumerate(usuarios_cadastrados, 1):
                    print(f"{i}. {usuario.nome} - {usuario.dataNascimento}")
                    if usuario.tagsDePreferencias:
                        print(f"   Preferências: {', '.join(usuario.tagsDePreferencias)}")
                    print()
                    
        elif opcao == "4":
            print("Saindo do sistema...")
            break
            
        else:
            print("ERRO: Opção inválida!")

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"\nERRO inesperado: {e}")
