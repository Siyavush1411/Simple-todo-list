import os
from .view_core.ViewManager import ViewManager
from core.services.user_services.user_choose import UserOperation
from core.common import WELCOME_TEXT, UI_TEXT, SOLUTIONS

class Menu:
    def show_main_menu(self):
        os.system('clear')
        welcome_text = ViewManager.style_text(WELCOME_TEXT).bright_magenta
        print(ViewManager.align_massive_center(str(WELCOME_TEXT)))
        self.show_menu_ui()
        print(self.choose_solution())

            
    def choose_solution(self) -> int:

        
        while True:
            user_choose = UserOperation.user_request()
            if user_choose in SOLUTIONS:
               return SOLUTIONS.get(user_choose, "Пожалуйста введите число от 1 до 5")
           
           
           
    def show_menu_ui(self):
        try:
            styled_line = str(ViewManager.style_text(UI_TEXT).green.bold)
            print(ViewManager.align_massive_center(styled_line))
        except Exception as e:
            print(f"Ошибка: {e}")
