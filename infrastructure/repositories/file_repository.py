from .repository import AbstractUserRepository
from core.entities.user import User
from core.common import USER_FILE_PATH
import os

class UserRepository(AbstractUserRepository):
    def __init__(self, file_path=USER_FILE_PATH):
        self.file_path = file_path
        self.users = self._load_users()

    def _load_users(self):
        with open(self.file_path, 'r') as file:
            users = []
            for line in file:
                user_data = line.strip().split(',')
                user = User(id=user_data[0], login=user_data[1], password=user_data[2])
                users.append(user)
            return users

    def _save_users(self):
        with open(self.file_path, 'w') as file:
            for user in self.users:
                file.write(f"{user.id},{user.login},{user.password}\n")

    def add_user(self, user : User):
        self.users.append(user)
        self._save_users()

    def load_user_by_id(self, user_id : int):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def remove_user(self, user_id : int):
        self.users = [user for user in self.users if user.id != user_id]
        self._save_users()
