from app import db 
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32))
    estado = db.Column(db.String(64))
    pais = db.Column(db.String(64))
    email = db.Column(db.String(64))
    senha = db.Column(db.String(64))