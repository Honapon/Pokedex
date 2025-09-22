from flask import Flask
from app.routes.pokemon_routes import pokemon_bp
def create_app():
    app = Flask(__name__)
    app.register_blueprint(pokemon_bp)
    return app