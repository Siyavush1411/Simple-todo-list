from  .TextStyleMaster import TextStyle
from .TextLayout import TextMarkupBuilder

class ViewManager:
    
    def style_text(text):
        return TextStyle(text)

    def align_text(text):
        markup = TextMarkupBuilder(text)
        return markup