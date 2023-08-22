from flask import request, jsonify

from db import db
from models.links.links import link_schema, links_schema, Links
from util.reflection import populate_object
def add_link():
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all required fields")
    
    new_link = Links(req_data.get('link_url'))

    
    db.session.add(new_link)
    db.session.commit()

    return jsonify("link created"), 200

#READ
def get_all_active_links():
    pass

def get_link_by_id(id):
    pass
#UPDATE
def update_link(id):
    pass
def post_status(id):
    post_data = db.session.query(Links).filter(Links.link_id == id).first()

    if post_data:
        post_data.active = not post_data.active
        db.session.commit()

        return jsonify(link_schema.dump(post_data)), 200
    return jsonify({"message": "No link found"}), 404

#DELETE
def delete_post(id):

    link = db.session.query(Links).filter(Links.link_id == id).first()

    if not link:
        return jsonify("That link doesn't exist"), 404

    else:
        db.session.delete(link)
        db.session.commit()
        return jsonify("Link Deleted")