import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db


class Posts(db.Model):
    __tablename__ = "Posts"

    post_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    location = db.Column(db.String())

    # photo_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Photos.photo_id"), nullable=False)

    active = db.Column(db.Boolean(), nullable=False, default=True)

    def __init__(self, title, description, location, active):
        self.title = title
        self.description = description
        self.location = location
        self.active = active

    def new_post():
        return Posts("", "", "", True)

class PostSchema(ma.Schema):
    class Meta:
        fields = ['post_id', 'title', 'description', 'location', 'active']
    


post_schema = PostSchema()
posts_schema = PostSchema(many=True)