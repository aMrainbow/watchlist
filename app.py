from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Welcome to M_B Watchlist!</h1><img src="http://helloflask.com/totoro.gif">'


