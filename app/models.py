from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def user_loader(id):
    return Usuario.query.get(int(id))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32))
    nascimento = db.Column(db.String(10))
    estado = db.Column(db.String(64))
    pais = db.Column(db.String(64))
    email = db.Column(db.String(64))
    senha_hash = db.Column(db.String(64))
    @property 
    def senha(self):
        raise AttributeError("A senha não é visível")
    @senha.setter
    def senha(self, senha):    
        self.senha_hash = generate_password_hash(senha)
    def verifica_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)