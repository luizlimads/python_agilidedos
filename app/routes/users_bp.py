from flask import Blueprint, render_template, redirect, request, url_for, flash

users_bp = Blueprint('users', __name__)

@users_bp.route('/login')
def login():
    return render_template('login/login.html')

@users_bp.route('/login', methods=['POST'])
def verifica_login():
    return redirect(url_for('users.login'))

@users_bp.route('/register')
def registro():
    return render_template('login/register.html')

@users_bp.route('/register', methods=['POST'])
def faz_registro():
    data = {chave: request.form[chave] for chave in request.form}
    try:
        pass
    except Exception as e:
        flash("Falha em salvar os dados")
        print("Houve um erro:", e)
    return redirect(url_for('users.login'))

