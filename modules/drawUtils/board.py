from .values import *
from .square import Square


class Board:
    def __init__(self, N, colFlag):
        self.rocol = N+2
        self.squares = [[Square(i*SQUARE_SIZE, j*SQUARE_SIZE, BOARD_COLOR[(i+j+colFlag) % 2])
                         for i in range(self.rocol)] for j in range(self.rocol)]
        self.highlighedSquares = []

    def getSquareID(self, x, y):
        j, i = x//SQUARE_SIZE, y//SQUARE_SIZE
        return j, i

    def getSquare(self, x, y):
        j, i = self.getSquareID(x, y)
        print("Square at (", i, ",", j, ")")
        return self.squares[i][j]

    def getRow(self, x, y):
        i = self.getSquareID(x, y)[1]
        return i

    def getCol(self, x, y):
        j = self.getSquareID(x, y)[0]
        # print("Square at (", i, ",", j, ")")
        return j

    def getDiag(self, x, y):
        j, i = self.getSquareID(x, y)
        # print("Square at (", i, ",", j, ")")
        return self.rocol - j + i - 1

    def getRevDiag(self, x, y):
        j, i = self.getSquareID(x, y)
        # print("Square at (", i, ",", j, ")")
        return i+j

    def draw(self, win):
        for i in range(self.rocol):
            for j in range(self.rocol):
                self.squares[i][j].draw(win, False)

    def normalizeSquare(self, i, j):
        self.squares[i][j].highlight = False

    def isValid(self, i, j):
        return 0 <= i < self.rocol and 0 <= j < self.rocol
    # def setBoardColor(self) :
        # for i in range(0, self.rocol):
        #     for j in range(0, self.rocol):
    #             self.square[i][j] = BOARD_COLOR[(i+j)%2]
