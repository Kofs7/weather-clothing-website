from base64 import b64encode
from PIL import Image
import io
import os


class Item:
    database = {'top': [], 'bottom': [], 'shoes': []}

    def __init__(self):
        pass

    def new_item(self, item_name: str, item_type: str, season: list, image):
        image_path = os.getcwd() + f"/{image}"
        
        im = Image.open(image_path)
        image_bytes = io.BytesIO()
        im.save(image_bytes, format="JPEG")

        img_str = b64encode(image_bytes.getvalue())
        final_str = img_str.decode('ascii')

        tops = {'shirt', 'coat', 'jacket', 'hoodie', 'jumper'}
        bottoms = {'shorts', 'trousers', 'pants', 'sweatpants', 'denim', 'jeans', 'chinos'}
        shoes = {'trainers', 'sneakers', 'sandals', 'flip flops', 'slippers', 'slides', 'boots'}

        if item_type in tops:
            self.database['top'].append({'name': item_name, 'season': season, 'image': final_str})
        if item_type in bottoms:
            self.database['bottom'].append({'name': item_name, 'season': season, 'image': final_str})
        if item_type in shoes:
            self.database['shoes'].append({'name': item_name, 'season': season, 'image': final_str})

    @classmethod
    def get_database(cls):
        return cls.database

db = Item()
db.new_item('nike tye-dye', 'shirt', ['summer', 'spring'], 'nikeshirt.jpeg')
print(db.get_database())