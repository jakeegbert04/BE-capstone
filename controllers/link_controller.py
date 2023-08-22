from flask import request, jsonify

from db import db
from models.links.links import link_schema, links_schema, Links
from util.reflection import populate_object
from lib.authenticate import auth

@auth
def add_link(request):
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all required fields")
    
    new_link = Links(req_data.get('link_url'))

    
    db.session.add(new_link)
    db.session.commit()

    return jsonify("link created"), 200

#READ
@auth
def get_all_active_links(request):
    links = db.session.query(Links).all()

    if not links:
        return jsonify("No Links Exists"), 404
    else:
        return jsonify(links_schema.dump(links)), 200

@auth
def get_link_by_id(request, id):
    link = db.session.query(Links).filter(Links.link_id == id).first()

    if not link:
        return jsonify("That link does not exist"), 404
    else:
        return jsonify(link_schema.dump(link)), 200

#UPDATE
def update_link(request, id):
    req_data = request.form if request.form else request.json
    existing_link = db.session.query(Links).filter(Links.link_id == id).first()

    populate_object(existing_link, req_data)

    db.session.commit()
    return jsonify("Link Updated"), 200

@auth
def link_status(request, id):
    link_data = db.session.query(Links).filter(Links.link_id == id).first()

    if link_data:
        link_data.active = not link_data.active
        db.session.commit()

        return jsonify(link_schema.dump(link_data)), 200
    return jsonify({"message": "No link found"}), 404

#DELETE
@auth
def delete_link(request, id):

    link = db.session.query(Links).filter(Links.link_id == id).first()

    if not link:
        return jsonify("That link doesn't exist"), 404

    else:
        db.session.delete(link)
        db.session.commit()
        return jsonify("Link Deleted")