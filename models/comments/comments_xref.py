from db import db

comments_xref = db.Table(
    "comments_xref",
    db.Model.metadata,
    db.Column("comment_id",db.ForeignKey('Comments.comment_id'), primary_key=True),
    db.Column("user_id", db.ForeignKey("Users.user_id"), primary_key=True)
)