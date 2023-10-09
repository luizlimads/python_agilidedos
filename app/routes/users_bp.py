from flask import Blueprint, render_template, redirect, request, url_for, flash
from app.service.User_Controller import User_Controller
from app.model.user import User

users_bp = Blueprint('users', __name__)

def catch_form_user(*args):
    data = {}
    dict_key = {
        "nome": 'name',
        "login": 'login',
        "email": 'email',
        "senha": 'password' 
    }

    for key in args:
        data[ dict_key[key] ] = request.form[key]

    return(data)

@users_bp.route('/login')
def login():
    return render_template('login/login.html')


@users_bp.route('/login', methods=['POST'])
def verifica_login():
    try:
        data = catch_form_user('login','senha')
        user = User(**data)
        user_controller = User_Controller(user)
        user_controller.login()
    except Exception as e:
        return redirect(url_for('users.login'))
    return redirect(url_for('users.login'))


@users_bp.route('/register')
def registro():
    return render_template('login/register.html')

@users_bp.route('/register', methods=['POST'])
def faz_registro():
    try:
        data = catch_form_user('nome','login','email','senha')
        user = User(**data)
        user_controller = User_Controller(user)
        user_controller.register()
    except Exception as e:
        return redirect(url_for('users.registro'))
    
    return redirect(url_for('users.login'))

