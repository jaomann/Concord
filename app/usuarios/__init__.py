from flask import Blueprint

usuario = Blueprint("usuario", __name__)

from app.usuarios import routes