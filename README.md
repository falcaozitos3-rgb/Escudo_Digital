# 🛡️ Escudo Digital

**Sistema Inteligente de Proteção Contra Fraudes e Golpes Online**

Desenvolvido com ❤️ para a Feira de Ciências da Bahia

## 🎓 Projeto para Feira de Ciências

**Escudo Digital** é uma plataforma de cibersegurança desenvolvida com o objetivo de proteger pessoas que têm pouca ou nenhuma familiaridade com tecnologia, como **idosos e usuários iniciantes**.

## 📋 Sobre o Projeto

**Escudo Digital** é uma plataforma de cibersegurança **100% segura** desenvolvida com foco em:

- **✅ Back-end Robusto** - Processamento seguro com Flask + SQLAlchemy
- **✅ Inteligência Artificial** - Análise em tempo real com Llama 3.3-70b via Groq API
- **✅ Cibersegurança Blindada** - Proteção contra SQL Injection, Prompt Injection e Buffer Overflow
- **✅ Localização por IP** - Detecção de região do usuário para monitoramento regional
- **✅ Interface Acessível** - Simples, intuitiva e otimizada para qualquer pessoa

O frontend foi **totalmente desenvolvido com IA**, garantindo uma interface **amigável** para qualquer pessoa, independentemente do seu nível de conhecimento técnico.

### 🎯 Público-alvo

- 👴 Idosos e pessoas da terceira idade
- 📱 Usuários iniciantes em tecnologia
- 👨‍👩‍👧 Qualquer pessoa que quer se proteger de fraudes online

## ⚠️ Status do Projeto

### ✅ Funcionalidades Implementadas

- **IA Llama 3 Operacional** - Análise de textos/links em tempo real
- **Análise Educativa** - IA explica o risco em linguagem simples
- **Banco de Dados Completo** - 8 campos: ID, texto, resultado, IP, cidade, estado, país, data
- **Interface Amigável** - Frontend responsivo e acessível
- **Detecção de IP e Localização** - Identifica região do usuário automaticamente
- **🔐 Camada de Segurança Avançada** - Proteção contra injeções e ataques

### 🔐 Novas Proteções de Segurança (v2.0)

- **✅ SQL Injection** - Bloqueado por validação + SQLAlchemy ORM
- **✅ Prompt Injection** - Bloqueado com tags XML + system prompt blindado
- **✅ Buffer Overflow** - Limite de 1000 caracteres por requisição
- **✅ Python Injection** - Bloqueio de `eval()`, `exec()`, etc

## 🚀 Tecnologias

| Componente | Tecnologia | Versão |
|-----------|-----------|--------|
| **Backend** | Flask | 3.1.0+ |
| **IA** | Llama 3.3-70b (Groq) | Última |
| **ORM** | SQLAlchemy | 3.0+ |
| **Banco** | SQLite | 3.x |
| **Linguagem** | Python | 3.8+ |
| **Requests** | requests | 2.31+ |

