import re

from flask import flash
from mysql.connector import Error as mysql_error

from app.DAO.User_dao import User_Dao
from app.util.Handle_Erros import Handle_Erros_Mysql

class User_Controller():
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.login = kwargs.get('login')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')

    def register(self):
        try:
            user_dao = User_Dao()
            user_dao.send_db(
                self.name,
                self.login,
                self.email,
                self.password)
        except mysql_error as e:
            process_erro = Handle_Erros_Mysql(e)
            flash(process_erro.message())
            raise(e)
    
    def __str__(self):
        return f'{self.name} {self.login} {self.email}'
        

