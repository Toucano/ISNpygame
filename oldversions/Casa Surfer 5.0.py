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
GREY_Alpha = (120, 120, 120, 150)
WHITE = (255, 255, 255)
B_GREEN = (0, 255, 0)
B_RED = (255, 0, 0)
# Load les images
mortFenetre = pygame.image.load ('./img/mort.png').convert_alpha ( )

taxi_sprite = pygame.image.load ('./img/obstacle.png')
background = pygame.image.load ('./img/background.png')
introback = pygame.image.load ('./img/introback.jpg')
player = pygame.image.load ('./img/player.png')
#player6= pygame.transform.scale(player, (200,200))
player1 = pygame.image.load ('./img/player1.png')
#player1 = pygame.transform.scale(player1, (200,200))
player2 = pygame.image.load ('./img/player2.png')
#player2 = pygame.transform.scale(player2, (200,200))
player3 = pygame.image.load ('./img/player3.png')
#player3 = pygame.transform.scale(player3, (200,200))
player4 = pygame.image.load ('./img/player4.png')
#player4 = pygame.transform.scale(player4, (200,200))
player5 = pygame.image.load ('./img/player5.png')
#player5 = pygame.transform.scale(player5, (200,200))
player6 = pygame.image.load ('./img/player6.png')
#player6 = pygame.transform.scale(player6, (200,200))
mort = pygame.image.load ('./img/mort.png')
mort = pygame.transform.scale(mort, (700,500))
bus_sprite = pygame.image.load('./img/bus.png')
explosion = pygame.image.load('./img/explosion.gif')
glisse = pygame.image.load('./img/glisse.png')
saute = pygame.image.load('./img/saute.png')
bande = pygame.image.load('./img/bande.png')
coin_sprite = pygame.image.load('./img/coin.png')
palmier_sprite_Up = pygame.image.load('./img/arbre.png')
arbre_sprite_Up = pygame.image.load('./img/arbre1.png')
gameMusic = pygame.mixer.Sound ('./music/ambienceGame.ogg')
palmier_sprite_Down = pygame.transform.rotate(palmier_sprite_Up,180)
arbre_sprite_Down = pygame.transform.rotate(arbre_sprite_Up,180)
arial20 = pygame.font.SysFont("arial", 20)
# position inital des objets
posPlayerY = 250
posPlayerX = 20
positionPlayer = [posPlayerX, posPlayerY]
variableInutile = 0
playerLargeur = 100
playerHauteur = 200
taxiLargeur = 200
taxiHauteur = 200
busLargeur = 260
busHauteur = 200
coinLargeur = 200
coinHauteur = 200
couloir = [(1400, 450), (1400, 250), (1400, 50)] # 1400 pour qu'on ne les voit âs apparaitre
Money = 0
taxiPos = []
busPos = []
Position = (0,0)
obstacles = []
palmierLargeur = 50
palmierHauteur = 50
arbreLargeur = 50
arbreHauteur = 50
speedTaxi = -18
speedBus = -8
speedPlayer = 8
taxi = ["taxi", (taxiLargeur, taxiHauteur), speedTaxi]
bus = ["bus", (busLargeur, busHauteur), speedBus]
coin = ["coin", (coinLargeur, coinHauteur), -6]
palmier = ["palmier", (palmierLargeur,palmierHauteur), -6]
arbre = ["arbre", (arbreLargeur,arbreHauteur), -6]
obstaclePos = (0,0) #0 juste pr avoir une valeur de base
coins = []
typeObstacle = [bus,taxi]
typeDeco = [palmier,arbre]
profondeurJ = 1
nbrBandeVisible = 11
nbrObstacleVisible = 5
nbrCoinVisible = 7
nbrDecoVisible = 30
posBandeY = [245,450]
posBackY = [(1400,0),(1400,610)]
bandePos = (0,0)
bandesPos = []
Back = []
score = 0
toDelete = []
tempsApparition = 3333
acceleration = 1
distanceSecu = 5
# Reperes temporels
moving = 0
speedBande = -3
obstacleSpawn = 0
dessinage = 0
mouvement = 0
decospawn = 0
obstacleReuse = 0
coinspawn = 0
randomlist = [3000,3500,4000,4500,5000,5500,6000] # nb de secondes entre 2 apparitions
# Les différents etats du jeu
RUNNER = False
intro = True
dead = False
EXPLO = False
GLISSER = False
SAUTER = False
DIFFIC = False
PAUSE = False
STPSPWNOB = False
STPSPWNBANDE = False
STPSPWNCOIN = False
STPSPWNBACK = False
# Fichier meilleurs scores


