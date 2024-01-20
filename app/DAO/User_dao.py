from app.util.Db_Config import Data_Base
from app.model.User import User
from app.model.Response import Default_Response

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
            user_id = row[0]
            data = User(id = user_id,
                        name=row[1],
                        login=row[2])
            is_valid_user = True
            sql = "INSERT INTO access (user_id) VALUES (%s);"
            values = (user_id,)
            cursor.execute(sql,values)

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




        