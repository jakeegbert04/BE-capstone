import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db

class Links(db.Model):
    __tablename__ = "Links"

    link_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    link_url = db.Column(db.String(), nullable=False)


    def __init__(self, link_url):
        self.link_url = link_url

class LinksSchema(ma.Schema):
    class Meta:
        fields = ['link_id', 'link_url', "user"]
    user = ma.fields.Nested("UsersSchema")

link_schema = LinksSchema()
links_schema = LinksSchema(many=True)