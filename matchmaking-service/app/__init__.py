from flask import Flask
from .config import Config
from .models import init_db
from .routes import bp as match_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)
    app.register_blueprint(match_bp, url_prefix='/matches')

    return app