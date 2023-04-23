from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from app.main import main as main_bp
    from app.usuarios import usuario as usuario_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(usuario_bp, url_prefix="/usuarios")
    
    return app