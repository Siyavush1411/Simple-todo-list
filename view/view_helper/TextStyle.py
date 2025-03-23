'''This class need for text customize'''
class TextStyle:
    def __init__(self, text):
        self.text = text
        self.style_list = []
    
    def __getattr__(self, style):       
        styles = {
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'bright_black': '\033[90m',
            'bright_red': '\033[91m',
            'bright_green': '\033[92m',
            'bright_yellow': '\033[93m',
            'bright_blue': '\033[94m',
            'bright_magenta': '\033[95m',
            'bright_cyan': '\033[96m',
            'bright_white': '\033[97m',
            'reset': '\033[0m',
            'bold': '\033[1m',
            'underline': '\033[4m',
        }
        if style in styles:
            self.style_list.append(styles[style])
            return self
        
    def __str__(self):
        return f"{''.join(self.style_list)}{self.text}\033[0m"