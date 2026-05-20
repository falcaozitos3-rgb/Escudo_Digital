"""
Configuração e modelos do banco de dados
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AnalisarGolpes(db.Model):
    """Modelo para armazenar análise de mensagens suspeitas"""
    __tablename__ = 'analisar_golpes'
    
    id = db.Column(db.Integer, primary_key=True)
    texto_suspeito = db.Column(db.String, nullable=False)
    resultado_ia = db.Column(db.String(50), nullable=False, default="PENDENTE")
    justificativa = db.Column(db.String, nullable=True)
    
    # Novos campos para localização e IP
    ip_usuario = db.Column(db.String(50), nullable=True)
    cidade = db.Column(db.String(100), nullable=True)
    estado = db.Column(db.String(100), nullable=True)
    pais = db.Column(db.String(100), nullable=True)
    
    # Data/hora da análise
    data_registro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"<AnalisarGolpes {self.id} - {self.resultado_ia}>"



def inicializar_banco(app):
    """Inicializa o banco de dados com o app Flask"""
    db.init_app(app)
    with app.app_context():
        db.create_all()
