from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', apelido='apelido')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verifica', methods=['POST',])
def verifica():
    apelido = request.form['apelido']
    print(apelido)
    return redirect('/')
