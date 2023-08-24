import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Comments(db.Model):
    __tablename__ = "Comments"

    comment_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    rating = db.Column(db.Integer())

    def __init__(self, title, description, rating, active):
        self.comment_id = uuid.uuid4()
        self.title = title
        self.description = description
        self.rating = rating
        self.active = active

    def new_comment():
        return Comments("", "", 0, True)

class CommentsSchema(ma.Schema):
    class Meta:
        fields = ['comment_id', 'title', 'description', 'rating', 'active']


comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)