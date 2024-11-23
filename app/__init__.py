from flask import Flask
from config import Config
from .services import TMDBService
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize TMDBService and attach to blueprint
    tmdb_service = TMDBService(app.config['TMDB_API_KEY'])
    bp.tmdb_service = tmdb_service  # Attach service to blueprint
    app.register_blueprint(bp)

    return app
