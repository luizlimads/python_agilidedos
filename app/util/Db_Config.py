import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Data_Base:
    conn = None

    def __init__(self):
        try:
            self._abrir_conn()
        except:
            print('FALHA AO CONECTAR')
        finally:
            self._fechar_conn()

    def _abrir_conn(self):
        print('Abrindo conn')
        self.conn = mysql.connector.connect(
            host="db4free.net",
            user=os.environ["user_db"],
            password=os.environ["password_db"],
            database=os.environ["database"]
        )
 
    def _fechar_conn(self):
        self.conn.commit()
        self.conn.close()
    