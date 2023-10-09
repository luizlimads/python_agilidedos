import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Data_Base:
    conn = None

    def abrir_conn(self):
        try:
            if not self.conn:
                self.conn = mysql.connector.connect(
                    host="db4free.net",
                    # host="localhost",
                    user=os.environ["user_db"],
                    password=os.environ["password_db"],
                    database=os.environ["database"],
                    auth_plugin='mysql_native_password',
                    autocommit=True
                )
        except Exception as e:
            print(e)
 
    def fechar_conn(self):
        try:
            if self.conn:
                self.conn.close()
            self.conn = None
        except Exception as e:
            print(e)
    