from flask import Blueprint
from controllers import comment_controller


comment = Blueprint("comment", __name__)
@comment.route('/comment/add', methods=["POST"])
def add_comment():
    return comment_controller.add_comment()

@comment.route('/comment/update/<id>', methods=["PUT"])
def update_comment(id):
    return comment_controller.update_comment(id)


@comment.route('/comments/get', methods=['GET'])
def get_all_active_comments():
    return comment_controller.get_all_active_comments()


@comment.route("/comment/get/<id>", methods=["GET"])
def get_comment_by_id(id):
    return comment_controller.get_comment_by_id(id)