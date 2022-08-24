from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тим Бёртон'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=255, example='Марс Атакует!'),
    'description': fields.String(required=True, max_length=255, example='...'),
    'trailer': fields.String(required=True, max_length=255, example='https://www.youtube.com/watch?v=Qjpmysz4x-4'),
    'year': fields.Integer(required=True, example=1999),
    'rating': fields.Float(required=True, example=7.2),
    'genre_id': fields.Integer(required=True, example=1),
    'genre': fields.String(attribute='genre.name', example='Комедия'),
    # 'genre': fields.Nested(genre),
    'director_id': fields.Integer(required=True, example=2),
    'director': fields.String(attribute='director.name', example='Тим Бёртон'),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=200, example='test@test.com'),
    'password': fields.String(required=True, max_length=255, example='123'),
    'role': fields.String(max_length=100, example='user'),
    'name': fields.String(max_length=100, example='John'),
    'surname': fields.String(rmax_length=100, example='Smith'),
    'favorite_genre_id': fields.Integer(example=1),
    'favorite_genre': fields.String(attribute='genre.name', example='Комедия'),
})
