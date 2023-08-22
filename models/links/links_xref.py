from db import db

links_xref = db.Table(
    "links_xref",
    db.Model.metadata,
    db.Column("link_id", db.ForeignKey('Links.link_id'), primary_key=True),
    db.Column("user_id", db.ForeignKey("Users.user_id"), primary_key=True)
)