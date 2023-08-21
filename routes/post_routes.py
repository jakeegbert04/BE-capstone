from flask import Blueprint
from controllers import post_controller


post = Blueprint("post", __name__)
@post.route('/post/add', methods=["POST"])
def add_post():
    return post_controller.add_post()

@post.route('/post/update/<id>', methods=["PUT"])
def update_post(id):
    return post_controller.update_post(id)


@post.route('/posts/get', methods=['GET'])
def get_all_active_posts():
    return post_controller.get_all_active_posts()


@post.route("/post/get/<id>", methods=["GET"])
def get_post_by_id(id):
    return post_controller.get_post_by_id(id)

@post.route("/post/status/<id>", methods=["PATCH"])
def post_status(id):
    return post_controller.post_status(id)