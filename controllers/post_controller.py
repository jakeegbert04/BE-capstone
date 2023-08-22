from flask import request, jsonify

from db import db
from models.posts import post_schema, posts_schema, Posts
from util.reflection import populate_object
from lib.authenticate import auth

# CREATE
@auth
def add_post(request):
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all required fields")

    new_post = Posts.new_post()

    populate_object(new_post, req_data)
    db.session.add(new_post)
    db.session.commit()

    return jsonify("Post Created"), 200

#READ
@auth
def get_all_active_posts(request):
    posts = db.session.query(Posts). filter(Posts.active == True).all()

    if not posts:
        return jsonify("No Posts Exists"), 404
    else:
        return jsonify(posts_schema.dump(posts)), 200
        
@auth
def get_post_by_id(request, id):
    post = db.session.query(Posts).filter(Posts.post_id == id).first()

    if not post:
        return jsonify("That post does not exist"), 404
    else:
        return jsonify(post_schema.dump(post)), 200

#UPDATE
@auth
def update_post(request, id):
    req_data = request.form if request.form else request.json
    existing_post = db.session.query(Posts).filter(Posts.post_id == id).first()

    populate_object(existing_post, req_data)

    db.session.commit()
    return jsonify("Post Updated"), 200
#DEACTIVATE/ACTIVATE

@auth
def post_status(request, id):
    post_data = db.session.query(Posts).filter(Posts.post_id == id).first()

    if post_data:
        post_data.active = not post_data.active
        db.session.commit()

        return jsonify(post_schema.dump(post_data)), 200
    return jsonify({"message": "No post found"}), 404

#DELETE
@auth
def delete_post(request, id):

    post = db.session.query(Posts).filter(Posts.post_id == id).first()

    if not post:
        return jsonify("That post doesn't exist"), 404

    else:
        db.session.delete(post)
        db.session.commit()
        return jsonify("Post Deleted")