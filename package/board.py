from math import *
import pygame
import numpy as np
from .piece import Piece
class Board :
    def __init__(self, rowcols):
        self.board = np.zeros((rowcols,rowcols)).astype(int)
        self.pieces = []
        self.rows = rowcols
        self.cols = rowcols
        self.sqrsz = 100
        piece = None
        for row in range(self.rows):
            #tmp = []
            for col in range(self.cols):
                if((row==0 or row==self.rows-1)and 0<col<self.cols-1) :
                    self.board[row][col] = -1
                    piece = (col,row)#Piece(row,col,self.sqrsz,(78,53,36)) 
                    #tmp.append(-1)   
                elif((col==0 or col==self.cols-1)and 0<row<self.rows-1) :
                    self.board[row][col] = 1
                    piece = (col,row)#Piece(row,col,self.sqrsz,(78,53,136))
                    #tmp.append(1)
                else : 
                    self.board[row][col] = 0
                    #tmp.append(0)
                    continue
                self.pieces.append(piece)
            #self.board.append(tmp)
    
    def drawSquares(self, win) :
        win.fill((0,200,200))
        for row in range(self.rows):
            for col in range(row%2,self.cols,2):
                pygame.draw.rect(win,(0,30,30),(row*self.sqrsz,col*self.sqrsz,self.sqrsz,self.sqrsz))

    def drawInitPieces (self,win) :
        for piecePos in self.pieces:
            (col,row) = piecePos
            piece = None
            if(self.board[col][row]==-1): piece = Piece(row,col,self.sqrsz,(78,53,36))
            else : piece = Piece(row,col,self.sqrsz,(78,53,136))
            piece.draw(win)
    
    def getPos(self,x,y):
        return (floor(x//self.sqrsz),floor(y//self.sqrsz))
    
    def isValid(self , i ,j):
        return True if 0<=i<self.rows and 0<=j<self.cols else False

    def validCells(self,win,i1,j1) :
        #print(i1,j1)
        sz = self.cols
        cnt = [0,0,0,0]
        for i in range(sz):
            if(self.board[i][j1]!=0): cnt[1] += 1
        for j in range(sz):
            if(self.board[i1][j]!=0): cnt[0] += 1
        mn = min(i1,j1)
        ln = self.cols - 1
        mx = min(ln-j1,i1)
        i = i1 - mn
        j = j1 - mn
        while(i<=ln and j<=ln):
            if(self.board[i][j]!=0): cnt[2] += 1
            i += 1
            j += 1
        
        #print(i1,j1,mx)
        i = i1-mx
        j = j1+mx
        while(i<=ln and j>=0):
            #print(i,j)
            if(self.board[i][j]!=0): cnt[3] += 1
            i += 1
            j -= 1
        fy = [-1, 1, 0, 0, 1,-1,-1, 1]
        fx = [ 0, 0, 1,-1, 1,-1, 1,-1]
        arr = []
        
        for i in range(8):
            j = floor(i//2)
            if self.isValid(i1+cnt[j]*fx[i],j1+cnt[j]*fy[i]):
                arr.append((i1+cnt[j]*fx[i],j1+cnt[j]*fy[i]))
        #print(cnt)
        #print(arr)
        self.drawSquares(win)
        pygame.draw.rect(win,(100,255,100),(j1*self.sqrsz,i1*self.sqrsz,self.sqrsz,self.sqrsz))
        for x in arr :
            (col,row) = x
            pygame.draw.rect(win,(255,255,100),(row*self.sqrsz,col*self.sqrsz,self.sqrsz,self.sqrsz))
        return arr