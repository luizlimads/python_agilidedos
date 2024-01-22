import math

from flask import Blueprint, render_template, request, jsonify, redirect, url_for

from app.service.Auth import token_required
from app.model.Game import Game
from app.model.Game_Details import Game_Details
from app.model.User import User
from app.model.Words import Words
from app.DAO.Words_dao import Words_Dao
from app.DAO.Game_dao import Game_Dao

game_bp = Blueprint('game', __name__, url_prefix="/game")

def match_char(text_one, text_two):
    number_of_hits = 0
    for indice, char in enumerate(text_one):
        if len(text_two) <= indice: break
        number_of_hits += 1 if char == text_two[indice] else 0
    return number_of_hits

@game_bp.route('/')
@token_required
def menu(user_data: User):
    words = Words_Dao.get_words()
    return render_template('game/menu.html', user = user_data, words = words.data)

@game_bp.route('/play', methods=['POST'])
@token_required
def new_game(user_data: User):
    user_id = user_data.id
    word_id = request.form['id']
    res = Game_Dao.create_game(user_id = user_id, words_id = word_id)
    game_id = res.data['game_id']
    return redirect(url_for('game.play', no_game=f'{user_id}-{game_id}'))

@game_bp.route('/play/<no_game>')
@token_required
def play(user_data: User,no_game: str):
    user_id, game_id = no_game.split('-')
    res = Words_Dao.get_word_by_game(game_id)
    game: Game = res.data['game']
    user: User = res.data['user']
    word: Words = res.data['word']
    texto_de_aprendizado_completo = word.value
    return render_template('game/play.html', texto_de_aprendizado=texto_de_aprendizado_completo)



@game_bp.route('/update_text', methods=['POST'])
@token_required
def update(user_data: User):
    data = request.get_json()
    game_id = data['game_id']
    user_id = user_data.id
    line = data['line']
    if data['currentText']:
        number_of_hits = sum( [1 for x,y in zip(data['currentText'],data['myText']) if x==y] )
        number_of_miss = len(data['currentText']) - number_of_hits        
    else:
        number_of_hits = 0
        number_of_miss = 0
    time = data['time']
    
    res:Game_Details = Game_Dao.add_shot(game_id,user_id,line,number_of_hits,number_of_miss,time)
    
    return jsonify({
        'line': res.line+1
        })