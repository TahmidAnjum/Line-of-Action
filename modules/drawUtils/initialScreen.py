from .values import *
from .button import Button
import pygame

class InitialScreen:
    def __init__(self) :
        self.width = INITIAL_SCREEN_WIDTH
        self.height = INITIAL_SCREEN_HEIGHT
        self.color = BACKGROUND_COLOR
        self.setButtons()
        # self.playButton = Button(PLAY_BUTTON_ATTRS)
        # self.quitButton = Button(QUIT_BUTTON_ATTRS)
        # self.sixVsSixButton = Button(SIX_BUTTON_ATTRS)
        # self.eightVsEighthButton = Button(EIGHT_BUTTON_ATTRS)
        # self.vsHumanButton = Button(VSHUMAN_BUTTON_ATTRS)
        # self.vsAIButton = Button(VSAI_BUTTON_ATTRS)
        # self.brownButton = Button(BROWN_BUTTON_ATTRS)
        # self.purpleButton = Button(PURPLE_BUTTON_ATTRS)
        # self.draw()
    

    def setButtons(self) :
        self.buttons = []
        buttonAttrs = [ 
            PLAY_BUTTON_ATTRS, 
            QUIT_BUTTON_ATTRS, 
            SIX_BUTTON_ATTRS, 
            EIGHT_BUTTON_ATTRS, 
            VSHUMAN_BUTTON_ATTRS, 
            VSAI_BUTTON_ATTRS, 
            BROWN_BUTTON_ATTRS, 
            PURPLE_BUTTON_ATTRS
        ]
        for attr in buttonAttrs :
            self.buttons.append(Button(attr))

    def draw(self, win) :
        # initialWindow = pygame.display.set_mode((self.width, self.height))
        for button in self.buttons:
            button.draw(win)
            #initialWindow.blit()
        pygame.display.update()