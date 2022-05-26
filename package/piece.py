import pygame

class Piece :
    def __init__(self,ro,col,sqsz,color) :
        self.ro = ro
        self.col = col
        self.x = ro*sqsz + sqsz//2
        self.y = col*sqsz + sqsz//2
        self.radius = sqsz//2 - sqsz//8
        self.color = color
      
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)