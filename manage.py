import os
from app import create_app, db
from app.models import *
from flask_migrate import Migrate
from app import socketio
app = create_app("default")

migrate = Migrate(app, db)

if __name__ == "__main__":
    socketio.run(app, debug=True)