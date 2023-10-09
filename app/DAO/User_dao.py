from app.util.Db_Config import Data_Base
from app.model.user import User
class User_Dao(Data_Base):
    def __init__(self):
        super().__init__()
    
    def send_db(self,user: User):
        try:
            self.abrir_conn()
            cursor = self.conn.cursor()
            sql = "INSERT INTO users (name, login, email, password) VALUES (%s, %s, %s, %s)"
            values = (user.name, user.login, user.email, user.password)
            cursor.execute(sql,values)
        except Exception as e:
            print(e)
            raise(e)
        finally:
            self.fechar_conn()
    
    def valid_user(self,user: User):
        invalid_user = True
        try:
            self.abrir_conn()
            cursor = self.conn.cursor()
            sql = "SELECT id FROM users WHERE login LIKE %s AND password LIKE %s;"
            values = (user.login, user.password)
            cursor.execute(sql,values)
            for id in cursor:
                invalid_user = False
        except Exception as e:
            print(e)
            raise(e)
        finally:
            self.fechar_conn()
        if invalid_user:
            raise('Usuario ou senha incorretos')




        