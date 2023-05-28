import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame 
from drawUtils.initialScreen import InitialScreen
from drawUtils.gameScreen import GameScreen
from drawUtils.board import Board

pygame.init()

def handleInitialScreen() : 
    initialScreen = InitialScreen()
    win = pygame.display.set_mode((initialScreen.width, initialScreen.height))
    win.fill((0,200,200))
    inInitScreen = True
    while inInitScreen: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inInitScreen = False
        initialScreen.draw(win)

def gg()  :
    gameScreen = GameScreen(6, 0)
    win = pygame.display.set_mode((gameScreen.size, gameScreen.size))
    inGameScreen = True
    while inGameScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inGameScreen = False
            if event.type == pygame.MOUSEBUTTONUP:
                (x,y) = pygame.mouse.get_pos()
                gameScreen.handleClickEvent(x,y)
        gameScreen.draw(win)
gg()
# gg = Board(6)
# gg.setBoardColor()
# handleInitialScreen()