import math

from flask import Blueprint, render_template, request, jsonify

game_bp = Blueprint('game', __name__, url_prefix="/game")

def match_char(text_one, text_two):
    number_of_hits = 0
    for indice, char in enumerate(text_one):
        if len(text_two) <= indice: break
        number_of_hits += 1 if char == text_two[indice] else 0
    return number_of_hits


@game_bp.route('/')
def menu():
    return render_template('game/menu.html')

@game_bp.route('/play')
def play():
    texto_de_aprendizado_completo = "banana batata jaca laranja"
    return render_template('game/play.html', texto_de_aprendizado=texto_de_aprendizado_completo)


@game_bp.route('/update_text', methods=['POST'])
def update():
    data = request.get_json()
    number_of_hits = match_char(data['currentText'],data['myText'])
    time = math.floor((data['timeEnd'] - data['timeStart'])/1000)
    return jsonify({
        'time': time
        })