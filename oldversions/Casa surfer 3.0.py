import pygame
import time
from random import *
import random
pygame.init ( )
clock = pygame.time.Clock ( )  # controle du temps: images par secondes
# Paratmetre fenetre
displayLargeur = 1024
displayHauteur = 768
gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))  # creer fenetre
pygame.display.set_caption ('Casa circuit')
# Banque a couleur
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 240, 0)
BLUE = (0, 0, 255)
RED = (240, 0, 0)
GREY = (120, 120, 120)
WHITE = (255, 255, 255)
B_GREEN = (0, 255, 0)
B_RED = (255, 0, 0)
# Load les images
mortFenetre = pygame.image.load ('mort.png').convert_alpha ( )
player = pygame.image.load ('player.png')
taxi = pygame.image.load ('obstacle.png')
background = pygame.image.load ('background.png')
introback = pygame.image.load ('introback.jpg')
player1 = pygame.image.load ('player1.png')
mort = pygame.image.load ('mort.png')
mort = pygame.transform.scale(mort, (700,500))
bus = pygame.image.load('bus.png')
explosion = pygame.image.load('explosion.gif')
glisse = pygame.image.load('glisse.png')
saute = pygame.image.load('saute.png')
bande = pygame.image.load('bande.png')
# position initale des objets
posPlayerY = 250
posPlayerX = 20
positionPlayer = [posPlayerX, posPlayerY]
playerLargeur = 100
playerHauteur = 200
taxiLargeur = 200
taxiHauteur = 200
busLargeur = 270
busHauteur = 200
couloir = [(1400, 450), (1400, 250), (1400, 50)] # 1400 pour qu'on ne les voit âs apparaitre
taxiPos = (0, 0)
taxisPos = []
busPos = (0,0)
bussPos = []
obstaclesPos = [taxisPos, bussPos]
obstaclePos = (0,0) #0 juste pr avoir une valeur de base
obstacles = []
profondeurJ = 1
nbrBandeVisible = 11
nbrObstacleVisible = 4
posBandeY = [245,450]
bandePos = (0,0)
bandesPos = []
# Reperes temporels
moving = 0
speedTaxi = -10
speedBus = -5
speedBande = -3
taxiSpawn = 0
dessinage = 0
mouvement = 0
randomlist = [3000,3500,4000,4500,5000,5500,6000] # nb de secondes entre 2 apparitions
# Les différents etats du jeu
intro = False
dead = False
EXPLO = False
GLISSER = False
SAUTER = False
DIFFIC = False
PAUSE  = False
obtstacleType = taxi



def quitgame():
    pygame.quit ( )
    quit ( )

def restart() : #vider les listes + coordonnées initiales
    global taxisPos, posPlayerX, posPlayerY, obstaclesPos, obstacles, profondeurJ
    obstaclesPos = []
    obstacles = []
    taxisPos = []
    bussPos = []

    profondeurJ = 1
    posPlayerX = 20
    posPlayerY = 250
    gameloop()

def apparitionBandes():
    global nbrBandeVisible, bandePos, bandesPos, posBandeY
    for w in range(nbrBandeVisible):
        bandePos = (15 + (130*w),posBandeY[0])
        bandesPos.append(bandePos)
    for w in range(nbrBandeVisible):
        bandePos = (15 + (130*w),posBandeY[1])
        bandesPos.append(bandePos)




def apparitionObstacles():
    global taxisPos, taxiPos, busPos, bussPos, obstaclesPos, obtstacleType, obstaclePos
    taxiPos = random.choice(couloir)
    busPos = random.choice(couloir)
    randint(0, 1) # 0 = taxi et 1 = bus
    if randint(0, 1) == 0:
        taxisPos.append(taxiPos)
       # obstacles.append(taxiPos)
    elif randint(0,1) == 1:
        bussPos.append(busPos)
        #obstacles.append(busPos)
    obstaclesPos = [taxisPos, bussPos]

def unpause():
    global PAUSE
    global dead
    PAUSE = False
    dead = False


def paused():

    gameDisplay.blit (mort, ((1300-700)/2, (700-500)/2))
    largeText = pygame.font.SysFont ("arial", 115)
    TextSurf, TextRect = text_objects ("Pause !", largeText, GREY)
    TextRect.center = ((((1300-700)/2))+350, ((700-500)/2)+150)
    gameDisplay.blit (TextSurf, TextRect)

    while PAUSE:
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                unpause ( )

        button ("Continue", 400, 450, 100, 50, GREY, B_GREEN, unpause)
        button ("Quit", 550, 450, 100, 50, GREY, BROWN, quitgame)
        button ("Restart", 700, 450, 100, 50, GREY, B_GREEN, gameloop)

        pygame.display.update ( )
        clock.tick (15)

