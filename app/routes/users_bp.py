import jwt
import datetime

from flask import Blueprint, render_template, redirect, request, url_for, flash, make_response

from app.DAO.User_dao import User_Dao
from app.model.user import User
from app.service.Auth import generate_token, parametros_auth

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
        is_valid_user = User_Dao.valid_user(user)

        if is_valid_user.bool_response:
            response = make_response(redirect(url_for('game.menu')))
            response.set_cookie(**parametros_auth(is_valid_user.data))
            return response
        else:
            flash("Senha ou usuário invalidos")
            return redirect(url_for('users.login'))
        
    except Exception as e:
            flash("Um comportamento inesperado ocorreu")
            print(e)
            return redirect(url_for('users.login'))


@users_bp.route('/register')
def registro():
    return render_template('login/register.html')

@users_bp.route('/register', methods=['POST'])
def faz_registro():
    try:
        data = catch_form_user('nome','login','email','senha')
        user = User(**data)
        User_Dao.register_user(user)
        flash("Usuário criado com sucesso")
        return redirect(url_for('users.login'))
    except Exception as e:
        flash("Houve uma falha no seu registro, tende novamente")
        print(e)
        return redirect(url_for('users.register'))
    

