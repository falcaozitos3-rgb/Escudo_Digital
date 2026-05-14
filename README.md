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

Este projeto está em **desenvolvimento ativo** e contém algumas falhas que estamos resolvendo progressivamente. Novas features e correções são constantemente implementadas para melhorar a estabilidade e funcionalidade do sistema.

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
4. IA retorna análise em formato JSON estruturado
5. Resultado é armazenado no SQLite
6. Frontend exibe o resultado com animação

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

- O projeto está em fase de desenvolvimento
- Há bugs conhecidos sendo trabalhados
- Melhorias contínuas são implementadas regularmente
- Contribuições e feedback são bem-vindos

## 📞 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

---

**Desenvolvido com ❤️ e IA**
