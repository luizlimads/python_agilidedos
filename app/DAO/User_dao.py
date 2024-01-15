from app.util.Db_Config import Data_Base
from app.model.user import User


class User_Dao():

    @staticmethod
    def valid_user(user: User):
        is_valid = False
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor()
        sql = "SELECT id FROM users WHERE login LIKE %s AND password LIKE %s;"
        values = (user.login, user.password)
        cursor.execute(sql,values)

        for id in cursor:
            is_valid = True

        db.fechar_conn()
        return is_valid

    @staticmethod    
    def register_user(user: User):
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor()
        sql = "INSERT INTO users (name, login, email, password) VALUES (%s, %s, %s, %s)"
        values = (user.name, user.login, user.email, user.password)
        cursor.execute(sql,values)
        db.fechar_conn()




        