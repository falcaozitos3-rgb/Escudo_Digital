# ==============================================================================
#  IMPORTAÇÕES DAS BIBLIOTECAS E MÓDULOS
# ==============================================================================
# Importa as ferramentas principais do Flask para criar as rotas e gerenciar o site
from flask import Flask, render_template, request, jsonify

# Importa o carregador de variáveis de ambiente (.env)
from dotenv import load_dotenv

# Importa o cliente oficial da Groq para conectar o modelo Llama 3
from groq import Groq

# Importa as ferramentas de banco de dados do seu arquivo separado 'banco_dados.py'
from banco_dados import db, AnalisarGolpes, inicializar_banco

# Importa bibliotecas nativas do Python para gerenciar o sistema e ler formatos JSON
import os
import json

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# ==============================================================================
# CONFIGURAÇÃO DO SERVIDOR FLASK E BANCO DE DADOS
# ==============================================================================
# Inicializa o servidor web principal do Flask
app = Flask(__name__)

# Configura o caminho absoluto exato para o banco SQLite dentro da sua pasta de trabalho
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////./home/evaristo/escudo_digital/golpes.db'

# Desativa o monitoramento de modificações para economizar memória RAM no seu Celeron
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Executa a função do seu arquivo separado para ligar o banco de dados ao servidor Flask
inicializar_banco(app)

# Inicializa o motor da IA (ele vai ler a chave 'GROQ_API_KEY' injetada no terminal)
client = Groq()

# ==============================================================================
#  ROTA 1: PÁGINA PRINCIPAL DO SITE (MÉTODO GET E POST)
# ==============================================================================
# Rota raiz que entrega o site bonito do Claude e processa envios tradicionais de formulário
@app.route('/', methods=['GET', 'POST'])
def index():
    # Verifica se o usuário enviou algum dado através do formulário clássico
    if request.method == 'POST':
        texto_recebido = request.form.get('mensagem')

        # Se houver texto, salva temporariamente no banco (fluxo básico de segurança)
        if texto_recebido:
            novo_alerta = AnalisarGolpes(texto_suspeito=texto_recebido)
            db.session.add(novo_alerta)
            db.session.commit()
            print(f"[BANCO DE DADOS] Salvo com êxito! {texto_recebido}")

    # Fora do bloco IF (roda tanto no GET quanto no POST) para listar os alertas na tela
    alertas_registrados = AnalisarGolpes.query.order_by(AnalisarGolpes.id.desc()).all()
    return render_template('index.html', alertas=alertas_registrados)

# ==============================================================================
#  ROTA 2: API DE ANÁLISE COMPLETA VIA IA LLAMA 3 (MÉTODO POST VIA JAVASCRIPT)
# ==============================================================================
# Rota usada pelo JavaScript do Claude para rodar a animação de análise sem travar a tela
@app.route('/analisar', methods=['POST'])
def analisar():
    # Captura os dados no formato JSON enviados pelo JavaScript de fundo da página
    data = request.get_json()
    mensagem = data.get('mensagem', '').strip()
    
    # Validação básica de cibersegurança: rejeita envios vazios antes de gastar cota da IA
    if not mensagem:
        return jsonify({'nivel': 'seguro', 'descricao': 'Nenhuma mensagem enviada.'}), 400
    
    # Engenharia de Prompt: Blinda e força o Llama 3 a retornar uma estrutura JSON pura e limpa
    prompt = (
        "Você é um especialista em segurança que explica termos técnicos de forma simples para pessoas sem conhecimento de tecnologia. "
        "Analise o seguinte texto e determine se é um golpe, phishing ou fraude. "
        "Responda estritamente no formato JSON com TRÊS chaves de letras minúsculas: "
        "'nivel' (valores possíveis: seguro, suspeito ou golpe), "
        "'descricao' (explicação curta em português do porquê dessa classificação) e "
        "'educacao' (se for suspeito ou golpe, explique em linguagem MUITO SIMPLES o que é phishing/golpe/fraude e por que este é um exemplo, use analogias do dia a dia).\n\n"
        f"Texto: {mensagem}"
    )
    
    try:
        # Dispara a requisição em nuvem para o modelo Llama 3 mais rápido e preciso da Groq
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        # Converte a resposta em texto cru enviada pela IA em um dicionário Python tratável
        resultado_ia = json.loads(completion.choices[0].message.content)
        nivel = resultado_ia.get('nivel', 'suspeito')
        descricao = resultado_ia.get('descricao', 'Análise inconclusiva.')
        educacao = resultado_ia.get('educacao', '')
        
        # Cria e popula o novo registro no banco de dados SQLite unindo o texto e o veredito da IA
        novo_alerta = AnalisarGolpes(
            texto_suspeito=mensagem, 
            resultado_ia=nivel.upper(),  # Transforma o status em maiúsculo (GOLPE, SUSPEITO)
            justificativa=descricao
        )
        db.session.add(novo_alerta)
        db.session.commit()
        
        # Devolve o resultado formatado para o JavaScript atualizar a tela do usuário na hora
        return jsonify({'nivel': nivel, 'descricao': descricao, 'educacao': educacao})
        
    except Exception as e:
        # Se a conexão falhar ou a API cair, evita tela preta e retorna o erro com código HTTP 500
        return jsonify({'nivel': 'erro', 'descricao': f'Erro ao processar com a IA: {str(e)}'}), 500

# ==============================================================================
#  ROTA 3: API DE FEED COMUNITÁRIO EM TEMPO REAL (MÉTODO GET)
# ==============================================================================
# Rota usada pelo painel para puxar os últimos 10 golpes do banco sem atualizar a página inteira
@app.route('/alertas', methods=['GET'])
def alertas():
    # Consulta no SQLite os 10 últimos registros adicionados pela comunidade
    alertas_list = AnalisarGolpes.query.order_by(AnalisarGolpes.id.desc()).limit(10).all()
    
    # Transforma a lista de objetos do banco em uma lista JSON compreensível para o front-end
    return jsonify([{
        'id': a.id,
        'resumo': a.texto_suspeito[:50] + '...' if len(a.texto_suspeito) > 50 else a.texto_suspeito,
        'tipo': getattr(a, 'resultado_ia', 'PENDENTE'),
        'data': 'Recentemente'
    } for a in alertas_list])

# ==============================================================================
#  INICIALIZAÇÃO DA APLICAÇÃO
# ==============================================================================
# Verifica se o script está sendo executado diretamente e liga o modo de desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)