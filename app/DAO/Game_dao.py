from app.util.Db_Config import Data_Base
from app.model.Game_Details import Game_Details
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

    @staticmethod
    def add_shot(game_id ,user_id, line, hits, miss, time):
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor()

        sql = "SELECT MAX(line) FROM game_details WHERE game_id=%s;"
        values = (game_id,)
        cursor.execute(sql,values)
        line_db = cursor.fetchone()[0]

        if line_db is None or (line_db is not None and line_db < line):        
            sql = "INSERT INTO game_details (game_id, user_id, line, hits, miss, time) \
                VALUES(%s, %s, %s, %s, %s, %s);"
            values = (game_id ,user_id, line, hits, miss, time)
            cursor.execute(sql,values)
            gd = Game_Details(game_id, user_id, line, hits, miss)
            is_recharge = False
        else:
            sql = "SELECT game_id, user_id, line, hits, miss FROM game_details WHERE game_id = %s AND line=(\
	        SELECT MAX(line) FROM game_details WHERE game_id = %s GROUP BY game_id LIMIT 1\
            );"
            values = (game_id,game_id)
            cursor.execute(sql,values)
            infos = cursor.fetchone()
            gd = Game_Details(infos[0], infos[1], infos[2], infos[3], infos[4])
            is_recharge = True

        db.fechar_conn()
        return gd




        