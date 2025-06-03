# Sistema de Eventos - API FastAPI

Este projeto implementa uma API completa para gerenciamento de eventos, festas, convites e sugestões usando FastAPI com múltiplos padrões de projeto.

## Estrutura do Projeto

- `main.py` - Aplicação principal com endpoints FastAPI
- `models/` - Modelos Pydantic que representam as entidades do sistema
- `routes/` - Rotas organizadas por funcionalidade
- `patterns/` - Implementação de 6 padrões de projeto GoF
- `teste/` - Sistema de teste interativo completo
- `requirements.txt` - Dependências do projeto

## Instalação

### Pré-requisitos
- Python 3.8+
- pip

### Passos de Instalação

1. **Clone ou acesse o diretório do projeto**:
   ```bash
   cd "/home/leandro/Área de trabalho/2025.1-T01-_G4_QuemFazNiver_GostaDe_Entrega_03/backend"
   ```

2. **Crie um ambiente virtual Python**:
   ```bash
   python3 -m venv venv
   ```

3. **Ative o ambiente virtual**:
   - **Linux/Mac**: 
     ```bash
     source venv/bin/activate
     ```
   - **Windows**: 
     ```bash
     venv\Scripts\activate
     ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

### Solução de Problemas

Se você encontrar o erro `externally-managed-environment`:

1. **Certifique-se de que o ambiente virtual está ativo**:
   ```bash
   which pip  # Deve mostrar o caminho do venv
   ```

2. **Se o problema persistir, tente**:
   ```bash
   # Desative e recrie o ambiente virtual
   deactivate
   rm -rf venv
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Ou use o pip diretamente do ambiente virtual**:
   ```bash
   ./venv/bin/pip install -r requirements.txt
   ```

4. **Para sistemas Ubuntu/Debian, instale o python3-full**:
   ```bash
   sudo apt install python3-full python3-venv
   ```

## Executando a API

1. **Certifique-se de que o ambiente virtual está ativo**:
   ```bash
   source venv/bin/activate  # Linux/Mac
   ```

2. **Execute a aplicação**:
   ```bash
   uvicorn main:app --reload
   ```

3. **Acesse a API**:
   - API: `http://localhost:8000`
   - Documentação Swagger: `http://localhost:8000/docs`
   - Documentação ReDoc: `http://localhost:8000/redoc`

## Padrões de Projeto Implementados

### 1. Factory Method
O padrão Factory Method foi implementado no sistema de notificações e fornecedores, permitindo:
- Criação de diferentes tipos de notificação (Email, WhatsApp, Telegram)
- Criação de diferentes fornecedores (Pizzaria, Confeitaria, Churrascaria)
- Extensibilidade para adicionar novos canais e fornecedores
- Separação da lógica de criação da lógica de uso

### 2. Builder Pattern
Implementado para criação de festas com diferentes configurações:
- `FestaBasicaBuilder`: Cria festas com configurações padrão
- `FestaPersonalizadaBuilder`: Permite personalização completa
- `FestaDirector`: Coordena o processo de construção
- Separação entre construção e representação

### 3. Template Method
Utilizado para criação de portfólios de buffets:
- `PortifolioBuffet`: Template para buffets tradicionais
- `PortifolioConfeitaria`: Template para confeitarias especializadas
- Algoritmo base comum com variações específicas
- Reutilização de código e flexibilidade

### 4. Composite Pattern
Implementado em duas áreas:
- **Quiz de Personalidade**: Combina diferentes tipos de perguntas (Preferência, Temática, Localidade, Estilo, Comida)
- **Organização de Eventos**: Coordena fornecedores (Banda, Local, Segurança, Decoração, Comida)
- Permite tratamento uniforme de objetos individuais e composições

### 5. Observer Pattern
Sistema de notificações automáticas:
- Inscrição de observadores para eventos específicos
- Notificação automática sobre mudanças (novos convidados, desejos adquiridos)
- Desacoplamento entre publishers e subscribers

### 6. Decorator Pattern
Sistema de convites com funcionalidades incrementais:
- `ConviteConcreto`: Convite básico
- `DecoratorInterativo`: Adiciona mapas, carrossel, comentários
- `DecoratorLuxo`: Adiciona vídeos, sons, tipografia personalizada
- Extensão de funcionalidades sem modificar código base

## Fluxo Completo do Sistema

1. **Cadastro e Login de Usuário**
2. **Quiz de Personalidade** (Composite Pattern)
3. **Seleção de Fornecedores** (Factory Method)
4. **Seleção de Buffet** (Template Method)
5. **Criação de Festa** (Builder Pattern)
6. **Organização de Evento** (Composite Pattern)
7. **Criação de Convites** (Decorator Pattern)

## Teste Interativo

O sistema inclui um módulo de teste completo (`teste/teste.py`) que demonstra todos os padrões em funcionamento através de uma interface de terminal interativa.

Para executar os testes:
```bash
python teste/teste.py
```

## Recursos Implementados

- Gerenciamento de usuários
- Criação e gestão de festas
- Adição de convidados
- Lista de desejos
- Sistema de convites
- Recomendação de fornecedores
- Sistema de notificações (Factory Method)

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados e serialização
- **Uvicorn**: Servidor ASGI de alta performance
- **Python-Jose**: Manipulação de tokens JWT
- **Passlib**: Hash de senhas seguro
- **Email-Validator**: Validação de endereços de email

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
