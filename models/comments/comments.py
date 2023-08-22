import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
# from models.comments.comments_xref import comments_xref


class Comments(db.Model):
    __tablename__ = "Comments"

    comment_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    rating = db.Column(db.Integer())

    user_comments = db.relationship("Users", secondary="comments_xref", back_populates = "comments")

    def __init__(self, comment_id, title, description, rating, active):
        self.comment_id = comment_id
        self.title = title
        self.description = description
        self.rating = rating
        self.active = active

    def new_comment():
        return Comments("", "", "", None, True)

class CommentsSchema(ma.Schema):
    class Meta:
        fields = ['comment_id', 'title', 'description', 'rating', 'active']


comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)