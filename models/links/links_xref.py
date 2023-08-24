import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db
from models.users import Users
from models.links.links import Links

class LinksXRef(db.Model):
    __tablename__ = "LinksXRef"

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Users.user_id), primary_key=True)
    link_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Links.link_id), primary_key=True)

    user_links = db.relationship("Users", back_populates = "links_xref")


    def __init__(self, link_id, user_id):
        self.link_id = link_id
        self.user_id = user_id

class LinksXrefSchema(ma.Schema):
    class Meta:
        fields = ["link_id", "user_id"]

link_xref_schema = LinksXrefSchema()
link_xrefs_schema = LinksXrefSchema(many=True)