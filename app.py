from flask import Flask, session
from flask import render_template, redirect 
from flask import url_for, flash

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return "Home Page"

@app.route('/rack')
def rack():
    return "rack page"

@app.route('/combos')
def combos():
    return 'combos'

@app.route('/login')
def login():
    return "login"

@app.route('/logout')
def logout():
    return 'logout'

if __name__ == '__main__':
    app.run(debug=True)
