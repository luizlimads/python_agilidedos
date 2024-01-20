import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def execute(sql_commands):
    commands = sql_commands.split(";")
    for command in commands:
        try:
            print(command)
            cursor.execute(command)
        except mysql.connector.Error as err:
            if err.errno == 1065:
                # erro linhas em branco
                pass
            else:
                print(f"Erro ao executar comando SQL: {err}")



def create_tables():
        with open("init_db/create_tables.sql", "r", encoding="UTF-8") as file:
            sql_commands = file.read()
        execute(sql_commands)

def fill_tables():
    with open("init_db/fill_tables.sql", "r", encoding="UTF-8") as file:
        sql_commands = file.read() 
    execute(sql_commands)


try:
    conn = mysql.connector.connect (
        host = os.environ["host_db"],
        user = os.environ["user_db"],
        password = os.environ["password_db"],
        database = os.environ["database"],
        auth_plugin = "mysql_native_password",
        autocommit=True
    )
    cursor = conn.cursor()

    create_tables()
    fill_tables()

    cursor.close()
    conn.close()
except Exception as e:
    print(e)