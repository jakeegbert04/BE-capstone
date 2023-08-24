from flask import request, jsonify

from db import db
from models.links.links import link_schema, links_schema, Links
from models.links.links_xref import link_xref_schema, link_xrefs_schema, LinksXRef
from util.reflection import populate_object
from lib.authenticate import auth, auth_with_return

@auth_with_return
def add_link(request, auth_info):
    req_data = request.form if request.form else request.json
    # print(auth_info.user_id)

    if not req_data:
        return jsonify("Please enter all required fields")

    new_link_url = req_data.get('link_url')
    user_id = auth_info.user_id

    new_link = Links(link_url=new_link_url)

    db.session.add(new_link)
    db.session.flush()

    new_link_xref = LinksXRef(user_id=user_id, link_id=new_link.link_id)
    print(new_link_xref)
    db.session.add(new_link_xref)
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