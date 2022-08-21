from typing import Optional, List

from project.dao import UsersDAO
from project.exceptions import ItemNotFound
from project.dao.models.users_model import User


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_one(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, sort_by: Optional[str] = None) -> List[User]:
        return self.dao.get_all(page=page, sort_by=sort_by)
