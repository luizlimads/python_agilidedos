from app.util.Db_Config import Data_Base
from app.model.words import Words
from app.model.response import Default_Response

class Words_Dao():

    @staticmethod
    def get_words():
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor()
        sql = "SELECT id, user_id, name, value FROM set_words WHERE user_id = 1;"
        cursor.execute(sql)
        data = []

        for row in cursor:
            data.append(Words(user_id = row[1],
                         name = row[2],
                         value = row[3]
                         ))
        for i in data:
            print(i)
            
        def_res = Default_Response(data=data)

        db.fechar_conn()
        return def_res





        