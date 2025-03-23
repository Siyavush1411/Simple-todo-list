import os
from view.view_helper import ViewManager
from core.services import UserOperation, UserAuth
from core.common import WELCOME_TEXT, UI_TEXT, SOLUTIONS, USER_LOGIN_FORM, LOGIN_MESSAGE

class Menu:
    def __init__(self):
        self._user_choice = None
        self.auth = UserAuth()
        
    def show_main_menu(self) -> None:
        os.system('clear')
        welcome_text = ViewManager.style_text(WELCOME_TEXT).bright_magenta
        print(ViewManager.align_massive_center(str(welcome_text)))
        self.user_form()
        self.menu_form()
        print(self.choose_solution())

    def choose_solution(self) -> int:
        while True:
            self._user_choice = UserOperation.user_request()
            if self._user_choice in SOLUTIONS:
               return SOLUTIONS.get(self._user_choice, "Пожалуйста введите число от 1 до 5")
           
    def menu_form(self) -> None:
        try:
            styled_line = str(ViewManager.style_text(UI_TEXT).green.bold)
            print(ViewManager.align_massive_center(styled_line))
        except Exception as e:
            print(f"Ошибка: {e}")

    def user_form(self) -> None:
        try:
            while True:
                user_login_form = ViewManager.style_text(USER_LOGIN_FORM).magenta.bold
                print(ViewManager.align_massive_center(str(user_login_form)))
                choose = int(input("Введите 1 чтобы войти, 2 чтобы регистрироваться: "))
                if choose == 1:
                    login = input("Введите логин: ")
                    password = input("Введите пароль: ")
                    is_log = self.auth.login(login, password)
                    if is_log:
                        print("Вы успешно вошли")
                        break
                    else:
                        login_message = ViewManager.style_text(LOGIN_MESSAGE).magenta.bold
                        print(ViewManager.align_massive_center(str(login_message)))
                elif choose == 2:
                    login = input("Введите логин: ")
                    password = input("Введите пароль: ")
                    self.auth.register(login, password)
                    break
                else:
                    print("Введите 1 или 2")
        except Exception as e:
            print(f"Ошибка: {e}")   

