import marshmallow as ma

from db import db
from models.comments.comments import Comments

class CommentsXRef(db.Model):
    __tablename__ = "Comments_xref"

    comment_id = db.Column("comment_id", db.ForeignKey(Comments.comment_id), primary_key=True),
    user_id = db.Column("user_id", db.ForeignKey("Users.user_id"), primary_key=True)

    def __init__(self, comment_id, user_id):
        self.comment_id = comment_id
        self.user_id = user_id

class CommentsXrefSchema(ma.Schema):
    class Meta:
        fields = ["comment_id", "user_id"]

comment_xref_schema = CommentsXrefSchema()
comment_xrefs_schema = CommentsXrefSchema(many=True)

