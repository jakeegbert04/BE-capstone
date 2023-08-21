from flask import request, jsonify

from db import db
from models.comments.comments_xref import commentsxref_schema, commentsxrefs_schema, CommentsXref
from util.reflection import populate_object

def add_comment_xref():
    req_data = request.form if request.form else request.json