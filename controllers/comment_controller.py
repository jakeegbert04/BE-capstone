from flask import request, jsonify

from db import db
from models.comments.comments import comment_schema, comments_schema, Comments
from models.comments.comments_xref import CommentsXRef
from util.reflection import populate_object
from lib.authenticate import auth, auth_with_return

@auth_with_return
def add_comment(request, auth_info):
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all required fields")

    new_comment = Comments.new_comment()
    populate_object(new_comment, req_data)
    db.session.add(new_comment)
    db.session.flush()

    user_id = auth_info.user_id
    new_comment_xref = CommentsXRef(user_id=user_id, comment_id=new_comment.comment_id)
    db.session.add(new_comment_xref)
    db.session.commit()

    return jsonify('Comment Created'), 200

#READ
@auth
def get_all_active_comments(request):
    comments = db.session.query(Comments).filter(Comments.active == True).all()

    if not comments:
        return jsonify("No comments Exists"), 404
    else:
        return jsonify(comments_schema.dump(comments)), 200

@auth
def get_comment_by_id(request, id):
    comment = db.session.query(Comments).filter(Comments.comment_id == id).first()

    if not comment:
        return jsonify("That comment does not exist"), 404
    else:
        return jsonify(comment_schema.dump(comment)), 200

#UPDATE
@auth
def update_comment(request, id):
    req_data = request.form if request.form else request.json
    existing_comment = db.session.query(Comments).filter(Comments.comment_id == id).first()

    populate_object(existing_comment, req_data)

    db.session.commit()
    return jsonify("comment Updated"), 200

@auth
def comment_status(request, id):
    comment_data = db.session.query(Comments).filter(Comments.comment_id == id).first()

    if comment_data:
        comment_data.active = not comment_data.active
        db.session.commit()

        return jsonify(comment_schema.dump(comment_data)), 200
    return jsonify({"message": "No comment found"}), 404

#DELETE
@auth
def delete_comment(request, id):

    comment = db.session.query(Comments).filter(Comments.comment_id == id).first()

    if not comment:
        return jsonify("That comment doesn't exist"), 404

    else:
        db.session.delete(comment)
        db.session.commit()
        return jsonify("comment Deleted")