def quitgame():
    global RUNNER,dead, intro, DIFFIC
    RUNNER = False
    intro = False
    dead = False
    DIFFIC = False
    pygame.quit ( )
    quit ( )

def initialisation() : #vider les listes + coordonnées initiales
    global STPSPWNBACK,score,toDelete,RUNNER,dead ,intro,DIFFIC, obstacles,tempsApparition,Money,acceleration, posPlayerX, posPlayerY, obstaclesPos, obstacles, profondeurJ, obstacles, SAUTER, GLISSER, STPSPWNOB, STPSPWNBANDE, STPSPWNCOIN, coins, bandesPos
    obstaclesPos = []
    obstacles = []
    bandesPos = []
    coins = []
    toDelete = []
    tempsApparition = 3333
    Money = 0
    acceleration = 1
    SAUTER = False
    GLISSER = False
    STPSPWNOB = False
    STPSPWNBANDE = False
    STPSPWNCOIN = False
    STPSPWNBACK = False
    score = 0
    profondeurJ = 1
    posPlayerX = 20
    posPlayerY = 250

def restart():
    global intro, DIFFIC, RUNNER,dead, PAUSE
    intro = False
    DIFFIC = False
    RUNNER = True
    dead = False
    PAUSE = False
    initialisation()


def apparitionBandes():
    global nbrBandeVisible, bandePos, bandesPos, posBandeY , STPSPWNBANDE
    if not STPSPWNBANDE:
        for w in range(nbrBandeVisible):
            bandePos = (15 + (130*w),posBandeY[0])
            bandesPos.append(bandePos)
        for w in range(nbrBandeVisible):
            bandePos = (15 + (130*w),posBandeY[1])
            bandesPos.append(bandePos)

def apparitionBack():
    global Back, BackPos, STPSPWNBACK
    BackPos = random.choice(posBackY)
    if not STPSPWNBACK:
        if randint(0, 1) == 0 :
            Back.append([palmier, BackPos])
        else:
            Back.append([arbre, BackPos])
def apparitionCoin():
    global coin, coinHauteur,coinLargeur, obstacles, COIN, coins, STPSPWNCOIN, couloir
    if not STPSPWNCOIN:
            for y in range(len(obstacles)):
                if obstacles[y][1]== couloir[0]:
                    coins.append ([coin, (couloir[1])])
                    coins.append ([coin, (couloir[2])])
                if obstacles[y][1]== couloir[1]:
                    coins.append ([coin, (couloir[0])])
                    coins.append ([coin, ( couloir[2])])
                if obstacles[y][1]== couloir[2]:
                    coins.append ([coin, (couloir[1])])
                    coins.append ([coin, (couloir[0])])

def apparitionObstacles():
    global obstacles, taxiPos, busPos, obstacles, obstaclesPos, obtstacleType, obstaclePos, Position, STPSPWNOB
    Position = random.choice(couloir)
    #randint(0, 1) # 0 = taxi et 1 = bus
    if not STPSPWNOB:
        if randint(0, 2) == 0 or 1:
            obstacles.append([taxi, Position])
        elif randint(0, 2) == 2:
            obstacles.append([bus, Position])


def unpause():
    global PAUSE
    global dead
    PAUSE = False
    dead = False
    RUNNER = True

def buttonintro():
    global intro, RUNNER, dead, DIFFIC, PAUSE
    intro = True
    RUNNER = False
    dead = False
    DIFFIC = False
    PAUSE = False

def paused():
    global buttonintro, RUNNER, PAUSE, intro
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
                PAUSE = False
                RUNNER = True

        button ("Continue", 400, 450, 100, 50, GREY, B_GREEN, unpause)
        button ("Quit", 550, 450, 100, 50, GREY, BROWN, buttonintro)
        button ("Restart", 700, 450, 100, 50, GREY, B_GREEN, restart)

        pygame.display.update()
        clock.tick (15)


