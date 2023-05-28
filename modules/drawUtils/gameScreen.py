from .board import Board
from .piece import Piece
from .values import *
import pygame


class GameScreen:
    def __init__(self, modeSize, modeColor):
        self.board = Board(modeSize, modeColor)
        self.size = self.board.rocol * SQUARE_SIZE
        self.pieces = {}
        self.rowCnt = [0] * self.board.rocol
        self.colCnt = [0] * self.board.rocol
        self.diaCnt = [0] * (2 * self.board.rocol - 1)
        self.revDiaCnt = [0] * (2 * self.board.rocol - 1)
        self.createUserPieces(BROWN if modeColor == 0 else PURPLE, modeSize)
        self.createOpponentPieces(
            BROWN if modeColor != 0 else PURPLE, modeSize)
        self.selectedPiece = (-1, -1)
        self.turn = True
        self.highlightPositions = []
        # print(self.rowCnt)
        # print(self.colCnt)
        # print(self.diaCnt)
        # print(self.revDiaCnt)
        # print(self.pieces.keys())
        # print(self.pieces[(-1, -1)])
        # print(self.pieces[(0, 1)].color, self.pieces[(0, 1)].x, self.pieces[(0, 1)].y)

    def createPiece(self, i, j, color, acc):
        centerX, centerY = i * SQUARE_SIZE + \
            SQUARE_SIZE//2, j * SQUARE_SIZE + SQUARE_SIZE//2
        self.rowCnt[self.board.getRow(centerX, centerY)] += 1
        self.colCnt[self.board.getCol(centerX, centerY)] += 1
        self.diaCnt[self.board.getDiag(centerX, centerY)] += 1
        self.revDiaCnt[self.board.getRevDiag(centerX, centerY)] += 1
        return Piece(centerX, centerY, color, i, j, acc)

    def createUserPieces(self, color, N):
        for i in range(N):
            piece = self.createPiece(i+1, 0, color, True)
            # print(piece.accessibility, piece.color)
            self.pieces[(0, i+1)] = piece
        for i in range(N):
            piece = self.createPiece(i+1, N+1, color, True)
            self.pieces[(N+1, i+1)] = piece
            # print(piece.accessibility, piece.color)

    def createOpponentPieces(self, color, N):
        for i in range(N):
            piece = self.createPiece(0, i+1, color, False)
            self.pieces[(i+1, 0)] = piece
        for i in range(N):
            piece = self.createPiece(N+1, i+1, color, False)
            self.pieces[(i+1, N+1)] = piece

    def isValidPosition(self, i, j, diffX, diffY, dist):
        fin_i = i + diffX * dist
        fin_j = j + diffY * dist
        

        
        if not self.board.isValid(fin_i, fin_j):
            return False

        selected_piece_color = self.pieces[self.selectedPiece].color

        if (fin_i, fin_j) in self.pieces.keys() and self.pieces[(fin_i, fin_j)].color == selected_piece_color:
            print("Hello!!")
            return False
        
        print("Ahhhh... ", diffX, diffY)

        if diffX == 0 :
            for jj in range (j, fin_j, diffY) :
                print(fin_i, jj)
                if (fin_i, jj) in self.pieces.keys():
                    if self.pieces[(fin_i, jj)].color != selected_piece_color:
                        return False
        
        elif diffY == 0:
            for ii in range (i, fin_i, diffX) :
                print(ii, fin_j)
                if (ii, fin_j) in self.pieces.keys():
                    if self.pieces[(ii, fin_j)].color != selected_piece_color:
                        return False
        else :     
            for ii in range (i, fin_i, diffX) :
                for jj in range (j, fin_j, diffY) :
                    print(ii, jj)
                    if (ii, jj) in self.pieces.keys():
                        if self.pieces[(ii, jj)].color != selected_piece_color:
                            return False
        return True

    def setHighlightPositions(self):
        if (self.selectedPiece == (-1, -1)):
            return
        self.highlightPositions.append(self.selectedPiece)

        rcnt = self.rowCnt[self.selectedPiece[0]]
        ccnt = self.colCnt[self.selectedPiece[1]]
        dia = self.diaCnt[self.board.rocol - self.selectedPiece[1] + self.selectedPiece[0] - 1]
        revDia = self.revDiaCnt[self.selectedPiece[0]+self.selectedPiece[1]] 
        print("Vals", rcnt, ccnt, dia, revDia)

        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        dists = [dia, ccnt, revDia, rcnt, dia, ccnt, revDia, rcnt]
        for k in range(0, 8) :
            (i, j) = self.selectedPiece
            if self.isValidPosition(i, j, dx[k], dy[k], dists[k]):
                self.highlightPositions.append((i + dx[k] * dists[k], j + dy[k] * dists[k]))
        

        # for i in range(-self.rowCnt[i], self.rowCnt[i]):

    def selectPiece(self, x, y):
        j, i = self.board.getSquareID(x, y)
        if (i, j) not in self.pieces.keys():
            return
        piece = self.pieces[(i, j)]
        if (piece.isIn(x, y, self.turn)):
            self.selectedPiece = (i, j)
            self.setHighlightPositions()
        print("Select : ", self.selectedPiece)

    def movePiece(self, x, y):
        j, i = self.board.getSquareID(x, y)
        print(i, j)

        
        if ((i, j) == self.selectedPiece):
            print("Same place!!")
            self.selectedPiece = (-1, -1)
            return

        if (i,j) not in self.highlightPositions:
            print("Invalid position!!")
            if (i, j) in self.pieces.keys() and self.pieces[(i, j)].color == self.pieces[self.selectedPiece].color:
                self.highlightPositions.clear()
                self.selectPiece(x, y)
                return
            self.selectedPiece = (-1, -1)
            return

        piece = self.pieces[self.selectedPiece]
        self.rowCnt[i] += 1
        self.rowCnt[self.selectedPiece[0]] -= 1
        self.colCnt[j] += 1
        self.colCnt[self.selectedPiece[1]] -= 1
        self.diaCnt[self.board.rocol - j + i - 1] += 1
        self.diaCnt[self.board.rocol - self.selectedPiece[1] +
                    self.selectedPiece[0] - 1] -= 1
        self.revDiaCnt[i+j] += 1
        self.revDiaCnt[self.selectedPiece[0]+self.selectedPiece[1]] -= 1
        piece.move(j, i)
        # print("Move : ", j, i)
        self.pieces[(i, j)] = piece
        self.pieces.pop(self.selectedPiece)
        # print(self.pieces.keys())
        self.selectedPiece = (-1, -1)
        self.turn = not self.turn

    def deletePiece(self, x, y):
        return

    def handleClickEvent(self, x, y):
        j, i = self.board.getSquareID(x, y)
        # print("Handle : ", j, i)
        if (self.selectedPiece == (-1, -1)):
            self.selectPiece(x, y)
        else:
            self.movePiece(x, y)
            if(self.selectedPiece == (-1, -1)):
                self.highlightPositions.clear()
        # print(self.rowCnt)
        # print(self.colCnt)
        # print(self.diaCnt)
        # print(self.revDiaCnt)
        # print(self.selectedPiece)
        # print(self.pieces.keys())
        # square = self.board.getSquare(x, y)

    def highlight(self, win):
        for pos in self.highlightPositions:
            self.board.squares[pos[0]][pos[1]].draw(win, True)

    def draw(self, win):
        self.board.draw(win)
        self.highlight(win)
        for piece in self.pieces.values():
            piece.draw(win)
        pygame.display.update()

# pygame.init()
# win = pygame.d
# borad = Board(6)
# borad.draw()
