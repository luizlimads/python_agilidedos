from app.util.Db_Config import Data_Base
from app.model.Game import Game
from app.model.Response import Default_Response

class Game_Dao():

    @staticmethod
    def create_game(user_id: str, words_id: str):
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor()
        sql = "INSERT INTO game (user_id, word_id) VALUES(%s, %s);"
        values = (user_id, words_id)
        cursor.execute(sql,values)

        sql = "SELECT MAX(id) id FROM game WHERE user_id=%s;"
        values = (user_id,)
        cursor.execute(sql,values)

        data = {'game_id':None}
        for row in cursor:
            data["game_id"] = row[0]
           
        def_res = Default_Response(data=data)

        db.fechar_conn()
        return def_res





        