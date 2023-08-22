from flask import Blueprint
from controllers import link_controller


link = Blueprint("link", __name__)
@link.route('/link/add', methods=["POST"])
def add_link():
    return link_controller.add_link()

@link.route('/link/update/<id>', methods=["PUT"])
def update_link(id):
    return link_controller.update_link(id)


@link.route('/links/get', methods=['GET'])
def get_all_active_links():
    return link_controller.get_all_active_links()


@link.route("/link/get/<id>", methods=["GET"])
def get_link_by_id(id):
    return link_controller.get_link_by_id(id)