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

# IMPORTA FUNÇÕES DE SEGURANÇA do arquivo 'seguranca.py'
# Essas funções protegem contra SQL Injection, Prompt Injection, e Buffer Overflow
from seguranca import input_e_seguro, construir_prompt_seguro, eh_link, validar_resposta_ia, verificacao_das_operadoras_oficial

# Importa bibliotecas nativas do Python para gerenciar o sistema e ler formatos JSON
import os
import json
import requests

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# ==============================================================================
# CONFIGURAÇÃO DO SERVIDOR FLASK E BANCO DE DADOS
# ==============================================================================
# Inicializa o servidor web principal do Flask
app = Flask(__name__)

# Garante que o Flask envie os acentos em português corretamente para o navegador
app.config['JSON_AS_ASCII'] = False

# Configura o caminho absoluto exato para o banco SQLite dentro da sua pasta de trabalho
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "instance", "golpes.db")}'

# Desativa o monitoramento de modificações para economizar memória RAM no seu Celeron
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Executa a função do seu arquivo separado para ligar o banco de dados ao servidor Flask
inicializar_banco(app)

# Inicializa o motor da IA (ele vai ler a chave 'GROQ_API_KEY' injetada no terminal)
client = Groq()

# ==============================================================================
#  ROTA 1: PÁGINA PRINCIPAL DO SITE (MÉTODO GET E POST)
# ==============================================================================
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto_recebido = request.form.get('mensagem')

        if texto_recebido:
            novo_alerta = AnalisarGolpes(texto_suspeito=texto_recebido)
            db.session.add(novo_alerta)
            db.session.commit()
            print(f"[BANCO DE DADOS] Salvo com êxito! {texto_recebido}")

    alertas_registrados = AnalisarGolpes.query.order_by(AnalisarGolpes.id.desc()).all()
    return render_template('index.html', alertas=alertas_registrados)

# ==============================================================================
#  ROTA 2: API DE ANÁLISE COMPLETA VIA IA LLAMA 3 (MÉTODO POST VIA JAVASCRIPT)
# ==============================================================================
@app.route('/analisar', methods=['POST'])
def analisar():
    """
    ROTA DE ANÁLISE COM FILTRO LOCAL + IA
    """
    try:
        data = request.get_json()
        mensagem = data.get('mensagem', '').strip()
        ip_real = data.get('ip_real', '')
        
        # PASSO 1: SANITIZAÇÃO - Valida se o input é seguro
        if not data or not mensagem:
            return jsonify({'nivel': 'erro', 'descricao': 'Nenhuma mensagem enviada.'}), 400
        
        # PASSO 2: VALIDAÇÃO DE SEGURANÇA (SQL/Python Injection)
        if not input_e_seguro(mensagem):
            return jsonify({
                'nivel': 'erro', 
                'descricao': 'Mensagem rejeitada por conter padrões suspeitos. Tente novamente sem comandos de código.'
            }), 400
        
        # PASSO 3: TENTA FILTRO LOCAL DE OPERADORAS
        eh_oficial, justificativa_local = verificacao_das_operadoras_oficial(mensagem)
        
        if eh_oficial:
            print(f" [FILTRO LOCAL] Mensagem detectada como aviso de operadora legítimo")
            return jsonify({
                'nivel': 'seguro',  # <-- Força o nível seguro para acender o painel verde
                'descricao': justificativa_local,
                'educacao': 'Dica: Para sua total segurança, evite pagar Pix copiados diretamente de SMS. Abra o aplicativo oficial da operadora para confirmar.',
                'tipo': 'MENSAGEM',
                'origem': 'filtro_local'
            })

        # PASSO 4: DETECTA TIPO DE CONTEÚDO (Texto ou Link)
        eh_link_bool = eh_link(mensagem)
        tipo_conteudo = "LINK" if eh_link_bool else "MENSAGEM"
        print(f" [ANÁLISE] Tipo detectado: {tipo_conteudo}")
        
        # PASSO 5: CONSTRÓI PROMPT BLINDADO EM XML
        mensagens_api = construir_prompt_seguro(mensagem, eh_link=eh_link_bool)

        # Obtém localização do IP do usuário de forma segura
        localizacao = obter_localizacao_ip(ip_real) if ip_real else obter_localizacao_ip()
        
        print(f" [IA] Enviando requisição para Llama 3...")
        
        try:
            # PASSO 6: CHAMADA À IA VIA GROQ CLIENT
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=mensagens_api,
                response_format={"type": "json_object"}
            )
            
            # PASSO 7: VALIDA RESPOSTA DA IA
            resposta_texto = completion.choices[0].message.content
            resultado_ia = validar_resposta_ia(resposta_texto)
            
            if not resultado_ia:
                return jsonify({
                    'nivel': 'erro',
                    'descricao': 'IA retornou resposta em formato inválido. Tente novamente.'
                }), 500
            
            nivel = resultado_ia.get('nivel', 'suspeito')
            descricao = resultado_ia.get('descricao', 'Análise inconclusiva.')
            educacao = resultado_ia.get('educacao', '')
            
            print(f" [IA] Resposta validada: {nivel.upper()}")
            
            # PASSO 8: SALVA NO BANCO COM PREPARED STATEMENT VIA ORM
            novo_alerta = AnalisarGolpes(
                texto_suspeito=mensagem,
                resultado_ia=nivel.upper(),
                justificativa=descricao,
                ip_usuario=ip_real or localizacao.get('ip'),
                cidade=localizacao.get('cidade'),
                estado=localizacao.get('estado'),
                pais=localizacao.get('pais')
            )
            db.session.add(novo_alerta)
            db.session.commit()
            
            print(f" [BANCO] Salvo com ID: {novo_alerta.id} | {novo_alerta.cidade}, {novo_alerta.estado}")
            
            # RETORNA RESULTADO PARA FRONTEND COM ENCODING REVISADO
            return jsonify({
                'nivel': nivel,
                'descricao': descricao,
                'educacao': educacao,
                'tipo': tipo_conteudo,
                'origem': 'ia_groq'
            })
            
        except Exception as e:
            print(f" [IA] Erro ao chamar Llama 3: {str(e)}")
            return jsonify({
                'nivel': 'erro',
                'descricao': f'Erro ao processar com a IA: {str(e)}'
            }), 500
        
    except Exception as e:
        print(f" [ERRO GERAL] {str(e)}")
        return jsonify({
            'nivel': 'erro',
            'descricao': f'Erro no servidor: {str(e)}'
        }), 500