#def suppr_list(list , element):
 #   list.remove(element)


def text_objects(text, font, color):
    textSurface = font.render (text, True, color)
    return textSurface, textSurface.get_rect()


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
    global dead, textMort,intro, RUNNER

    gameDisplay.blit (mort, ((1300-700)/2, (700-500)/2))
    largeText = pygame.font.SysFont ("arial", 70)
    TextSurf, TextRect = text_objects (textMort, largeText,WHITE)
    TextRect.center = ((((1300-700)/2))+350, ((700-500)/2)+150)
    gameDisplay.blit (TextSurf, TextRect)
    for event in pygame.event.get ( ):
        if event.type == pygame.QUIT:
            pygame.quit ( )
            quit ( )
    button ("Quitter", 400, 450, 180, 50, RED, B_RED, buttonintro)
    button ("Recommencer", 700, 450, 180, 50, GREEN, B_GREEN, restart)

    pygame.display.update ( )

def difficulteFenetre() :
    global DIFFIC, gameDisplay, displayLargeur, displayHauteur, intro, dead, DIFFIC
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    gameDisplay.fill (WHITE)
    for event in pygame.event.get ( ):
        if event.type == pygame.QUIT:
            pygame.quit ( )
            quit ( )
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit ( )
                quit ( )
    button ("Quitter", 550, 500, 200, 50, GREY, B_RED, quitgame)
    button ("Retour", 550, 450, 100, 50, GREY, BROWN, buttonintro)

def gameintro():
    global gameDisplay,gameMusic, displayLargeur, displayHauteur, intro, dead, DIFFIC, RUNNER, PAUSE
    displayLargeur = 1024
    displayHauteur = 768
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    if not pygame.mixer.get_busy() == True :
        pygame.mixer.Sound.play(gameMusic)
    for event in pygame.event.get ( ):
        if event.type == pygame.QUIT:
            quitgame()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                quitgame()
    gameDisplay.blit (introback, (0, 0))
    largeText = pygame.font.SysFont ("comic sans ms", 105)
    TextSurf, TextRect = text_objects ("Casa Surfer", largeText, B_GREEN)
    TextRect.center = ((displayLargeur / 2), (displayHauteur / 12))
    gameDisplay.blit (TextSurf, TextRect)
    button ("Jouer", 250, 200, 200, 50, GREY, B_GREEN, restart)
    button ("Option", 550, 200, 200, 50, GREY, B_RED,quitgame)
    button ("Description", 250, 350, 200, 50, GREY, B_GREEN, restart)
    button ("Apparence", 550, 350, 200, 50, GREY, B_RED, quitgame)
    button ("Meilleur Score", 250, 500, 200, 50, GREY, B_GREEN, restart)
    button ("Quitter", 550, 500, 200, 50, GREY, B_RED, quitgame)

    pygame.display.update ( )
    clock.tick (15)

