from core.entities.user import User
from infrastructure.repositories.user_repository import UserRepository
from core.common.hash_function import HashFunction

class UserAuth:
    def __init__(self):
        self.user_repository = UserRepository()
        
    def register(self, login : str, password : str) -> None:
        password = HashFunction.hash_function(password)
        user = User(None, login, password)
        self.user_repository.add_user(user)
        
    def login(self, login : str, password : str) -> User | None:
        user = self.user_repository.load_user_by_login(login)
        if user and str(user.password) == str(HashFunction.hash_function(password)):
            return user
        return None