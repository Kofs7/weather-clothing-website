from flask import Flask, session
from flask import render_template, redirect 
from flask import url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from model import current_season

app = Flask(__name__)
app.secret_key = 'tH1x93H??s1Zow_#~2'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/items.sqlite'
app.config['SQLALCHEMY_BINDS'] = {
    'users_saved': 'sqlite:///databases/user_saved.sqlite'
}
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    style = db.Column(db.String(20))
    item_type = db.Column(db.String(50))
    weather = db.Column(db.String(50))
    image = db.Column(db.String(100))

    def __init__(self, style, item_type, weather, image):
        self.style = style
        self.item_type = item_type
        self.weather = weather
        self.image = image

class Saved(db.Model):
    __bind_key__ = 'users_saved'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))
    item_type = db.Column(db.String(50))
    weather = db.Column(db.String(50))
    image = db.Column(db.String(100))

    def __init__(self, user, style, item_type, weather, image):
        self.user = user
        self.style = style
        self.item_type = item_type
        self.weather = weather
        self.image = image  


@app.route('/')
@app.route('/index')
def home():
    # if 'user' in session:
    #     session['user'] = request.form['name']
    #     user = session['user']
    #     return render_template('index.html', name=user)
    return render_template('index.html')

@app.route('/rack', methods=['GET', 'POST'])
def rack():
    all_items = Item.query.all()
    #filters = Item.query.filter_by(style='casual', item_type='top')

    # if request.method == 'POST':  
    #     filter_dict = {'item_type': request.form['filter-clothes'],
    #                    'style': request.form['filter-style'],
    #                    'weather': request.form['filter-weather']   
    #                   }      
        
    return render_template('rack.html', items=all_items)

@app.route('/combos')
def combos():
    # items = Item.get_database()
    # tops = items['top']
    # bottoms = items['bottom']
    # shoes = items['shoes']
    weather_filter = current_season()
    top_filter = Item.query.filter_by(item_type='top', weather=weather_filter)
    bottom_filter = Item.query.filter_by(item_type='bottom', weather=weather_filter)
    shoes_filter = Item.query.filter_by(item_type='shoes', weather=weather_filter)
    
    return render_template('combo.html', tops=top_filter, bottoms=bottom_filter, shoes=shoes_filter)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        session['user'] = user

        return redirect(url_for('home'))
    else:
        if 'user' in session:
            redirect(url_for('home')) 
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
