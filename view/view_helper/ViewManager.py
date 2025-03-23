from  .TextStyle import TextStyle
from .TextLayout import TextMarkupBuilder

class ViewManager:
    
    @staticmethod
    def style_text(text: str) -> str:
        return TextStyle(text)
    
    @staticmethod
    def align_text(text: str) -> str:
        markup = TextMarkupBuilder(text)
        return markup
    
    def align_massive_center(text: str) -> str:
        str_list = text.splitlines()
        centered_lines = []
        for line in str_list:
            centered_lines.append(ViewManager.align_text(line).center)
        return "\n".join(centered_lines) 