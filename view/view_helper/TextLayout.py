
import os

class TextMarkupBuilder:
    def __init__(self, text):
        self.text = text
        
    def __str__(self):
        return str(self.text)
    
    def __getattr__(self, align):
        
        width = os.get_terminal_size().columns
        
        if align == 'center':
            return self.text.center(width)
        elif align == 'right':
            return self.text.rjust(width)
        elif align == 'left':
            return self.text.ljust(width)
        
        
