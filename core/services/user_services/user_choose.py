class UserOperation:
    
    @staticmethod
    def user_request() -> int : 
        while True:
            try:
                user_choose = int(input())
                return user_choose
            except ValueError:
                print("Введите числовое значение")