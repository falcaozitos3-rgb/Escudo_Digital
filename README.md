# 🛡️ Escudo Digital

Sistema de análise inteligente de fraudes e golpes usando IA.

## 🎓 Projeto para Feira de Ciências

**Escudo Digital** é um projeto apresentado na **Feira de Ciências da Bahia**, desenvolvido com o objetivo de proteger pessoas que têm pouca ou nenhuma familiaridade com tecnologia, como **idosos e usuários iniciantes**.

## 📋 Sobre o Projeto

**Escudo Digital** é uma plataforma de cibersegurança desenvolvida com foco em:

- **Back-end robusto** - Processamento seguro de dados com Flask
- **Inteligência Artificial** - Análise em tempo real com Llama 3 via API Groq
- **Cibersegurança** - Detecção automática de fraudes, phishing e golpes

O frontend foi **totalmente desenvolvido com IA**, garantindo uma interface **simples, intuitiva e acessível** para qualquer pessoa, independentemente do seu nível de conhecimento técnico.

### 🎯 Público-alvo

- 👴 Idosos e pessoas da terceira idade
- 📱 Usuários iniciantes em tecnologia
- 🛡️ Qualquer pessoa que quer se proteger de fraudes online

## ⚠️ Status do Projeto

### ✅ Funcionalidades Ativas

- **IA Llama 3 Operacional** - Análise de textos em tempo real funcionando perfeitamente
- **Análise com Explicações Educativas** - A IA agora explica o que é phishing, fraude e golpes em linguagem simples
- **Banco de Dados Persistente** - Todas as análises são armazenadas corretamente
- **Interface Amigável** - Frontend totalmente otimizado para pessoas sem conhecimento técnico

### 🔨 Melhorias em Desenvolvimento

- **Validação de Entrada Robusta** - Bloquear comandos injections que possam travar a IA
- **Explicações Expandidas** - Detalhamento sobre:
  - 🎣 O que é **Phishing** (engenharia social)
  - 💰 O que é **Fraude** (roubo de informações)
  - 🚨 O que é **Golpe** (esquema fraudulento)
- **Rate Limiting** - Proteção contra abuso da API
- **Sanitização de Inputs** - Remover caracteres perigosos antes de enviar à IA

## 🚀 Tecnologias

- **Flask 3.1.0** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **Groq API** - Modelo Llama 3.3-70b para análise de IA
- **SQLite** - Banco de dados leve
- **Python 3** - Linguagem principal

## 📦 Instalação

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)

### Setup

1. Clone o repositório:
```bash
cd escudo_digital
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente (.env):
```bash
cp .env.example .env
# Adicione sua GROQ_API_KEY no arquivo .env
```

4. Execute a aplicação:
```bash
python3 app.py
```

A aplicação estará disponível em `http://127.0.0.1:5000`

## 🔧 Funcionalidades

### 1️⃣ Análise de Textos
Envie um texto suspeito e o sistema classifica em:
- ✅ **Seguro** - Nenhum risco detectado
- ⚠️ **Suspeito** - Possível risco
- 🚨 **Golpe** - Risco confirmado

### 2️⃣ Feed Comunitário
Visualize os últimos golpes reportados pela comunidade em tempo real.

### 3️⃣ Banco de Dados
Todas as análises são armazenadas para histórico e estatísticas futuras.

## 📂 Estrutura do Projeto

```
escudo_digital/
├── app.py                 # Aplicação principal Flask
├── banco_dados.py         # Modelos e inicialização do banco
├── requirements.txt       # Dependências do projeto
├── .env                   # Variáveis de ambiente (git-ignored)
├── .env.example           # Exemplo de .env
├── golpes.db              # Banco SQLite
├── static/                # Arquivos estáticos (CSS, JS)
├── templates/             # Templates HTML
└── README.md              # Este arquivo
```

## 🤖 Como Funciona a IA

1. Usuário submete um texto suspeito
2. Flask recebe a requisição e valida os dados
3. Prompt engineered é enviado ao Llama 3 via Groq
4. IA retorna análise em formato JSON estruturado com:
   - **nivel** - Classificação (seguro, suspeito, golpe)
   - **descricao** - Explicação técnica da análise
   - **educacao** - Explicação em linguagem simples sobre o tipo de risco (phishing, fraude, etc)
5. Resultado é armazenado no SQLite
6. Frontend exibe o resultado com animação e caixa educativa

## ⚙️ Configuração da API Groq

A aplicação utiliza a **Groq API** para rodar o modelo Llama 3.3-70b.

Para usar, você precisa:
1. Criar uma conta em [console.groq.com](https://console.groq.com)
2. Gerar uma chave de API
3. Adicionar no arquivo `.env`:
```env
GROQ_API_KEY=sua_chave_aqui
```

## 📝 Notas de Desenvolvimento

- ✅ **Análise com IA funcionando** - Llama 3 processando e explicando ameaças
- ✅ **Explicações educativas ativas** - Usuários recebem explicação simples
- 🔨 **Em desenvolvimento:**
  - Validação rigorosa para prevenir injection attacks
  - Expansão de explicações sobre termos técnicos
  - Limite de requisições (rate limiting)
  - Sanitização de inputs perigosos
  - Contribuições e feedback são bem-vindos
  - Mais pra frente será adicionado tambem sistema de lolalização por IP pra monitorar os casos em cada região.
-codifiicação do codigo

## 📞 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

---

**Desenvolvido com ❤️ e IA**
