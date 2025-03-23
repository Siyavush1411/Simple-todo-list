from core.entities.user import User
from infrastructure.repositories.user_repository import UserRepository

class UserAuth:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = UserRepository()
        