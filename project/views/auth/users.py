from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.dao.models.users_model import UserSchema
from project.setup.api.models import user
from project.setup.api.parsers import page_parser
from project.views.decorators import auth_required

api = Namespace('users')

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)


@api.route('/')
class UsersView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all users.
        """
        return user_service.get_all(**page_parser.parse_args())
        # all_users = user_service.get_all(**page_parser.parse_args())
        # return users_schema.dump(all_users) #, 200


@api.route('/<int:user_id>/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    @auth_required
    def get(self, user_id: int):
        """
        Get user by id.
        """
        return user_service.get_one(user_id)

    @api.response(404, 'Not Found')
    @auth_required
    def patch(self, user_id: int):
        user_d = request.json
        user_service.update(user_id, user_d)
        return "", 204

    @api.response(404, 'Not Found')
    @auth_required
    def put(self, user_id: int):
        passwords = request.json
        if user_service.change_password(user_id, passwords):
            return "", 204
        return {"error": "Incorrect password"}, 401


