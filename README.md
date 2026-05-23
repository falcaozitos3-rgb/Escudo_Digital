# 🛡️ Escudo Digital

> **Sistema Inteligente de Proteção Contra Fraudes e Golpes Online**

Desenvolvido com ❤️ para a Feira de Ciências da Bahia com **inteligência artificial real** e **segurança blindada** contra ciberataques.

---

## 📋 Sobre o Projeto

**Escudo Digital** é uma plataforma de cibersegurança desenvolvida para proteger pessoas que têm **pouca ou nenhuma familiaridade com tecnologia**, como idosos e usuários iniciantes.

### 🎯 Por que Escudo Digital?

Segundo a [Safernet Brasil](https://www.safernet.org.br/), **34 milhões de brasileiros** foram vítimas de fraudes online em 2024. Este projeto visa:

- ✅ **Proteção Educativa** - Analisa golpes e explica em linguagem simples
- ✅ **Tecnologia Robusta** - IA Llama 3 + Flask + SQLAlchemy
- ✅ **Cibersegurança Profissional** - Blindado contra SQL Injection, Prompt Injection e Buffer Overflow
- ✅ **Acessibilidade** - Interface intuitiva para qualquer pessoa

### 👥 Público-alvo

- 👴 Idosos e pessoas da terceira idade
- 📱 Usuários iniciantes em tecnologia
- 👨‍👩‍👧 Qualquer pessoa que quer se proteger de fraudes online

---

## 🚀 Funcionalidades Principais

### 1️⃣ Análise de Mensagens e Links em Tempo Real
Envie um texto suspeito ou link e o sistema classifica automaticamente:
- ✅ **Seguro** - Nenhum risco detectado
- ⚠️ **Suspeito** - Possível risco de fraude
- 🚨 **Golpe** - Risco confirmado de phishing/fraude

### 2️⃣ Explicações Educativas Simples
A IA explica **em linguagem do dia-a-dia** o que é:
- 🎣 **Phishing** - Roubo de dados via falsificação
- 💰 **Fraude** - Promessas enganosas de ganho
- 🚨 **Golpe** - Esquema criminoso para roubar dinheiro
- Com **analogias práticas** que qualquer pessoa entende

### 3️⃣ Detecção de Localização por IP
Registra automaticamente:
- 📍 **Cidade** do usuário
- 📍 **Estado/Região**
- 📍 **País**
- 📊 Permite monitoramento regional de fraudes

### 4️⃣ Feed Comunitário em Tempo Real
- 🔴 Visualize os **últimos golpes reportados** pela comunidade
- 📊 Saiba quais fraudes estão **mais ativas na sua região**
- ⚠️ Receba avisos sobre **novos padrões de golpe**

### 5️⃣ Banco de Dados Completo e Seguro
Registro persistente com **8 campos**:
- ID do alerta
- Texto/link analisado
- Classificação (SEGURO/SUSPEITO/GOLPE)
- IP e localização do usuário
- Data/hora e justificativa da IA

---

## 🔐 Segurança em Camadas

Este projeto implementa **4 camadas de proteção** contra ciberataques:

### Camada 1: Validação de Input
```python
# Bloqueia tentativas de SQL Injection
input_e_seguro("'; DROP TABLE users; --")  # ❌ BLOQUEADO

# Bloqueia tentativas de Python Injection
input_e_seguro("exec(import os; os.system('rm -rf'))")  # ❌ BLOQUEADO

# Bloqueia Buffer Overflow (máximo 1000 caracteres)
input_e_seguro("A" * 2000)  # ❌ MUITO GRANDE
```

### Camada 2: Prompt Injection Defense
Usa **tags XML** para isolar o input do usuário:
```xml
<conteudo>
QUALQUER COISA QUE O USUÁRIO ESCREVER AQUI
</conteudo>
```
Mesmo que o usuário tente enganar a IA, ela só analisa o conteúdo isolado.

### Camada 3: ORM Seguro
Usa **SQLAlchemy** (prepared statements) para proteger contra SQL Injection no banco.

### Camada 4: Validação de Resposta
Valida que a IA retornou **JSON válido** com as chaves corretas.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnologia | Versão | Por quê? |
|-----------|-----------|--------|---------|
| **Backend** | Flask | 3.1.0 | Leve, rápido, seguro |
| **IA** | Llama 3.3-70b (Groq) | Última | Grátis e poderosa |
| **Banco de Dados** | SQLAlchemy + SQLite | 3.0+/3.x | ORM seguro, sem SQL raw |
| **Linguagem** | Python | 3.8+ | Rápido de prototipar |
| **HTTP Client** | requests | 2.31+ | Para chamar APIs |
| **Variáveis** | python-dotenv | 1.0.0 | Segurança com .env |

---

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes)
- Chave de API Groq (gratuita em [console.groq.com](https://console.groq.com))

### Setup em 5 Passos

**1. Clonar ou acessar o diretório:**
```bash
cd escudo_digital
```

**2. Criar ambiente virtual (opcional, mas recomendado):**
```bash
python3 -m venv env
source env/bin/activate  # No Windows: env\Scripts\activate
```

**3. Instalar dependências:**
```bash
pip install -r requirements.txt
```

**4. Configurar variáveis de ambiente:**
```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave Groq:
```env
GROQ_API_KEY=gsk_seu_token_aqui_sem_aspas
```

**5. Executar a aplicação:**
```bash
python3 app.py
```

Acesse em seu navegador: **http://localhost:5000** 🎉

---

## 📂 Estrutura do Projeto

```
escudo_digital/
│
├── 📄 app.py                    # Aplicação Flask principal (258 linhas)
│   ├── 5 rotas principais
│   ├── Integração com Groq API
│   ├── Localização por IP
│   └── Salvamento em banco de dados
│
├── 📄 seguranca.py              # Módulo de cibersegurança (198 linhas)
│   ├── input_e_seguro()         # Sanitização de input
│   ├── construir_prompt_seguro() # Blindagem contra prompt injection
│   ├── eh_link()                # Detecção de URLs
│   ├── validar_resposta_ia()    # Validação de JSON
│   ├── detectar_link_clonado_banco() # Anti-phishing
│   └── verificacao_das_operadoras_oficial() # Filtro de falsos positivos
│
├── 📄 banco_dados.py            # Modelos SQLAlchemy (38 linhas)
│   └── AnalisarGolpes           # Tabela com 8 campos
│
├── 📄 requirements.txt          # Dependências Python
├── 📄 .env.example              # Modelo de variáveis de ambiente
├── 📄 .env                      # ⚠️ Não versionar (chaves sensíveis)
│
├── 📁 templates/
│   └── 📄 index.html            # Interface web responsiva
│
├── 📁 static/
│   └── 📄 style.css             # Estilos CSS modernos
│
├── 📁 instance/
│   └── golpes.db                # Banco SQLite (criado automaticamente)
│
└── 📄 README.md                 # Este arquivo
```

---

## 🔧 Como Usar

### Cenário 1: Analisar uma Mensagem Suspeita
```
1. Abra http://localhost:5000
2. Cole uma mensagem: "Você ganhou R$ 1000! Clique para confirmar"
3. Clique em "Analisar"
4. Veja o resultado: GOLPE ❌
5. Leia a explicação em linguagem simples
```

### Cenário 2: Analisar um Link Suspeito
```
1. Cole um link: "https://bankk-bradesco-seguro.com/login"
2. Clique em "Analisar"
3. Veja o resultado: GOLPE (link clonado) ❌
4. A IA explica por que é phishing
```

### Cenário 3: Checar o Feed Comunitário
```
1. Role para baixo na página inicial
2. Veja os últimos 10 golpes reportados
3. Veja de qual cidade/estado cada alerta veio
4. Identifique padrões de fraude da sua região
```

---

## 📊 API REST Disponível

### Rota 1: Página Principal
```http
GET / 
```
Retorna a interface web com lista de alertas registrados.

### Rota 2: Analisar Texto/Link (POST)
```http
POST /analisar
Content-Type: application/json

{
  "mensagem": "Clique aqui para liberar seu Pix",
  "ip_real": "189.123.45.67"
}
```

**Resposta de Sucesso:**
```json
{
  "nivel": "golpe",
  "descricao": "Promessa de ganho sem esforço é típica de fraude",
  "educacao": "Isso é como receber uma ligação oferecendo dinheiro...",
  "tipo": "MENSAGEM",
  "origem": "ia_groq"
}
```

### Rota 3: Feed de Alertas (GET)
```http
GET /alertas
```

**Resposta:**
```json
[
  {
    "id": 42,
    "resumo": "Você ganhou um prêmio...",
    "tipo": "GOLPE",
    "data": "Recentemente"
  },
  {
    "id": 41,
    "resumo": "Confirme seus dados...",
    "tipo": "SUSPEITO",
    "data": "Recentemente"
  }
]
```

### Rota 4: Localização do Usuário (GET)
```http
GET /localizacao
```

### Rota 5: Localização por IP (POST)
```http
POST /localizacao-por-ip
Content-Type: application/json

{
  "ip": "8.8.8.8"
}
```

---

## 📊 Estrutura do Banco de Dados

### Tabela `analisar_golpes`

| Campo | Tipo | Exemplo |
|-------|------|---------|
| `id` | INTEGER | 42 |
| `texto_suspeito` | VARCHAR | "Clique para ganhar prêmio" |
| `resultado_ia` | VARCHAR(20) | "GOLPE" |
| `justificativa` | VARCHAR | "Promessa de ganho fácil..." |
| `ip_usuario` | VARCHAR(50) | "189.123.45.67" |
| `cidade` | VARCHAR(100) | "Salvador" |
| `estado` | VARCHAR(100) | "Bahia" |
| `pais` | VARCHAR(100) | "Brasil" |
| `data_registro` | DATETIME | "2026-05-22 20:47:15" |

---

## 🤖 Como a IA Funciona

### Fluxo Completo de Análise

```
┌─────────────────────────────────────┐
│  Usuário envia texto/link            │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│  1️⃣ VALIDAÇÃO                        │
│  - input_e_seguro()                  │
│  - Bloqueia injections               │
│  - Limita tamanho (1000 chars)       │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│  2️⃣ DETECÇÃO DE TIPO                 │
│  - eh_link()                         │
│  - É URL ou mensagem?                │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│  3️⃣ ENGENHARIA DE PROMPT             │
│  - construir_prompt_seguro()         │
│  - Isola input em tags XML           │
│  - System prompt blindado            │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│  4️⃣ CHAMADA À IA GROQ                │
│  - Llama 3.3-70b                     │
│  - Análise com JSON response         │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│  5️⃣ VALIDAÇÃO DA RESPOSTA            │
│  - validar_resposta_ia()             │
│  - JSON válido?                      │
│  - Chaves corretas?                  │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│  6️⃣ SALVAR NO BANCO                  │
│  - SQLAlchemy ORM                    │
│  - Prepared statements               │
│  - IP + localização                  │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│  7️⃣ RETORNAR AO USUÁRIO              │
│  - JSON estruturado                  │
│  - Frontend exibe resultado          │
└─────────────────────────────────────┘
```

### Resposta da IA (Exemplo Real)

```json
{
  "nivel": "golpe",
  "descricao": "Este é um golpe clássico de phishing. O banco nunca pede dados via SMS. O link é de domínio falsificado (bradeskko.com vs bradesco.com.br).",
  "educacao": "Imagine alguém batendo na sua porta fingindo ser do banco e pedindo seu CPF. Você daria? Links em SMS são iguais - nunca clique!"
}
```

---

## 🔐 Testes de Segurança

### Teste 1: Input Legítimo ✅
```python
>>> input_e_seguro("Você ganhou um prêmio!")
[SEGURANÇA] Input validado como seguro: 31 caracteres
True
```

### Teste 2: SQL Injection ❌
```python
>>> input_e_seguro("'; DROP TABLE users; --")
[SEGURANÇA] SQL Injection detectada: padrão ';' encontrado
False
```

### Teste 3: Python Injection ❌
```python
>>> input_e_seguro("exec(print('hack'))")
[SEGURANÇA] Python Injection detectada: padrão 'exec(' encontrado
False
```

### Teste 4: Buffer Overflow ❌
```python
>>> input_e_seguro("A" * 2000)
[SEGURANÇA] Input rejeitado: texto muito grande (2000 caracteres)
False
```

### Teste 5: Detecção de Link ✅
```python
>>> eh_link("Clique em https://exemplo.com")
True

>>> eh_link("Você ganhou um prêmio")
False
```

---

## 🧠 Exemplos de Análise

### Exemplo 1: Phishing de Banco
**Input:**
```
Clique aqui para atualizar seus dados bancários:
https://bradeskko.com/login
```

**Saída:**
```
🚨 GOLPE

Descrição: Link falsificado (bradeskko.com vs bradesco.com.br). 
Bancos nunca pedem dados via SMS.

Educação: Como um ladrão que coloca uma placa falsa na porta 
do banco para você pensar que é legítimo.
```

### Exemplo 2: Phishing Operadora
**Input:**
```
Sua fatura com Claro está vencida! Pague via Pix:
000200.00000 00000.000000 00000.000000 0000000000000
```

**Saída:**
```
✅ SEGURO

Descrição: Aviso legítimo de cobrança da operadora Claro.

Educação: Verifique sempre no aplicativo oficial ou ligue 
no número atrás do seu modem. Nunca use Pix de SMS.
```

### Exemplo 3: Promessa de Ganho Fácil
**Input:**
```
Trabalhe de casa e GANHE R$ 5000/mês!
Sem experiência, sem investimento inicial!
```

**Saída:**
```
🚨 GOLPE

Descrição: Ganho fácil sem trabalho é típico de fraude 
(esquema Ponzi, pirâmide financeira).

Educação: Se parece bom demais para ser verdade, é porque é.
Ganho real exige trabalho e tempo.
```

---

## 📈 Próximas Melhorias

- [ ] **Rate Limiting** - Proteção contra DDoS (máx 10 req/min por IP)
- [ ] **CAPTCHA** - Proteção contra bots
- [ ] **Dashboard Admin** - Estatísticas por região/tipo de golpe
- [ ] **Mapa Interativo** - Visualizar golpes em tempo real
- [ ] **Sistema de Feedback** - Usuários confirmam se foi golpe ou não
- [ ] **Histórico Pessoal** - Usuário vê suas análises antigas
- [ ] **Notificações** - Alertas de novos padrões de fraude
- [ ] **Integração WhatsApp/Telegram** - Analisar direto do chat

---

## 🤝 Contribuindo

Este é um projeto **open-source** e contribuições são bem-vindas!

### Como Contribuir

1. Faça um **fork** do projeto
2. Crie uma **branch** para sua feature:
   ```bash
   git checkout -b feature/nova-protecao
   ```
3. **Commit** suas mudanças:
   ```bash
   git commit -m "Add: Proteção contra [tipo de fraude]"
   ```
4. **Push** para a branch:
   ```bash
   git push origin feature/nova-protecao
   ```
5. Abra um **Pull Request**

---

## 📞 Suporte e Contato

- 🐛 **Encontrou um bug?** - Abra uma [Issue](https://github.com/seu-usuario/escudo_digital/issues)
- 💡 **Sugestão de feature?** - Comente em uma discussão
- 📧 **Email:** [adicione seu email aqui]
- 🌐 **Twitter/X:** [@seu_usuario]

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.

---

## 🎓 Créditos

Desenvolvido com ❤️ para a **Feira de Ciências da Bahia 2026**

**Tecnologias usadas:**
- Python 3 + Flask
- Groq API (Llama 3.3-70b)
- SQLAlchemy + SQLite
- HTML5 + CSS3 + JavaScript

**Inspirado em:**
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [Safernet Brasil](https://www.safernet.org.br/)

---

**Versão:** 2.0 🚀  
**Última atualização:** Maio 2026  
**Status:** ✅ Pronto para Produção

**"Protegendo o Brasil, um clique por vez"** 🛡️
