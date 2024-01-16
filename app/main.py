import os

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for

from app.routes.users_bp import users_bp
from app.routes.game_bp import game_bp




def create_app(config = None):
    app = Flask(__name__)
    SECRET_KEY = os.environ["secret_key"]
    app.config['SECRET_KEY'] = SECRET_KEY

    # Registre o Blueprint de rotas
    app.register_blueprint(users_bp)
    app.register_blueprint(game_bp)

    @app.route('/')
    def index():
        return redirect(url_for('users.login'))
    
    return app

if __name__ == '__main__':
    create_app()