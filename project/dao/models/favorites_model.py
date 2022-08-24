from project.setup.db import db
from project.setup.db import models


class Favorites(models.Base):
    __tablename__ = 'favorite'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    movie = db.relationship("Movie")
