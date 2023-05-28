import pygame
from .values import *

class Piece :
    def __init__(self, x, y, c, i, j, acc):
        self.x = x
        self.y = y
        self.color = c
        self.sqrI = i
        self.sqrJ = j
        self.accessibility = acc
        self.selected = False
        self.out = False

    def isIn(self, x, y, turn) :
        #print(x,y,"Is in : ",self.accessibility,turn, self.color)
        if (self.x - x) * (self.x - x) + (self.y - y) * (self.y - y) <= PIECE_RADIUS*PIECE_RADIUS and not(self.accessibility^turn):
            #print("Is in (2): ",(self.accessibility^turn))
            return True
        return False

    def move(self, j, i) :
        self.x = j*SQUARE_SIZE + SQUARE_SIZE//2
        self.y = i*SQUARE_SIZE + SQUARE_SIZE//2

    def draw(self, win) :
        if(self.out) : pass
        # circle = (self.x, self.y, PIECE_RADIUS)
        pygame.draw.circle(win,self.color,(self.x,self.y),PIECE_RADIUS)
