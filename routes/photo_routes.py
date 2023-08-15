from flask import Blueprint
from controllers import photo_controller


user = Blueprint("photo", __name__)
@user.route('/photo/add', methods=["POST"])
def add_photo():
    return photo_controller.add_photo()

@user.route('/photo/update/<id>', methods=["PUT"])
def update_photo(id):
    return photo_controller.update_photo(id)


@user.route('/photos/get', methods=['GET'])
def get_all_active_photos():
    return photo_controller.get_all_active_photos()


@user.route("/photo/get/<id>", methods=["GET"])
def get_photo_by_id(id):
    return photo_controller.get_photo_by_id(id)