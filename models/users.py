import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
# from models.links.links_xref import LinksXrefSchema

class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(), nullable=False, unique=True )
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), unique=True)
    role = db.Column(db.String(), nullable=False)
    is_photographer = db.Column(db.Boolean())
    bio = db.Column(db.String())
    about_me = db.Column(db.String())
    active = db.Column(db.Boolean(), default=True)

    # links_xref = db.relationship("LinksXRef", back_populates = "user_links")
   

    def __init__(self, username, first_name, last_name, email, password, phone, role, is_photographer, bio, about_me, active):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.role = role
        self.is_photographer = is_photographer
        self.bio = bio
        self.about_me = about_me
        self.active = active

    def new_user():
        return Users("", "", "", "", "", "", "", True, "", "", True)

class UsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'username', 'first_name', 'last_name', 'email', 'role', 'phone', 'is_photographer', 'bio', 'about_me', 'active','links_xref']
    links_xref = ma.fields.Nested("LinksXrefSchema", many=True)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)