## 📦 Instalação

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)
- Chave de API da Groq (gratuita em [console.groq.com](https://console.groq.com))

### Setup Rápido

1. **Clone o repositório:**
```bash
cd escudo_digital
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente:**
```bash
cp .env.example .env
# Edite .env e adicione sua GROQ_API_KEY
```

4. **Execute a aplicação:**
```bash
python3 app.py
```

Acesse em: **http://localhost:5000**

## 🔧 Funcionalidades

### 1️⃣ Análise de Mensagens/Links
Envie um texto suspeito ou link e o sistema classifica em:
- ✅ **Seguro** - Nenhum risco detectado
- ⚠️ **Suspeito** - Possível risco de fraude
- 🚨 **Golpe** - Risco confirmado de phishing/fraude

### 2️⃣ Explicações Educativas
A IA explica em **linguagem simples do dia-a-dia**:
- 🎣 O que é phishing
- 💰 O que é fraude
- 🚨 O que é golpe
- Exemplos práticos e analogias

### 3️⃣ Localização por IP
Detecta automaticamente:
- 📍 Cidade do usuário
- 📍 Estado/Região
- 📍 País
- 📊 Monitoramento de alertas por região

### 4️⃣ Feed Comunitário em Tempo Real
Visualize os últimos golpes reportados pela comunidade (Top 10)

### 5️⃣ Banco de Dados Completo
Registro persistente com:
- ID do alerta
- Texto suspeito analisado
- Resultado (SEGURO/SUSPEITO/GOLPE)
- IP do usuário
- Localização (cidade, estado, país)
- Data/Hora da análise
- Justificativa da IA

## 📂 Estrutura do Projeto

```
escudo_digital/
├── 📄 app.py                  # Aplicação principal Flask (10 rotas)
├── 📄 banco_dados.py          # Modelos SQLAlchemy (campos de localização)
├── 🔐 seguranca.py            # Camada de segurança (4 funções)
├── 📄 requirements.txt        # Dependências Python
├── 📄 .env                    # Variáveis de ambiente (GROQ_API_KEY)
├── 📄 .env.example            # Exemplo de .env
├── 📁 static/
│   └── 📄 style.css          # Estilos CSS responsivos
├── 📁 templates/
│   └── 📄 index.html         # Interface principal
├── 📄 golpes.db              # Banco SQLite (criado automaticamente)
└── 📄 README.md              # Este arquivo
```

## 🔐 Camada de Segurança (Novo!)

### Funções de Proteção (`seguranca.py`)

#### 1. `input_e_seguro(texto_usuario)`
Valida entrada do usuário contra:
- ✅ SQL Injection (bloqueia `;`, `--`, `OR 1=1`, etc)
- ✅ Python Injection (bloqueia `eval()`, `exec()`, etc)
- ✅ Buffer Overflow (máximo 1000 caracteres)

**Exemplo:**
```python
if input_e_seguro(mensagem):
    processar(mensagem)
else:
    print("Input malicioso detectado!")
```

#### 2. `construir_prompt_seguro(conteudo, eh_link=False)`
Cria prompt blindado contra Prompt Injection:
- ✅ System prompt com regras invioláveis
- ✅ Input isolado em tags XML
- ✅ Instrução explícita de ignorar comandos do usuário

**Exemplo:**
```python
mensagens = construir_prompt_seguro("Clique em https://fake.com", eh_link=True)
# Retorna prompt estruturado com proteção
```

#### 3. `eh_link(texto)`
Detecta se é URL ou mensagem:
- ✅ Detecta http://, https://, ftp://, www.
- ✅ Usa regex para padrões comuns

#### 4. `validar_resposta_ia(resposta_texto)`
Valida resposta da IA:
- ✅ JSON válido
- ✅ Chaves obrigatórias (nivel, descricao, educacao)
- ✅ Tipos de dados corretos

### Fluxo de Segurança Completo

```
Usuário envia mensagem
    ↓
✅ input_e_seguro() - Valida contra injections
    ↓
✅ eh_link() - Detecta tipo de conteúdo
    ↓
✅ construir_prompt_seguro() - Cria prompt com tags XML
    ↓
✅ Envia para Llama 3 com isolamento
    ↓
✅ validar_resposta_ia() - Valida resposta
    ↓
✅ SQLAlchemy ORM - Salva no banco (Prepared Statements)
    ↓
✅ Retorna resultado ao frontend
```

## 🤖 Como Funciona a IA

1. Usuário submete texto/link suspeito
2. Flask valida entrada contra injeções
3. Prompt é construído com tags XML para segurança
4. Llama 3.3-70b analisa via Groq API
5. IA retorna JSON estruturado:
   ```json
   {
     "nivel": "golpe",
     "descricao": "Promessa de ganho fácil é característica de fraude",
     "educacao": "Isso é como um vendedor oferecendo dinheiro grátis na rua..."
   }
   ```
6. Resultado é armazenado no SQLite com IP e localização
7. Frontend exibe com animação e explicação educativa

## ⚙️ Configuração da API Groq

A aplicação utiliza a **Groq API** com o modelo **Llama 3.3-70b** (gratuito até certos limites).

### Setup de API Key

1. Acesse [console.groq.com](https://console.groq.com)
2. Crie uma conta (gratuita)
3. Gere uma chave de API
4. Adicione ao arquivo `.env`:

```env
GROQ_API_KEY=sua_chave_aqui_sem_aspas
```

## 📝 Rotas Disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET/POST | Página principal com lista de alertas |
| `/analisar` | POST | API de análise (JSON) |
| `/alertas` | GET | Feed comunitário (Top 10) |
| `/localizacao` | GET | Localização do usuário |
| `/localizacao-por-ip` | POST | Localização de um IP específico |

## 📊 Estrutura do Banco de Dados

### Tabela: `analisar_golpes`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | INTEGER | ID único |
| `texto_suspeito` | VARCHAR | Texto/link analisado |
| `resultado_ia` | VARCHAR(20) | SEGURO/SUSPEITO/GOLPE |
| `justificativa` | VARCHAR | Explicação da análise |
| `ip_usuario` | VARCHAR(50) | IP do usuário |
| `cidade` | VARCHAR(100) | Cidade detectada |
| `estado` | VARCHAR(100) | Estado/Região |
| `pais` | VARCHAR(100) | País |
| `data_registro` | DATETIME | Data/hora da análise |

## 🧪 Testes de Segurança

Todos os testes passaram ✅:

```
✅ Input legítimo: "Você ganhou um prêmio!"
   Resultado: APROVADO

✅ SQL Injection: "'; DROP TABLE users; --"
   Resultado: BLOQUEADO

✅ Python Injection: "exec(print('hack'))"
   Resultado: BLOQUEADO

✅ Detecção de links: "Clique em https://exemplo.com"
   Resultado: LINK DETECTADO

✅ Validação de prompt: Tags XML + System prompt
   Resultado: BLINDADO
```

## 📈 Próximas Melhorias

- [ ] Rate limiting (proteção contra DDoS)
- [ ] CAPTCHA para análises
- [ ] Dashboard com estatísticas por região
- [ ] Mapa interativo de alertas
- [ ] Sistema de feedback do usuário
- [ ] Histórico pessoal de análises
- [ ] Integração com redes sociais

## 📝 Notas de Desenvolvimento

- ✅ **Segurança** - Blindagem contra SQL Injection, Prompt Injection, Buffer Overflow
- ✅ **IA Funcionando** - Llama 3 processando análises em tempo real
- ✅ **Banco Completo** - 8 campos com IP e localização
- ✅ **Explicações Educativas** - IA explica em linguagem simples
- ✅ **Interface Responsiva** - Funciona em desktop/mobile

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:
1. Faça um fork
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Contato

Para dúvidas, sugestões ou reportar bugs:
- Abra uma issue no repositório
- Email: [Seu Email]

---

**Desenvolvido com ❤️, Python e IA para proteger a comunidade**

**Versão:** 2.0 (com camada de segurança)  
**Última atualização:** Mai 2026  
**Status:** ✅ Pronto para produção
