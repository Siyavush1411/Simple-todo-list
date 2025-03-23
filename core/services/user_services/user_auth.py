from core.entities.user import User
from infrastructure.repositories.user_repository import UserRepository
from core.common.hash_function import HashFunction

class UserAuth:
    def __init__(self):
        self.user_repository = UserRepository()
        
    def register(self, login, password):
        password = HashFunction.hash_function(password)
        user = User(None, login, password)
        self.user_repository.add_user(user)
        
    def login(self, login, password):
        user = self.user_repository.load_user_by_login(login)
        print(password)
        if user and user.password == HashFunction.hash_function(password):
            return user
        return None