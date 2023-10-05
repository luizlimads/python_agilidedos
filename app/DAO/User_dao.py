from app.util.Db_Config import Data_Base
class User_Dao(Data_Base):
    def __init__(self):
        super().__init__()

    def send_db(self,name,login,email,password):
        try:
            self.abrir_conn()
            cursor = self.conn.cursor()
            sql = "INSERT INTO users (name,login,email,password) VALUES (%s, %s, %s, %s)"
            values = (name, login, email, password)
            cursor.execute(sql,values)
            self.conn.commit()
            self.fechar_conn()
        except Exception as e:
            raise(e)


        