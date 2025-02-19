from app import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False, index=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    telefone = db.Column(db.String(20))
    data_nascimento = db.Column(db.Date)
    estado = db.Column(db.String(2))
    nivel = db.Column(db.String(50))
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    # Add index for common queries
    __table_args__ = (
        db.Index('idx_usuario_cpf_email', 'cpf', 'email'),
    )

class Pagamento(db.Model):
    __tablename__ = 'pagamentos'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False, index=True)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(50), default='pendente', index=True)
    tipo = db.Column(db.String(50))  # 'inscricao', 'taxa', 'frete'
    payment_id = db.Column(db.String(255), unique=True)  # ID do pagamento no For4Payments
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship('Usuario', backref=db.backref('pagamentos', lazy=True))

    # Add composite index for common queries
    __table_args__ = (
        db.Index('idx_pagamento_status_data', 'status', 'data_criacao'),
    )