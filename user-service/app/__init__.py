from flask import Flask
from .config import Config
from .models import init_db
from .routes import bp as user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)
    app.register_blueprint(user_bp, url_prefix='/users')

    return app