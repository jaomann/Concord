from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "usuario.login"

def create_app(config_name: str="default") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    from app.main import main as main_bp
    from app.usuarios import usuario as usuario_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(usuario_bp, url_prefix="/usuarios")
    
    return app