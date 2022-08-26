from flask import request, abort, jsonify
from flask_restx import Namespace, Resource

from project.container import favorite_service
from project.exceptions import DuplicateItem
from project.setup.api.models import favorite, favorite_movies, favored_by, user, movie

api = Namespace('favorites')

@api.route('/movies/<int:mid>')
class AddFavoriteMovie(Resource):
    def post(self, mid):
        movie = mid
        uid = 3
        if movie is None:
            abort(400)

        if favorite_service.create(uid, movie):
            return "", 201

        raise DuplicateItem('Already exists')

    def delete(self, mid):
        uid = 1
        favorite_service.delete(uid, mid)
        return "", 204

    @api.marshal_with(user, code=200, description='OK')
    def get(self, mid):
        return favorite_service.get_users(mid)

#favorite_movies
@api.route('/users/<int:uid>')
class GetFavoriteMovie(Resource):
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, uid):
        return favorite_service.get_movies(uid)



