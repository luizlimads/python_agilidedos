import os
from flask import Flask, render_template, redirect, url_for
from app.routes.users_bp import users_bp

app = Flask(__name__)
SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY

# Registre o Blueprint de rotas de usuários
app.register_blueprint(users_bp, url_prefix='')

@app.route('/')
def index():
    return redirect(url_for('users.login'))
    return render_template('home.html', res='aa')

if __name__ == '__main__':
    app.run()