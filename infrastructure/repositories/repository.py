from abc import ABC, abstractmethod

class AbstractUserRepository(ABC):
    @abstractmethod
    def load_user_by_id(self, user_id):
        pass
    
    @abstractmethod
    def load_all_users(self):
        pass
    
    @abstractmethod
    def save_user(self, user):
        pass
    
    @abstractmethod
    def load_user_by_login(self, login):
        pass

    @abstractmethod
    def remove_user(self, user_id):
        pass