def DynamiqueduJeu():
    global taxiPos, score, Money,RUNNER,speedPlayer, coinspawn,speedBus,distanceSecu, speedTaxi,acceleration, STPSPWNBACK, toDelete,tempsApparition,variableInutile, obstacleReuse,decospawn,typeDeco, posBackY, moving, STPSPWNBANDE, STPSPWNCOIN, nbrObstacleVisible,typeObstacle, STPSPWNOB, speedTaxi, speedBande, speedBus, obstacleSpawn, dead, positionPlayer, playerHauteur, playerLargeur, posPlayerY, posPlayerX, gradualApparition, randomlist, EXPLO, textMort, profondeurJ, obtstacleType, obstacles, obstaclesPos,obstaclePos, nbrBandeVisible, posBandeX, posBandeY, bandesPos, bandePos
    apparitionBandes()
    #if pygame.time.get_ticks() - coinspawn >= 1000:
     #   apparitionCoin()
      #  coinspawn = pygame.time.get_ticks()
    if pygame.time.get_ticks() - decospawn >= 500:
        apparitionBack()
        decospawn = pygame.time.get_ticks()
    if pygame.time.get_ticks() - obstacleSpawn >= 3333 :
        apparitionObstacles()
        apparitionCoin ( )
        obstacleSpawn = pygame.time.get_ticks ( )
    if len(Back) >= nbrDecoVisible:
        STPSPWNBACK = True
    if len(obstacles) >= nbrObstacleVisible :
        STPSPWNOB = True
    if len(bandesPos) >= nbrBandeVisible :
        STPSPWNBANDE = True
    if len(coins) >= nbrCoinVisible :
        STPSPWNCOIN = True
    for t in range(len(obstacles)):
        if obstacles[t][0][0] == "taxi" or obstacles[t][0][0] == "bus" :
            obstacles[t][1] = [obstacles[t][1][0] + obstacles[t][0][2]*acceleration, obstacles[t][1][1]]
                ############################################TRAVAIL SUR LES IA#############################################
            # Travail sur les taxi qui ralentissent a la rencontre d un bus plus lent
    for x in range(len(obstacles)):
        for y in range(len(obstacles)):
                if obstacles[x][1][1] - obstacles[y][1][1] == 0 and abs (int (obstacles[x][1][0]) - int (obstacles[y][1][0])) <= obstacles[y][0][1][1] + (distanceSecu +10) and obstacles[x][0][0] == "taxi" and obstacles[y][0][0] == "bus":
                    obstacles[x] = [[obstacles[x][0][0], obstacles[x][0][1], obstacles[y][0][2]], obstacles[x][1]]
                elif obstacles[x][1][1] - obstacles[y][1][1] == 0 and abs (int (obstacles[x][1][0]) - int (obstacles[y][1][0])) <= obstacles[x][0][1][1] + distanceSecu and obstacles[x][0][0] == "taxi" and obstacles[y][0][0] == "taxi":
                    obstacles[y] = [[obstacles[y][0][0], obstacles[y][0][1], obstacles[x][0][2]], obstacles[x][1]]
                ##########################################################################################################

    for x in range (len(obstacles)):
            if obstacles[x][0][0] == "taxi" and -50 <= int(obstacles[x][1][0])- int(posPlayerX) <= obstacles[x][0][1][0] - 70 and abs(int(posPlayerY)- int(obstacles[x][1][1])) == 0 and (profondeurJ == 0 or profondeurJ == 1):  # collision obstacle joueur
                #posPlayerY = -600
                #posPlayerX = -600
                dead = True
                RUNNER = False
                textMort = 'Un taxi vous a écrasé !'
    for y in range (len(obstacles)):
            if obstacles[y][0][0] == "bus" and -50 <= int(obstacles[y][1][0]) - int(posPlayerX) <= obstacles[y][0][1][0] - 90 and abs (int (posPlayerY) - int (obstacles[y][1][1])) == 0 and (profondeurJ == 2 or profondeurJ == 1):
                #posPlayerY = -600
                #posPlayerX = -600
                dead = True
                RUNNER = False
                textMort = 'Un bus vous a écrasé !'
    for y in range (len(coins)):
            if coins[y][0][0] == "coin" and -50 <= int(coins[y][1][0])- int(posPlayerX) <= playerLargeur and abs (int (posPlayerY) - int (coins[y][1][1])) == 0 and (profondeurJ == 0 or profondeurJ == 1):
                Money += 1
                coins[y][1] = random.choice(couloir)
    for c in range (len(coins)):
        if coins[c][1][0] != -(coins[c][0][1][0]) :
            coins[c][1] = [coins[c][1][0] + coins[c][0][2], coins[c][1][1]]
    for c in range (len(coins)) :
        if coins[c][1][0] <= -(coins[c][0][1][0]) :
            coins[c][1] = random.choice(couloir)
    for b in range(nbrBandeVisible*2): #pour fr avancer les 2 bandes
        bandesPos[b] = (bandesPos[b][0] + speedBande, bandesPos[b][1])
    for b in range(nbrBandeVisible*2):
        if bandesPos[b][0] <= -100 : #pour fr revenir les bandes
            score += 5/2
            bandesPos[b] = (1335, bandesPos[b][1])
    #############################################Reutilisation##########################################
    for x in range (len (obstacles)):
        if obstacles[x][1][0] <= -(obstacles[x][0][1][0]) and pygame.time.get_ticks ( ) - obstacleReuse >= tempsApparition :
            if 0 <= randint(0, 2) <= 1 :
                obstacles[x] = [taxi, random.choice(couloir)]
                apparitionCoin ( )
            elif randint(0, 2) == 1 :
                obstacles[x] = [bus, random.choice (couloir)]
                apparitionCoin ( )
            obstacleReuse = pygame.time.get_ticks()
    ###################################################################################################
    for x in range(len(Back)):
        Back[x][1] = [Back[x][1][0] + Back[x][0][2], Back[x][1][1]]
    for x in range(len(Back)):
        if Back[x][1][0] <= -(Back[x][0][1][0]):
            Back[x] = [random.choice (typeDeco), random.choice (posBackY)]
    #############################ANTIBUG##################################################
    #for x in range (len (obstacles)):
     #   for y in range (len (obstacles)):
      #      print(obstacles[x] == obstacles[y])
       #     if obstacl0es[x][1][0] >= 1300:
        #        if obstacles[x][1][1] - obstacles[y][1][1] == 0 and int (obstacles[x][1][0]) - int (obstacles[y][1][0]) <= (obstacles[x][0][1][1] - 40): #and ((obstacles[x][0][0] == "taxi" and obstacles[y][0][0] == "bus") or(obstacles[x][0][0] == "bus" and obstacles[y][0][0] == "bus") or (obstacles[x][0][0] == "bus" and obstacles[y][0][0] == "taxi") or (obstacles[x][0][0] == "taxi" and obstacles[y][0][0] == "taxi")):
         #           obstacles[x] = [random.choice (typeObstacle), random.choice (couloir)]
    #############################ANTIBUG##################################################
    #############################ACCELERATION#############################################
    if score % 25 == 0 and variableInutile == 0:
        tempsApparition *= 0.8
        #for x in range(len(obstacles)):
        acceleration += 0.1
        variableInutile = 1
        distanceSecu += 10
        speedPlayer += 2
    if score % 25 != 0:
        variableInutile = 0
    ####################################BLOCAGE ACCELERATION SINON JEU TROP DUR#################################################
    if tempsApparition <= 800 :
        tempsApparition = 800


