from flask import Flask, session
from flask import render_template, redirect 
from flask import url_for, flash
from model import Item

app = Flask(__name__)

@app.route('/')
#@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/rack')
def rack():
    items = Item.get_database()
    return "rack page"

@app.route('/combos')
def combos():
    items = Item.get_database()
    tops = items['top']
    bottoms = items['bottom']
    shoes = items['shoes']
    
    return 'combos'

@app.route('/login')
def login():
    return "login"

@app.route('/logout')
def logout():
    return 'logout'

if __name__ == '__main__':
    app.run(debug=True)
