from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser

api = Namespace('users')


@api.route('/')
class UsersView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all users.
        """
        return user_service.get_all(**page_parser.parse_args())


@api.route('/<int:user_id>/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, user_id: int):
        """
        Get user by id.
        """
        return user_service.get_item(user_id)
