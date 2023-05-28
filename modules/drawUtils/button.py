from .values import *

class Button :
    def __init__(self, attrs):
        self.text, self.x, self.y, self.width, self.height = attrs
        self.selected = False
        self.color = BUTTON_COLOR_UNSELECTED
    
    def switchState(self):
        if self.selected:
            self.selected = False
            self.color = BUTTON_COLOR_UNSELECTED
        else:
            self.selected = True
            self.color = BUTTON_COLOR_SELECTED
    
    def draw(self, win):
        rect1 = (self.x, self.y, self.width, self.height)
        # pygame.draw.rect(win, self.color, rect1)
        win.fill(self.color, rect1)
        # win.blit(self.text, (self.x + 80, self.y + 35))

