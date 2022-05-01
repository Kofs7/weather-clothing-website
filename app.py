from flask import Flask, session
from flask import render_template, redirect 
from flask import url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
# from model import current_season

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
    return render_template('rack.html', items=all_items)


@app.route('/combos', methods=["GET", "POST"])
def combos():
    # weather_filter = current_season()
    # top_filter = Item.query.filter_by(item_type='top', weather=weather_filter)
    # bottom_filter = Item.query.filter_by(item_type='bottom', weather=weather_filter)
    # shoes_filter = Item.query.filter_by(item_type='shoes', weather=weather_filter)
    top_filter = Item.query.filter_by(item_type='top')
    bottom_filter = Item.query.filter_by(item_type='bottom')
    shoes_filter = Item.query.filter_by(item_type='shoes')
    return render_template('combo.html', tops=top_filter, bottoms=bottom_filter, shoes=shoes_filter)


@app.route('/generated-combo', methods=['POST', "GET"])
def generate():
    from model import Selected_items
    
    if request.method == 'POST':
        clothes = request.form.getlist('cloth_checkbox')
        selected_top = clothes[0]
        selected_bottom = clothes[1]
        selected_shoe = clothes[2]

        items = Selected_items(selected_top, selected_bottom, selected_shoe)
        clothes_list = items.get_items().values()
        return render_template('generate.html', clothings=clothes_list)
    return redirect(url_for('home'))


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


@app.route('/saved')
def saved():
    from model import Selected_items
    items = Selected_items()
    return render_template('saved.html', stuff=items.display_items(), one=items.top,two=items.bottom,three=items.shoe)


@app.route('/logout')
def logout():
    if 'user' in session:
        flash(f"Successful log out, {session['user']}!!",  "info")
        session.pop('user')
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
