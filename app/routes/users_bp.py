from flask import Blueprint, render_template, redirect, request, url_for, flash
from app.service.User_Controller import User_Controller


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
    try:
        data = {
            "name":request.form['nome'],
            "login":request.form['login'],
            "email":request.form['email'],
            "password":request.form['senha']
        }
        user = User_Controller(**data)
        user.register()
    except:
        return redirect(url_for('users.registro'))
    return redirect(url_for('users.login'))

