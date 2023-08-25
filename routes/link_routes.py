from flask import Blueprint, request
from controllers import link_controller

link = Blueprint("link", __name__)
@link.route('/link/add', methods=["POST"])
def add_link():
    return link_controller.add_link(request)

@link.route('/link/update/<id>', methods=["PUT"])
def update_link(id):
    return link_controller.update_link(request, id)

@link.route('/links/get', methods=['GET'])
def get_all_links():
    return link_controller.get_all_links(request)

@link.route("/link/get/<id>", methods=["GET"])
def get_link_by_id(id):
    return link_controller.get_link_by_id(request, id)

@link.route('/link/delete/<id>', methods=["DELETE"])
def delete_link(id):
    return link_controller.delete_link(request, id)

@link.route("/links/delete/<user_id>", methods=["Delete"])
def delete_all_user_links(user_id):
    return link_controller.delete_all_user_links(request, user_id)