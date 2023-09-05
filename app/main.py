from flask import Flask, render_template

def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('login.html')
    
    return app