def dessiner():
    global taxiPos, obstacles, intro, taxi, obstacleSpawn,typeObstacle,coins, dessinage,taxi_sprite,bus_sprite, player1, player, tick, bus, GLISSER, SAUTER, nbrBandeVisible, bandePos, bandesPos, posBandeY, DIFFIC
    gameDisplay.blit (background, (0, 0))
    if GLISSER:
        gameDisplay.blit (glisse, (posPlayerX, posPlayerY))
    if SAUTER:
        gameDisplay.blit (saute, (posPlayerX, posPlayerY))
    if not GLISSER and not SAUTER and not dead:
        if 0 <= pygame.time.get_ticks () - dessinage <= 142:
            gameDisplay.blit (player, (posPlayerX, posPlayerY))
        elif 142 <= pygame.time.get_ticks ( ) - dessinage <= 284:
            gameDisplay.blit (player1, (posPlayerX, posPlayerY))
        elif 284 <= pygame.time.get_ticks ( ) - dessinage <= 426:
            gameDisplay.blit (player2, (posPlayerX, posPlayerY))
        elif 426 <= pygame.time.get_ticks ( ) - dessinage <= 568:
            gameDisplay.blit (player3, (posPlayerX, posPlayerY))
        elif 568 <= pygame.time.get_ticks ( ) - dessinage <= 710:
            gameDisplay.blit (player4, (posPlayerX, posPlayerY))
        elif 710 <= pygame.time.get_ticks ( ) - dessinage <= 852:
            gameDisplay.blit (player5, (posPlayerX, posPlayerY))
        elif 852 <= pygame.time.get_ticks ( ) - dessinage <= 1000:
            gameDisplay.blit (player6, (posPlayerX, posPlayerY))
        else :
            dessinage = pygame.time.get_ticks()
    if dead:
        gameDisplay.blit (glisse, (posPlayerX, posPlayerY))
        #if 0 <= pygame.time.get_ticks ( ) - dessinage <= 142:
            #gameDisplay.blit (player, (posPlayerX, posPlayerY))
    for x in range (len(obstacles)):
        if obstacles[x][0][0] == "taxi" :
            gameDisplay.blit (taxi_sprite, (obstacles[x][1]))
        if obstacles[x][0][0] == "bus" :
            gameDisplay.blit (bus_sprite, (obstacles[x][1]))
    for x in range (len(coins)):
        if coins[x][0][0] == "coin" :
            gameDisplay.blit (coin_sprite, coins[x][1])
    for b in range (nbrBandeVisible*2):
        gameDisplay.blit(bande, bandesPos[b])
    for x in range (len(Back)):
        if Back[x][0][0] == "palmier" and Back[x][1][1] == 0:
            gameDisplay.blit(palmier_sprite_Up, Back[x][1])
        if Back[x][0][0] == "palmier" and Back[x][1][1] == 610:
            gameDisplay.blit(palmier_sprite_Down, Back[x][1])
        if Back[x][0][0] == "arbre" and Back[x][1][1] == 0:
            gameDisplay.blit (arbre_sprite_Up, Back[x][1])
        if Back[x][0][0] == "arbre" and Back[x][1][1] == 610:
            gameDisplay.blit (arbre_sprite_Down, Back[x][1])
