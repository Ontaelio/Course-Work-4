from marshmallow import Schema, fields

from project.setup.db import db
from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genre'
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
