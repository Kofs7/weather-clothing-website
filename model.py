import os

class Add_items:
    def __init__(self):
        pass
        #options = casual, classic, streetwear
        #weather = sunny, rainy, cloudy, snowy

    def add_top(self): #style, item_type, season
        top = r'static/clothing-images/tops'

        for x, file in enumerate(os.listdir(top)):
            from app import db
            from app import Item

            weather = ['snowy', 'cloudy', 'sunny', 'cloudy', 'sunny']
            styles = ['casual', 'streetwear', 'casual', 'casual', 'casual']
            
            image_path = os.path.join(top, file)
            if os.path.isfile(image_path):
                item = Item(style=styles[x], item_type='top', weather=weather[x], image=image_path)
                db.session.add(item)
        db.session.commit()
    
    def add_bottom(self):
        bottom = r'static/clothing-images/bottoms'

        for x, file in enumerate(os.listdir(bottom)):
            from app import db
            from app import Item

            weather = ['sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'cloudy', 'snowy']
            styles = ['classic', 'casual', 'casual', 'classic', 'casual', 'streetwear', 'casual']
            
            image_path = os.path.join(bottom, file)
            if os.path.isfile(image_path):
                item = Item(style=styles[x], item_type='bottom', weather=weather[x], image=image_path)
                db.session.add(item)
        db.session.commit()

    def add_shoes(self):
        shoes = r'static/clothing-images/shoes'
        
        for x, file in enumerate(os.listdir(shoes)):
            from app import db
            from app import Item

            weather = ['snowy', 'sunny', 'sunny', 'sunny', 'cloudy', 'cloudy', 'sunny']
            styles = ['casual', 'casual', 'casual', 'casual', 'casual', 'streetwear', 'casual']
            
            image_path = os.path.join(shoes, file)
            if os.path.isfile(image_path):
                item = Item(style=styles[x], item_type='shoes', weather=weather[x], image=image_path)
                db.session.add(item)
        db.session.commit()

item = Add_items()
item.add_top()
item.add_bottom()
item.add_shoes()