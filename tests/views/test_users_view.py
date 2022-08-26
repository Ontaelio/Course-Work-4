from unittest import mock

import pytest
from unittest.mock import patch, MagicMock
import sys
from flask import request
import jwt

from project.dao.models.genres_model import Genre
from project.dao.models.users_model import User
from project.views.auth import users

# @pytest.fixture
# @patch('project.views.decorators')
# def auth_required(func):
#     def __wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return __wrapper
from tests.conftest import request_context


class TestUsersView:
    @pytest.fixture
    def user(self, db):
        obj = User(email="email@aaa.com", password='12345', favorite_genre_id=1,
                   name='John', surname='Smith', )
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def genre(self, db):
        g = Genre(name="Комедия")
        db.session.add(g)
        db.session.commit()
        return g

    def test_many(self, client, user, genre):
        response = client.get("/users/")
        assert response.status_code == 200
        assert response.json == [{"id": user.id, "email": user.email,
                                  "password": user.password,
                                  "favorite_genre_id": user.favorite_genre_id,
                                  "name": user.name,
                                  "surname": user.surname,
                                  "role": user.role,
                                  "favorite_genre": genre.name}]

    def test_user_pages(self, client, user):
        response = client.get("/users/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/users/?page=2")
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_user(self, client, user, genre):
        # r_mock = mock.MagicMock() # return_value ={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IkthbGlha2EyMzNAbWFpbC5ydSIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNjYxNDI2OTU5fQ.m0StVsFdFIA9mVvNE6Bdt9YddDSUXwg-M92X9sIUwyw'})
        # r_mock.headers = {'Authorization': 'Bearer eyJ0e'}
        mmock = MagicMock(return_value=True)
        # with mock.patch('flask.request', r_mock):

        #response = client.get("/users/1/")
        with patch('jwt.decode', mmock):
            response = client.get("/users/1/", headers={'Authorization': 'Bearer 453645267'})

        # with patch.dict('sys.module', {'request.json': r_mock}):


        assert response.status_code == 200, 'Not authorized'
        assert response.json == {"id": user.id, "email": user.email,
                                 "password": user.password,
                                 "favorite_genre_id": user.favorite_genre_id,
                                 "name": user.name,
                                 "surname": user.surname,
                                 "role": user.role,
                                 "favorite_genre": None} # genre.name}

    def test_user_not_found(self, client, user):
        response = client.get("/users/2/")
        assert response.status_code == 404
