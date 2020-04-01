from User.db import db


class Users(db.Document):
    public_id = db.StringField(required=True)
    name = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    admin = db.BooleanField(required=True)
