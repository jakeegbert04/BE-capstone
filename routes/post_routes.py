from flask import Blueprint, request
from controllers import post_controller

post = Blueprint("post", __name__)
@post.route('/post/add', methods=["POST"])
def add_post():
    return post_controller.add_post(request)

@post.route('/post/update/<id>', methods=["PUT"])
def update_post(id):
    return post_controller.update_post(request, id)

@post.route('/posts/get', methods=['GET'])
def get_all_active_posts():
    return post_controller.get_all_active_posts(request)

@post.route("/post/get/<id>", methods=["GET"])
def get_post_by_id(id):
    return post_controller.get_post_by_id(request, id)

@post.route("/post/status/<id>", methods=["PATCH"])
def post_status(id):
    return post_controller.post_status(request, id)

@post.route('/post/delete/<id>', methods=["DELETE"])
def delete_post(id):
    return post_controller.delete_post(request, id)