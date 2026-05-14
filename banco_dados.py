"""
Configuração e modelos do banco de dados
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AnalisarGolpes(db.Model):
    """Modelo para armazenar análise de mensagens suspeitas"""
    id = db.Column(db.Integer, primary_key=True)
    texto_suspeito = db.Column(db.String, nullable=False)
    resultado_ia = db.Column(db.String(20), nullable=False, default="PENDENTE")
    justificativa = db.Column(db.String, nullable=True)


def inicializar_banco(app):
    """Inicializa o banco de dados com o app Flask"""
    db.init_app(app)
    with app.app_context():
        db.create_all()
