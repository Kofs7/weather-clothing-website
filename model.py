import os
import json
import urllib

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

            weather = ['sunny','sunny','sunny','sunny','sunny','snowy', 'cloudy', 'sunny', 'cloudy', 'sunny','snowy']
            styles = ['casual','casual','classic','classic','classic','casual', 'streetwear', 'casual', 'casual', 'casual','casual']
            
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

            weather = ['sunny', 'sunny', 'sunny', 'rainy', 'sunny', 'sunny', 'cloudy', 'snowy']
            styles = ['classic', 'casual', 'casual', 'casual', 'classic', 'casual', 'streetwear', 'casual']
            
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

            weather = ['snowy', 'sunny', 'sunny', 'sunny', 'sunny', 'cloudy', 'cloudy', 'sunny']
            styles = ['casual', 'classic', 'casual', 'casual', 'casual', 'casual', 'streetwear', 'casual']
            
            image_path = os.path.join(shoes, file)
            if os.path.isfile(image_path):
                item = Item(style=styles[x], item_type='shoes', weather=weather[x], image=image_path)
                db.session.add(item)
        db.session.commit()

# item = Add_items()
# item.add_top()
# item.add_bottom()
# item.add_shoes()

# * Weather API filter
api_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Washington%2C%20DC/today?unitGroup=us&key=K3WUKAZ4638HASZFK2UBXBU3X&contentType=json"

def current_season():
    try: 
        result_bytes = urllib.request.urlopen(api_URL)
        # Parse the results as JSON
        jsonData = json.loads(result_bytes.read().decode('utf-8'))
    except urllib.error.HTTPError  as e:
        ErrorInfo= e.read().decode() 
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except  urllib.error.URLError as e:
        ErrorInfo= e.read().decode() 
        print('Error code: ', e.code,ErrorInfo)
        sys.exit()

    if jsonData['currentConditions']['temp'] <= 32.0:
        return "snowy"
    elif jsonData['currentConditions']['temp'] > 32.0 and jsonData['currentConditions']['temp'] <= 71.0:
        return "cloudy"
    elif jsonData['currentConditions']['temp'] > 71.0 and jsonData['currentConditions']['temp'] <= 84.0:
        return "rainy"
    else:
        return "sunny"

# * Get selected clothes and saving to db
class Selected_items:
    def __init__(self, top: str, bottom: str, shoes: str):
        self.top = top
        self.bottom = bottom
        self.shoes = shoes
        self.clothes_lst = [self.top, self.bottom, self.shoes]
        self.clothes_dict = clothes_dict = {
            'top': '',
            'bottom': '',
            'shoes': ''
        }
    
    def get_items(self):
        for item in self.clothes_lst:
            if item.find('/tops') > 0:
                self.clothes_dict['top'] = item
            if item.find('/bottoms') > 0:
                self.clothes_dict['bottom'] = item
            if item.find('/shoes') > 0:
                self.clothes_dict['shoes'] = item
        
        return self.clothes_dict

    def add_to_saved(self, user: str, style: str):
        from app import Saved
        from app import db

        for k, v in self.clothes_dict.items():
            save_field = Saved(user=user, style=style, item_type=k, weather=current_season(), image=v)
            db.session.add(save_field)
        db.session.commit()

