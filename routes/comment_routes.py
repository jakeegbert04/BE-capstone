from flask import Blueprint, request
from controllers import comment_controller


comment = Blueprint("comment", __name__)
@comment.route('/comment/add', methods=["POST"])
def add_comment():
    return comment_controller.add_comment(request)

@comment.route('/comment/update/<id>', methods=["PUT"])
def update_comment(id):
    return comment_controller.update_comment(request, id)


@comment.route('/comments/get', methods=['GET'])
def get_all_active_comments():
    return comment_controller.get_all_active_comments(request)

@comment.route("/comment/get/<id>", methods=["GET"])
def get_comment_by_id(id):
    return comment_controller.get_comment_by_id(request, id)

@comment.route("/comment/status/<id>", methods=["PATCH"])
def comment_status(id):
    return comment_controller.comment_status(request, id)

@comment.route('/comment/delete/<id>', methods=["DELETE"])
def delete_comment(id):
    return comment_controller.delete_comment(request, id)