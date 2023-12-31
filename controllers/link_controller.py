from flask import request, jsonify

from db import db
from models.links.links import link_schema, links_schema, Links
from models.links.links_xref import LinksXRef
from util.reflection import populate_object
from lib.authenticate import auth, auth_with_return

@auth_with_return
def add_link(request, auth_info):
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all required fields")

    new_link_url = req_data.get('link_url')
    user_id = auth_info.user_id

    new_link = Links(link_url=new_link_url)

    db.session.add(new_link)
    db.session.flush()

    new_link_xref = LinksXRef(user_id=user_id, link_id=new_link.link_id)
    db.session.add(new_link_xref)
    db.session.commit()

    return jsonify("link created"), 200

@auth
def get_all_links(request):
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

def update_link(request, id):
    req_data = request.form if request.form else request.json
    existing_link = db.session.query(Links).filter(Links.link_id == id).first()

    populate_object(existing_link, req_data)

    db.session.commit()
    return jsonify("Link Updated"), 200

@auth
def delete_link(request, id):

    link = db.session.query(Links).filter(Links.link_id == id).first()
    link_xrefs = db.session.query(LinksXRef).filter(LinksXRef.link_id == id).all()

    if not link and link_xref:
        return jsonify("That link doesn't exist"), 404

    else:

        for link_xref in link_xrefs:
            db.session.delete(link_xref)
        db.session.commit()
        db.session.delete(link)
        db.session.commit()

        return jsonify("Link Deleted")

@auth
def delete_all_user_links(request, user_id):

    links_xrefs = db.session.query(LinksXRef).filter(LinksXRef.user_id == user_id).all()

    if not links_xrefs:
        return jsonify("No links found for the user"), 404

    link_ids_to_delete = [xref.link_id for xref in links_xrefs]

    for link_id in link_ids_to_delete:
        link_xrefs = db.session.query(LinksXRef).filter(LinksXRef.link_id == link_id).all()
        for link_xref in link_xrefs:
            db.session.delete(link_xref)
        
        link = db.session.query(Links).filter(Links.link_id == link_id).first()
        if link:
            db.session.delete(link)

    db.session.commit()

    return jsonify("All links for the user have been deleted")