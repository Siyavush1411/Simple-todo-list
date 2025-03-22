import os
from .view_core.ViewManager import ViewManager

class Menu:
    view = ViewManager
    
    def show_main_menu(self):
        os.system('clear')
        choose = self.user_request
        print(self.view.align_text("WELCOME").center)
        self.show_menu_ui()
        print(self.choose_solution)
        
        
    def user_request() -> int : 
        while True:
            try:
                user_choose = int(input())
                return user_choose
            except ValueError:
                print("Введите числовое значение")
            
    def choose_solution(self) -> int:
        solutions = {
            1 : "заметки",
            2 : "обновление заметки",
            3 : "удаление заметки",
            4 : "язык"
        }
        user_choose = self.user_request()
        
        while True:
            if user_choose in solutions:
               return solutions[user_choose]
            else:
                print("Ведите числа в диапазоне от 1 до 4")
           
           
           
    def show_menu_ui(self):
        ui = '''
___________________________
|1 | "заметки"            |
|_________________________|
|2 | "обновление заметки" |
|__|______________________|
|3 | "удаление заметки"   |
|__|______________________|
|4 | "язык"               |
|__|______________________|
        '''
        styled_ui = self.view.style_text(ui).green.bold
        print(self.view.align_text(styled_ui))