import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Data_Base:
    conn = None

    def abrir_conn(self):
        if not self.conn:
            self.conn = mysql.connector.connect(
                host="db4free.net",
                user=os.environ["user_db"],
                password=os.environ["password_db"],
                database=os.environ["database"]
            )
 
    def fechar_conn(self):
        if self.conn:
            self.conn.close()
        self.conn = None
    