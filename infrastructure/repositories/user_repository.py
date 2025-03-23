from .repository import AbstractUserRepository
from core.entities.user import User
from core.common import USER_FILE_PATH

class UserRepository(AbstractUserRepository):
    def __init__(self, file_path=USER_FILE_PATH):
        print(file_path)
        self.file_path = file_path
        self.users = self._load_users()
        self.next_id = self._get_next_id()

    def _load_users(self) -> list[User]:
        file_path = self.file_path
        if not file_path.exists():
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.touch()

        with file_path.open("r", encoding="utf-8") as file:
            users = []
            for line in file:
                user_data = line.strip().split(',')
                if len(user_data) < 3:
                    continue
                user = User(id=int(user_data[0]), login=user_data[1], password=user_data[2])
                users.append(user)

        return users

    def _save_users(self) -> None:
        with open(self.file_path, 'w') as file:
            for user in self.users:
                file.write(f"{user.id},{user.login},{user.password}\n")

    def _get_next_id(self) -> int:
        if not self.users:
            return 1
        return max(user.id for user in self.users) + 1

    def add_user(self, user : User) -> None:
        user.id = self.next_id
        self.next_id += 1
        self.users.append(user)
        self._save_users()

    def load_user_by_id(self, user_id : int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def load_user_by_login(self, login : str) -> User:
        for user in self.users:
            if user.login == login:
                return user
        return None
    
    def remove_user(self, user_id : int) -> None:
        self.users = [user for user in self.users if user.id != user_id]
        self._save_users()
        self.next_id = self._get_next_id()
