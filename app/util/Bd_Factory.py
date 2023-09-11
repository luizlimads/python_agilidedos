import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Data_Base:
    __instance = None
    __conn = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = \
            super(Data_Base,cls).__new__(cls)
        return cls.__instance

    def __abrir_conn(self):
        self.__conn = mysql.connector.connect(
            host="db4free.net",
            user=os.environ["user_db"],
            password=os.environ["password_db"],
            database=os.environ["database"]
        )
 
    def __fechar_conn(self):
        self.__conn.commit()
        self.__conn.close()        

    def pegar_estado(self):
        self.__abrir_conn()
        mycursor = self.__conn.cursor()
        sql =  "select nome from estados where id=29;"
        mycursor.execute(sql)
        for nome in mycursor:
            res=nome
        self.__fechar_conn()
        return(res[0])
    