# ==============================================================================
#  ROTA 3: API DE FEED COMUNITÁRIO EM TEMPO REAL (MÉTODO GET)
# ==============================================================================
@app.route('/alertas', methods=['GET'])
def alertas():
    alertas_list = AnalisarGolpes.query.order_by(AnalisarGolpes.id.desc()).limit(10).all()
    
    return jsonify([{
        'id': a.id,
        'resumo': a.texto_suspeito[:50] + '...' if len(a.texto_suspeito) > 50 else a.texto_suspeito,
        'tipo': getattr(a, 'resultado_ia', 'PENDENTE'),
        'data': 'Recentemente'
    } for a in alertas_list])

# ==============================================================================
#  ROTA 4: FUNÇÃO E API DE LOCALIZAÇÃO POR IP (MÉTODO GET)
# ==============================================================================
def obter_localizacao_ip(ip_usuario=None):
    if not ip_usuario:
        # pegara o IP do cabeçalho ou do remote_addr nativo do flask
        ip_usuario = request.headers.get('X-Forwarded-For', request.remote_addr)

    # se ip_usuario ainda exixtir e for uma string valida
    if ip_usuario:
        # Primeira separa por virgula, pega a primeira posição e SÓ DEPOIS aplica o .strig() na strig
        ip_usuario = ip_usuario.split(',')[0].strip()

    # trava de segurança para testa locais no seu noteboock/computador/celular  
    if ip_usuario == '127.0.0.1' or not ip_usuario:
        ip_usuario = '8.8.8.8'  # IP de teste do Google caso rode local
    
    try:
        url = f"http://ip-api.com/json/{ip_usuario}?lang=pt"
        resposta = requests.get(url, timeout=5).json()
        
        if resposta.get('status') == 'success':
            return {
                'estado': resposta.get('regionName'),
                'lat': resposta.get('lat'),
                'cidade': resposta.get('city'),
                'lon': resposta.get('lon'),
                'ip': ip_usuario,
                'pais': resposta.get('country')
            }
    except Exception as e:
        print(f"[LOCALIZAÇÃO] Erro ao obter localização: {str(e)}")
    
    return {
        'estado': 'Desconhecido',
        'cidade': 'Desconhecido',
        'lat': 0,
        'lon': 0,
        'ip': ip_usuario,
        'pais': 'Desconhecido'
    }


@app.route('/localizacao', methods=['GET'])
def localizacao():
    dados = obter_localizacao_ip()
    return jsonify(dados)


@app.route('/localizacao-por-ip', methods=['POST'])
def localizacao_por_ip():
    data = request.get_json()
    ip = data.get('ip', '')
    
    if not ip:
        return jsonify({'erro': 'IP não fornecido'}), 400
    
    dados = obter_localizacao_ip(ip)
    return jsonify(dados)

# ==============================================================================
#  INICIALIZAÇÃO DA APLICAÇÃO
# ==============================================================================
if __name__ == '__main__':
    # Configurado em False por padrão para segurança na feira da SEC
    app.run(debug=False)