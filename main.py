import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame 
from package.board import Board

pygame.init()
run = False
lgn = True
gg = 0
unsel = (0,30,30)
sel = (78,53,136)
valarr = []
col1 = col2 = col3 = col4 = unsel
rocol = -1
surface = pygame.display.set_mode((600, 800))
while lgn :
    fnt = pygame.font.Font(None,50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lgn = False
        if event.type == pygame.MOUSEBUTTONUP:
            (x,y) = pygame.mouse.get_pos()
            if 50<=x<=275 and 200<=y<=300:
                col1 = unsel if col1==sel else sel
                rocol = 6 if col1==sel else -1
                col2 = unsel
            if 300<=x<=525 and 200<=y<=300:
                col2 = unsel if col2==sel else sel
                rocol = -1 if col2!=sel else 8
                col1 = unsel
            
            if 100<=x<=225 and 600<=y<=650:
                if rocol >=0 :
                    lgn = False
                    run = True
            if 350<=x<=475 and 600<=y<=650:
                lgn = False
    surface.fill((0,200,200))
    txt_sur = fnt.render("Welcome to Line of Action",True,(0,25,25))
    surface.blit(txt_sur,(75,50))
    
    rect1 = (50,150,225,100)
    surface.fill(col1,rect1)
    txt_sur = fnt.render("6X6",True,(175,175,175))
    surface.blit(txt_sur,(130,185))
    
    rect1 = (300,150,225,100)
    surface.fill(col2,rect1)
    txt_sur = fnt.render("8X8",True,(175,175,175))
    surface.blit(txt_sur,(380,185))
    
    rect1 = (50,300,225,100)
    surface.fill(col3,rect1)
    txt_sur = fnt.render("Brown",True,(175,175,175))
    surface.blit(txt_sur,(85,330))
    
    rect1 = (300,300,225,100)
    surface.fill(col4,rect1)
    txt_sur = fnt.render("Purple",True,(175,175,175))
    surface.blit(txt_sur,(370,330))

    rect1 = (50,450,225,100)
    surface.fill(col3,rect1)
    txt_sur = fnt.render("vsHuman",True,(175,175,175))
    surface.blit(txt_sur,(85,480))
    
    rect1 = (300,450,225,100)
    surface.fill(col4,rect1)
    txt_sur = fnt.render("vsAI",True,(175,175,175))
    surface.blit(txt_sur,(370,480))
    
    fnt = pygame.font.Font(None,30)

    rect1 = (100,600,125,50)
    surface.fill((78,53,36),rect1)
    txt_sur = fnt.render("Play",True,(175,175,175))
    surface.blit(txt_sur,(140,615))
    
    rect1 = (350,600,125,50)
    surface.fill((78,53,36),rect1)
    txt_sur = fnt.render("Quit",True,(175,175,175))
    surface.blit(txt_sur,(390,615))
    pygame.display.flip()

surface = pygame.display.set_mode(((rocol+2)*100, (rocol+2)*100))
inp = 6 #input("Size of the board : ")
board = Board(rocol+2)
idx = -1
#    
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            (x,y) = pygame.mouse.get_pos()
            if idx != -1 :
                (i,j) = board.getPos(x,y)
                if (j,i) in valarr :
                    j1,i1 = board.pieces[idx]
                    #(j1,i1) = board.getPos(x1,y1)
                    tmp = board.board[j1][i1]
                    board.board[j1][i1] = board.board[j][i]
                    board.board[j][i] = tmp
                    #board.pieces[idx] = ((i+.5)*board.sqrsz,(j+.5)*board.sqrsz)
                    #board.pieces[idx] = ((i+.5)*board.sqrsz,(j+.5)*board.sqrsz)
                    board.pieces[idx] = i,j
                    #board.pieces[idx].y = (j+.5)*board.sqrsz
                idx = -1
                valarr = []
                gg = 0
            else :
                for i in range(len(board.pieces)):
                    
                    cx,cy = board.pieces[i]
                    cx = cx*board.sqrsz+board.sqrsz//2
                    cy = cy*board.sqrsz+board.sqrsz//2
                    #print(cx,cy,x,y)
                    #cy = board.pieces[i].y
                    rad = board.sqrsz//2-board.sqrsz//8
                    if (x-cx)*(x-cx)+(y-cy)*(y-cy)<=rad*rad:
                        idx = i
                        gg = 1
                        (j1,i1) = board.getPos(x,y)
                        valarr = board.validCells(surface,i1,j1)
                        break
    if(gg==0) : board.drawSquares(surface)
    board.drawInitPieces(surface)
    pygame.display.flip()
#print(8)
n, m = board.board.shape
print(n)
for i in range(n):
    for j in range(m):
        print(board.board[i][j],end = " ")