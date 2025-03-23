from core.entities.user import User
from infrastructure.repositories.user_repository import UserRepository

class UserDataOperations:
    def __init__(self):
        self.user_repository = UserRepository()
        
    def get_user_by_id(self, user_id):
        return self.user_repository.load_user_by_id(user_id)
    
    def get_user_by_login(self, login):
        return self.user_repository.load_user_by_login(login)
    
    def remove_user(self, user_id):
        self.user_repository.remove_user(user_id)
        
    def get_all_users(self):
        return self.user_repository.users