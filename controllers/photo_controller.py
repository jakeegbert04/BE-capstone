# CREATE
from flask import request, jsonify

from db import db
from models.photos import photo_schema, photos_schema, Photos
from util.reflection import populate_object
def add_photo():
    pass

#READ
def get_all_active_photos():
    pass

def get_photo_by_id(id):
    pass
#UPDATE
def update_photo(id):
    pass
#DEACTIVATE/ACTIVATE

#DELETE