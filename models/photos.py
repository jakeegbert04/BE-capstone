import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
# from models.organizations import OrganizationsSchema
from db import db


class Photos(db.Model):
    __tablename__ = "Photos"

    photo_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    size = db.column(db.String(), nullable=False)
    file_type = db.column(db.String, nullable=False)
    photo_name = db.column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def __init__(self, size, file_type, photo_name, active):
        self.size = size
        self.file_type = file_type
        self.photo_name = photo_name
        self.active = active

    def new_photo():
        return Photos("", "", "", True)

class PhotoSchema(ma.Schema):
    class Meta:
        fields = ['photo_id', 'size', 'file_type', 'photo_name', 'active']
    


photo_schema = PhotoSchema()
photos_schema = PhotoSchema(many=True)