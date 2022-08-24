import pytest

from project.config import TestingConfig
from project.server import create_app
from project.setup.db import db as database


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    database.init_app(app)
    database.drop_all()
    database.create_all()
    database.session.commit()

    yield database

    database.session.close()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client


@pytest.fixture
def user_to_add():
    return {'email': 'test3@bbb.com',
            'password': 'secret',
            'role': 'admin',
            'name': 'John',
            'surname': 'Ohmygod',
            'favorite_genre_id': 1}


@pytest.fixture
def pass_hash():
    return['123456789',
    b"FfPIRKseRPU0Ie9LWD+BopJfEf00xcwhbWnKHospGpE="
    ]