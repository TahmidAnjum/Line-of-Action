from .values import SQUARE_SIZE
from .values import HIGHLIGHT_COLOR

class Square :
    def __init__(self, x, y, color) : 
        self.color = color
        self.x = x
        self.y = y
        self.size = SQUARE_SIZE

    def draw(self, win, highlight):
        sqr = (self.x, self.y, self.size, self.size)
        win.fill(self.color if not highlight else HIGHLIGHT_COLOR, sqr)
