from flask import Flask, render_template, redirect, request
from app.util.Bd_Factory import Data_Base

app = Flask(__name__)

@app.route('/')
def index():
    db = Data_Base()
    res = db.pegar_estado()
    return render_template('home.html', apelido=res)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verifica', methods=['POST',])
def verifica():
    apelido = request.form['apelido']
    print(apelido)
    return redirect('/')

