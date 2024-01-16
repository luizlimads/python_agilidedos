from app.util.Db_Config import Data_Base
from app.model.user import User
from app.model.response import Default_Response

class User_Dao():

    @staticmethod
    def valid_user(user: User):
        is_valid_user = False
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor()
        sql = "SELECT id,name,login FROM users WHERE login LIKE %s AND password LIKE %s;"
        values = (user.login, user.password)
        cursor.execute(sql,values)
        data = None

        for row in cursor:
            data = User(name=row[1],
                        login=row[2])
            is_valid_user = True

        def_res = Default_Response(is_valid_user, data)

        db.fechar_conn()
        return def_res

    @staticmethod    
    def register_user(user: User):
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor()
        sql = "INSERT INTO users (name, login, email, password) VALUES (%s, %s, %s, %s)"
        values = (user.name, user.login, user.email, user.password)
        cursor.execute(sql,values)
        db.fechar_conn()




        