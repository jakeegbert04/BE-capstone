from flask import Blueprint
from controllers import photo_controller

photo = Blueprint("photo", __name__)
@photo.route('/photo/add', methods=["POST"])
def add_photo():
    return photo_controller.add_photo()

@photo.route('/photo/update/<id>', methods=["PUT"])
def update_photo(id):
    return photo_controller.update_photo(id)

@photo.route('/photos/get', methods=['GET'])
def get_all_active_photos():
    return photo_controller.get_all_active_photos()

@photo.route("/photo/get/<id>", methods=["GET"])
def get_photo_by_id(id):
    return photo_controller.get_photo_by_id(id)