##########################DEBUGAGE COLLISION ENLEVER LES HASHTAGS############################
    #for x in range(len(obstacles)):
     #   pygame.draw.rect (gameDisplay, BLUE, (obstacles[x][1], obstacles[x][0][1]), 5)
    #for x in range(len(coins)):
     #   pygame.draw.rect (gameDisplay, GREEN, (coins[x][1], coins[x][0][1]), 5)
    #pygame.draw.rect(gameDisplay,BLUE,(posPlayerX,posPlayerY,200,200),5)
#############################################################################################
    pygame.draw.rect (gameDisplay, GREY_Alpha, (0, 645, 250, 100))
    largeText = pygame.font.SysFont ("arial", 20)
    TextSurf, TextRect = text_objects (("Distances :" + " " + str (int (score))) + " m", largeText,BLACK)
    TextRect.center = (125, 675)
    gameDisplay.blit (TextSurf, TextRect)
    pygame.draw.rect (gameDisplay, BLACK, (0, 0, 250, 53))
    largeText = pygame.font.SysFont ("arial", 20)
    TextSurf, TextRect = text_objects ((str (int (Money))), largeText,WHITE)
    TextRect.center = (100, 25)
    gameDisplay.blit (TextSurf, TextRect)
    gameDisplay.blit (coin_sprite, (50,-75))


def controleclavier():
    global positionPlayer, posPlayerX, posPlayerY, profondeurJ, mouvement, GLISSER, SAUTER, PAUSE, presseRight, speedPlayer, touchePresse, RUNNER
    touchePresse = pygame.key.get_pressed()
    if touchePresse[pygame.K_RIGHT] and posPlayerX <= 700:
        posPlayerX += speedPlayer
    if touchePresse[pygame.K_LEFT] and posPlayerX >= 20:
        posPlayerX -= speedPlayer
    if pygame.time.get_ticks() - mouvement >= 1500 and (profondeurJ == 0 or profondeurJ == 2):
                profondeurJ = 1
                GLISSER = False
                SAUTER = False
    for event in pygame.event.get ( ):
        if event.type == pygame.QUIT:
            pygame.quit ( )
            quit ( )
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE and PAUSE == False:
                PAUSE = True
                RUNNER = False
                paused()
            if event.key == pygame.K_ESCAPE and PAUSE == True:
                PAUSE = False
                RUNNER = True
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
            if event.key == pygame.K_f :
                # pygame.display.toggle_fullscreen()
                pygame.display.set_mode (pygame.display.list_modes ( )[0], pygame.FULLSCREEN)

def runner():
    global gameDisplay, dead, DIFFIC, PAUSE, intro, displayLargeur,displayHauteur
    displayLargeur = 1300
    displayHauteur = 700
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    clock.tick(70)
    controleclavier ()
    DynamiqueduJeu ()
    dessiner ()
    pygame.display.update()
    pygame.display.flip()

def gameloop():
    global runner, intro, dead, PAUSE, displayHauteur, displayLargeur
    while intro:
        gameintro ()
        print('intro')
    while RUNNER:
        runner ()
        print('runner')
    while dead:
        deadFenetre()
        print('dead')
    while PAUSE :
        paused()
        print('pause')

gameloop()
quitgame()