def text_objects(text, font, color):
    textSurface = font.render (text, True, color)
    return textSurface, textSurface.get_rect ( )


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos ( )
    click = pygame.mouse.get_pressed ( )

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect (gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action ( )
    else:
        pygame.draw.rect (gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont ("arial", 30)
    textSurf, textRect = text_objects (msg, smallText, WHITE)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit (textSurf, textRect)

def deadFenetre():
    global dead, textMort
    if dead == True:
        gameDisplay.blit (mort, ((1300-700)/2, (700-500)/2))
        largeText = pygame.font.SysFont ("arial", 70)
        TextSurf, TextRect = text_objects (textMort, largeText,WHITE)
        TextRect.center = ((((1300-700)/2))+350, ((700-500)/2)+150)
        gameDisplay.blit (TextSurf, TextRect)

    while dead:
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
        button ("Quitter", 400, 450, 180, 50, RED, B_RED, gameintro)
        button ("Recommencer", 700, 450, 180, 50, GREEN, B_GREEN, restart)

        pygame.display.update ( )



#def difficulteFenetre() :

 #   if DIFFIC == True :
  #      gameDisplay.fill(WHITE)

def gameintro():
    global gameDisplay, displayLargeur, displayHauteur, intro, dead, DIFFIC
    intro = True
    dead = False
    displayLargeur = 1024
    displayHauteur = 768
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    while intro:
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit ( )
                    quit ( )
        gameDisplay.blit (introback, (0, 0))
        largeText = pygame.font.SysFont ("comic sans ms", 105)
        TextSurf, TextRect = text_objects ("Casa Surfer", largeText, B_GREEN)
        TextRect.center = ((displayLargeur / 2), (displayHauteur / 12))
        gameDisplay.blit (TextSurf, TextRect)
        button ("Jouer", 250, 200, 200, 50, GREY, B_GREEN, restart)
        button ("Difficulté", 550, 200, 200, 50, GREY, B_RED,quitgame)
        button ("Description", 250, 350, 200, 50, GREY, B_GREEN, restart)
        button ("Apparence", 550, 350, 200, 50, GREY, B_RED, quitgame)
        button ("Credit", 250, 500, 200, 50, GREY, B_GREEN, restart)
        button ("Quitter", 550, 500, 200, 50, GREY, B_RED, quitgame)

        pygame.display.update ( )
        clock.tick (15)

def DynamiqueduJeu():
    global taxiPos, taxisPos, moving, nbrObstacleVisible, speedTaxi, speedBande, speedBus, taxiSpawn, dead, positionPlayer, playerHauteur, playerLargeur, posPlayerY, posPlayerX, randomApparition, randomlist, EXPLO, textMort, profondeurJ, obtstacleType, obstacles, obstaclesPos,obstaclePos, nbrBandeVisible, posBandeX, posBandeY, bandesPos, bandePos
    apparitionBandes()
    randomApparition = random.choice(randomlist)

    if pygame.time.get_ticks() - taxiSpawn >= randomApparition :
        apparitionObstacles()
        taxiSpawn = pygame.time.get_ticks ( )
        print (randomApparition , "blabkla")
    if pygame.time.get_ticks ( ) - moving >= 25:
        for t in range(len(taxisPos)):
            if taxisPos[t] != (-500, -500):
                taxisPos[t] = (taxisPos[t][0] + speedTaxi, taxisPos[t][1])
        for bu in range(len(bussPos)):
            if bussPos[bu] != (0, -400):
                bussPos[bu] = (bussPos[bu][0] + speedBus, bussPos[bu][1])
                ############################################TRAVAIL SUR LES IA#############################################
            # Travail sur les taxi qui ralentissent a la rencontre d un bus plus lent
        for y in range (len (taxisPos)):
            for x in range (len(bussPos)):
                if pygame.time.get_ticks ( ) - moving >= 25:
                    if bussPos[x] != (0, -400) and taxisPos[y] != (-500, -500) : #verification place bus
                        if abs(int(taxisPos[y][0] - bussPos[x][0])) <= busLargeur and taxisPos[y][1] - bussPos[x][1] == 0:
                            taxisPos[y] = (taxisPos[y][0] + speedBus, taxisPos[y][1])
                            print('collision taxi bus')
                ###########################################################################################################
    for x in range (len(taxisPos)):
            if 0 <= int(posPlayerX)- int(taxisPos[x][0]) <= taxiLargeur and abs(int(posPlayerY)- int(taxisPos[x][1])) <= 0 and (profondeurJ == 0 or profondeurJ == 1)  :  # collision obstacle joueur
                posPlayerY = -600
                posPlayerX = -600
                dead = True
                textMort = 'Un taxi vous a écrasé !'
    for y in range (len(bussPos)):
            if 0 <= int (posPlayerX) - int (bussPos[y][0]) <= busLargeur and abs (int (posPlayerY) - int (bussPos[y][1])) == 0 and (profondeurJ == 2 or profondeurJ == 1) :
                posPlayerY = -600
                posPlayerX = -600
                dead = True
                textMort = 'Un bus vous a écrasé !'
    for b in range(nbrBandeVisible*2): #pour fr avancer les 2 bandes
        bandesPos[b] = (bandesPos[b][0] + speedBande, bandesPos[b][1])
    for b in range(nbrBandeVisible*2):
        if bandesPos[b][0] <= -100 : #pour fr revenir les bandes
            bandesPos[b] = (1335, bandesPos[b][1])
    randomApparition = random.choice (randomlist)
    pygame.display.update()

def dessiner():
    global taxiPos, taxisPos, intro, taxi, taxiSpawn, dessinage, player1, player, tick, bus, GLISSER, SAUTER, nbrBandeVisible, bandePos, bandesPos, posBandeY, DIFFIC
    intro = False
    gameDisplay.blit (background, (0, 0))
    if GLISSER:
        gameDisplay.blit (glisse, (posPlayerX, posPlayerY))
    if SAUTER:
        gameDisplay.blit (saute, (posPlayerX, posPlayerY))
    if not GLISSER and not SAUTER:
        if 0 <= pygame.time.get_ticks () - dessinage <= 500:
            gameDisplay.blit (player1, (posPlayerX, posPlayerY))
        elif 500 <= pygame.time.get_ticks( ) - dessinage <= 1000:
            gameDisplay.blit (player, (posPlayerX, posPlayerY))
        else :
            dessinage = pygame.time.get_ticks()
    for bu in range (len (bussPos)):
        if bussPos[bu] != (0, -400):
            gameDisplay.blit (bus, bussPos[bu])
        if bussPos[bu][0] < -busLargeur:
            bussPos[bu] = (0, -400)
    for t in range(len(taxisPos)):
        if taxisPos[t] != (-500, -500):
            gameDisplay.blit (taxi, taxisPos[t])
        if taxisPos[t][0] < -taxiLargeur:
            taxisPos[t] = (-500, -500)

    for b in range (nbrBandeVisible*2):
        gameDisplay.blit(bande, bandesPos[b])
    pygame.display.update ()
    pygame.display.flip()


def controleclavier():
    global positionPlayer, posPlayerX, posPlayerY, profondeurJ, mouvement, GLISSER, SAUTER, PAUSE
    if pygame.time.get_ticks() - mouvement >= 1500 and (profondeurJ == 0 or profondeurJ == 2):
                profondeurJ = 1
                GLISSER = False
                SAUTER = False
    for event in pygame.event.get ( ):
        if event.type == pygame.QUIT:
            pygame.quit ( )
            quit ( )
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                PAUSE = True
                paused()
        if event.type == pygame.KEYDOWN: # pr touche pressée
            if event.key == pygame.K_a and not GLISSER and not SAUTER:
                profondeurJ = 0
                GLISSER = True

                mouvement = pygame.time.get_ticks ( )
            if event.key == pygame.K_SPACE and not GLISSER and not SAUTER:
                profondeurJ = 2
                SAUTER = True

                mouvement = pygame.time.get_ticks ( )
            if event.key == pygame.K_DOWN and posPlayerY < 450:
                posPlayerY += 200
            if event.key == pygame.K_UP and posPlayerY > 50:  # pour pas qu'il sorte du cadre
                posPlayerY -= 200


        pygame.display.update ( )


def gameloop():
    global gameDisplay, dead, DIFFIC, PAUSE
    displayLargeur = 1300
    displayHauteur = 700
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    intro = False
    dead = False
    PAUSE = False


    while not intro:
        deadFenetre()
        clock.tick (70)
        controleclavier ( )
        DynamiqueduJeu ( )
        dessiner ( )
        print(taxisPos)
        pygame.display.update()
        pygame.display.flip()


gameintro ( )
gameloop ( )
