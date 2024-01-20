from app.util.Db_Config import Data_Base
from app.model.Game import Game
from app.model.User import User
from app.model.Words import Words
from app.model.Response import Default_Response

class Words_Dao():

    @staticmethod
    def get_words():
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor()
        sql = "SELECT id, name FROM set_words WHERE user_id = 1;"
        cursor.execute(sql)
        data = []

        for row in cursor:
            data.append(Words(id = row[0], name = row[1]))
            
        def_res = Default_Response(data=data)

        db.fechar_conn()
        return def_res

    @staticmethod
    def get_word_by_id(id):
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor()
        sql = "SELECT id, user_id, name, value FROM set_words WHERE id = %s;"
        values = (id,)
        cursor.execute(sql,values)
        data = None

        for row in cursor:
            data = Words(id = row[0], user_id=row[1],
                        name = row[2], value = row[3])
            
        def_res = Default_Response(data=data)

        db.fechar_conn()
        return def_res

    @staticmethod
    def get_word_by_game(id):
        db = Data_Base()
        db.abrir_conn()
        cursor = db.conn.cursor(dictionary=True)
        sql = "SELECT g.id game_id, u.id user_id, sw.id word_id, sw.name word_name, sw.value word_value \
        FROM game g \
        LEFT JOIN users u ON g.user_id = u.id \
        LEFT JOIN set_words sw on g.word_id = sw.id \
        where g.id = %s;"
        values = (id,)
        cursor.execute(sql,values)
        data = {'game':None, 'user':None, 'word':None}
        
        row = cursor.fetchone()

        if row:
            data = {'game':Game(id=row['game_id']),
                    'user':User(id=row['user_id']),
                    'word':Words(id=row['word_id'], name=row['word_name'], value=row['word_value'] )}
        else:
            data = {'game': None, 'user': None, 'word': None}

            
        def_res = Default_Response(data=data)

        db.fechar_conn()
        return def_res

        