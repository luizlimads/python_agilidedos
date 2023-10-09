import re

from flask import flash
from mysql.connector import Error as mysql_error

from app.DAO.User_dao import User_Dao
from app.util.Handle_Erros import Handle_Erros_Mysql
from app.model.user import User

class User_Controller():
    user_dao:User_Dao = None
    user: User= None
    def __init__(self, user: User):
        self.user = user
        self.user_dao = User_Dao()

    def register(self):
        try:
            self.user_dao.send_db(self.user)
        except mysql_error as e:
            process_erro = Handle_Erros_Mysql(e)
            flash(process_erro.message())
            raise(e)
        flash('Usuário criado com sucesso')

    def login(self):
        try:
            self.user_dao.valid_user(self.user)
        except mysql_error as e:
            process_erro = Handle_Erros_Mysql(e)
            flash(process_erro.message())
            raise(e)
        except Exception as e:
            flash("Usuário ou senha não conferem")
    
    
    def __str__(self):
        return f'{self.name} {self.login} {self.email}'
        

