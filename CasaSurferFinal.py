# coding=utf-8
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
pygame.display.set_caption ('Casa circuit') #titre
icon = pygame.image.load ('./img/icon/icon.png')
pygame.display.set_icon(icon)
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
GOLD_color = (255,215,0)

# Load les images
mortFenetre = pygame.image.load ('./img/background/mort.png').convert_alpha ( )
taxi_sprite = pygame.image.load ('./img/obstacle_sprite/obstacle.png')
background = pygame.image.load ('./img/background/background.png')
introback = pygame.image.load ('./img/background/introback.jpg')
moulhanout = pygame.image.load ('./img/background/moulhanout.jpg')
moulhanout = pygame.transform.scale(moulhanout,(700,700))
########## SKIN DEFAULT ##################
player_default = pygame.image.load ('./img/skin/default/player.png')
player1_default = pygame.image.load ('./img/skin/default/player1.png')
# player1 = pygame.transform.scale(player1, (200,200))
player2_default = pygame.image.load ('./img/skin/default/player2.png')
# player2 = pygame.transform.scale(player2, (200,200))
player3_default = pygame.image.load ('./img/skin/default/player3.png')
# player3 = pygame.transform.scale(player3, (200,200))
player4_default = pygame.image.load ('./img/skin/default/player4.png')
# player4 = pygame.transform.scale(player4, (200,200))
player5_default = pygame.image.load ('./img/skin/default/player5.png')
# player5 = pygame.transform.scale(player5, (200,200))
player6_default = pygame.image.load ('./img/skin/default/player6.png')
# player6 = pygame.transform.scale(player6, (200,200))
glisse_default = pygame.image.load ('./img/skin/default/glisse.png')
saute_default = pygame.image.load ('./img/skin/default/saute.png')
########## SKIN ALLRED#######
player_allred = pygame.image.load ('./img/skin/allred/player.png')
player1_allred = pygame.image.load ('./img/skin/allred/player1.png')
player2_allred = pygame.image.load ('./img/skin/allred/player2.png')
player3_allred = pygame.image.load ('./img/skin/allred/player3.png')
player4_allred = pygame.image.load ('./img/skin/allred/player4.png')
player5_allred = pygame.image.load ('./img/skin/allred/player5.png')
player6_allred = pygame.image.load ('./img/skin/allred/player6.png')
glisse_allred = pygame.image.load ('./img/skin/allred/glisse.png')
saute_allred = pygame.image.load ('./img/skin/allred/saute.png')
########## SKIN ALLGREEN
player_allgreen = pygame.image.load ('./img/skin/allgreen/player.png')
player1_allgreen = pygame.image.load ('./img/skin/allgreen/player1.png')
player2_allgreen = pygame.image.load ('./img/skin/allgreen/player2.png')
player3_allgreen = pygame.image.load ('./img/skin/allgreen/player3.png')
player4_allgreen = pygame.image.load ('./img/skin/allgreen/player4.png')
player5_allgreen = pygame.image.load ('./img/skin/allgreen/player5.png')
player6_allgreen = pygame.image.load ('./img/skin/allgreen/player6.png')
glisse_allgreen = pygame.image.load ('./img/skin/allgreen/glisse.png')
saute_allgreen = pygame.image.load ('./img/skin/allgreen/saute.png')
########## SKIN GOLD
player_gold = pygame.image.load ('./img/skin/gold/player.png')
player1_gold = pygame.image.load ('./img/skin/gold/player1.png')
player2_gold = pygame.image.load ('./img/skin/gold/player2.png')
player3_gold = pygame.image.load ('./img/skin/gold/player3.png')
player4_gold = pygame.image.load ('./img/skin/gold/player4.png')
player5_gold = pygame.image.load ('./img/skin/gold/player5.png')
player6_gold = pygame.image.load ('./img/skin/gold/player6.png')
glisse_gold = pygame.image.load ('./img/skin/gold/glisse.png')
saute_gold = pygame.image.load ('./img/skin/gold/saute.png')
#################################################################"
mort = pygame.image.load ('./img/background/mort.png')
mort = pygame.transform.scale (mort, (700, 500))
bus_sprite = pygame.image.load ('./img/obstacle_sprite/bus.png')
#explosion = pygame.image.load ('./img/explosion.gif') les gif ne marchent pas !!!
playerSprite = [player_default,player1_default,player2_default,player3_default,player4_default,player5_default,player6_default,saute_default,glisse_default]
bande = pygame.image.load ('./img/background/bande.png')
coin_sprite = pygame.image.load ('./img/bonus_sprite/coin.png')
shield_bonus = pygame.image.load ('./img/bonus_sprite/shield.png')
shield_sprite = pygame.image.load ('./img/bonus_sprite/spr_shield.png')
palmier_sprite_Up = pygame.image.load ('./img/background/arbre.png')
arbre_sprite_Up = pygame.image.load ('./img/background/arbre1.png')
moto103 = pygame.image.load ('./img/obstacle_sprite/103.png')
#########SOUNDS###############
coinSound = pygame.mixer.Sound ('./music/coinsound.ogg')
gameMusic = pygame.mixer.Sound ('./music/ambienceGame.ogg')
deathshot = pygame.mixer.Sound ('./music/deathshot.ogg')
deathfall = pygame.mixer.Sound ('./music/deathfall.ogg')
buyskin = pygame.mixer.Sound ('./music/buyskin.ogg')
rightFoot = pygame.mixer.Sound ('./music/rightFoot.ogg')
leftFoot = pygame.mixer.Sound ('./music/leftFoot.ogg')
jumpSound = pygame.mixer.Sound ('./music/jump.ogg')
changeCouloir = pygame.mixer.Sound ('./music/change.ogg')
ambianceRunner = pygame.mixer.Sound ('./music/ambianceville.ogg')
shieldON = pygame.mixer.Sound ('./music/powerUp.ogg')
shieldOFF = pygame.mixer.Sound ('./music/powerDown.ogg')
shieldcollision = pygame.mixer.Sound ('./music/shieldcollision.ogg')
klaxtaxi = pygame.mixer.Sound ('./music/klaxtaxi.ogg')
klaxbus = pygame.mixer.Sound ('./music/klaxbus.ogg')
klaxmoto = pygame.mixer.Sound ('./music/klaxmoto.ogg')
##############################
palmier_sprite_Down = pygame.transform.rotate (palmier_sprite_Up, 180)
arbre_sprite_Down = pygame.transform.rotate (arbre_sprite_Up, 180)
arial20 = pygame.font.SysFont ("arial", 20)
# position inital des objets
posPlayerY = 250
previousposPlayer = 250
posPlayerX = 20
positionPlayer = [posPlayerX, posPlayerY]
variableInutile = 0
playerLargeur = playerSprite[0].get_size()[0]
playerHauteur = playerSprite[0].get_size()[1]
taxiLargeur = taxi_sprite.get_size()[0]
taxiHauteur = taxi_sprite.get_size()[1]
busLargeur = bus_sprite.get_size()[0]
busHauteur = bus_sprite.get_size()[1]
coinLargeur = coin_sprite.get_size()[0]
coinHauteur = coin_sprite.get_size()[1]
shieldLargeur = shield_bonus.get_size()[0]
shieldHauteur = shield_bonus.get_size()[1]
textMort = ''
couloir = [(1400, 450), (1400, 250), (1400, 50)]  # 1400 pour qu'on ne les voit pas apparaitre
couloirmoto = [(1400, 50), (1400,250)]
Money = 0
taxiPos = []
busPos = []
Position = (0, 0)
obstacles = []
palmierLargeur = 50
palmierHauteur = 50
arbreLargeur = 50
arbreHauteur = 50
speedTaxi = -18
speedBus = -8
speedPlayer = 5
motoLargeur = moto103.get_size()[0]
motoHauteur = moto103.get_size()[1]
speedMoto = -20
taxi = ["taxi", (taxiLargeur, taxiHauteur), speedTaxi]
bus = ["bus", (busLargeur, busHauteur), speedBus]
moto = ["moto", (motoLargeur, motoHauteur), speedMoto]
coin = ["coin", (coinLargeur, coinHauteur), -6]
shield = ["shield",(shieldLargeur,shieldHauteur), -6]
palmier = ["palmier", (palmierLargeur, palmierHauteur), -6]
arbre = ["arbre", (arbreLargeur, arbreHauteur), -6]
obstaclePos = (0, 0)  # 0 juste pr avoir une valeur de base
coins = []
#differencier les types, choix aleatoire
typeObstacle = [bus, taxi, moto]
typeDeco = [palmier, arbre]
typeBonus = [coin, shield_bonus]
profondeurJ = 1
nbrBandeVisible = 11 #bandes qui tournent
nbrObstacleVisible = 7
nbrCoinVisible = 7
nbrDecoVisible = 30
posBandeY = [245, 450]  #[0;1]
posBackY = [(1400, 0), (1400, 610)]
bandePos = (0, 0)
bandesPos = []
Back = []
distance = 0
tempsApparition = 3333
acceleration = 1
distanceSecu = 25
variableInutile3 = 1
variableInutile4 = 1
variableInutile5 = 0
variableInutile6 = 0
variableInutile7 = 0
variableInutile8 = 0
variableInutile9 = 0
variableInutile10 = 0
variableInutile11 = 0
variableInutile12 = 0
####MENU OPTION####
poscurseurX = 100
poscurseurY = 100
soundboxX = 175
soundboxY = 162.5
Difficulty = 1
# Variable du mixer son
fadout = 500
soundloop = -1
# Reperes temporels
moving = 0
speedBande = -3
obstacleSpawn = 0
dessinage = 0
mouvement = 0
decospawn = 0
obstacleReuse = 0
repereanim = 0
coinspawn = 0
footsteps = 0
erreurtime = 0
chansontime = 0
chanson1time = 0
randomsound = 0
quiztimer = 0
randomlist = [3000, 3500, 4000, 4500, 5000, 5500, 6000]  # nb de secondes entre 2 apparitions
timeshield = 0
timeendshield = 0
timeannimation = 650
shieldduration = 5000
clignote = 0
####LE QUIZ#####
Question1 = ["Qui a nomme la ville Casablanca ?", ["Les Portugais", "Les Espagnols", "Les Francais","Les Marocains"],1]
Question2 = ["Casablanca est la capitale … du Maroc :", ["… administrative", "… économique", "… touristique","… les trois"],2]
Question3 = ["En quelle annee le film Casablanca est sorti ?", ["1934", "1938", "1942","1946"],3]
Question4 = ["La première femme arabe, musulmane et africaine a devenir… est casablancaise :", ["pilote", "medecin", "ingenieur","ministre"],1]
Question5 = ["Combien y’avait-il d’habitants a Casablanca au debut des annees 1900 ?", ["2 000", "20 000", "200 000","2 000 000"],2]
Question6 = ["Quelle est la hauteur du minaret de la Mosquee Hassan II ?", ["110 m", "140 m", "210 m","300 m"],3]
Question7 = ["Quand est-ce que l’inauguration de la Mosquee Hassan II a eu lieu ?", ["1986", "1993", "1997","1999"],2]
Question8 = ["Casablanca est aussi une marque de…", ["Motos", "Sodas", "Darboukas","Bieres"],4]
quizz = [Question1,Question2,Question3,Question4,Question5,Question6,Question7,Question8]
reponsechoisie = 0
questionposee = []
# Les differents etats du jeu
RUNNER = False
MUSIC = True
DESC = False
SKIN = False
intro = True
dead = False
EXPLO = False
GLISSER = False
SAUTER = False
OPTN = False
SCORE = False
PAUSE = False
STPSPWNOB = False
STPSPWNBANDE = False
STPSPWNCOIN = False
STPSPWNBACK = False
animationdown = False
animationup = False
ALLRED = False
ALLGREEN = False
GOLD = False
SHIELDED = False
ENDSHIELD = False
QUIZ = False
FIRSTDEATH = False

def ecriture(police,size,msg,color,x,y):
    largeText = pygame.font.SysFont (police, size)
    TextSurf, TextRect = text_objects (msg, largeText, color)
    TextRect.center = (x, y)
    gameDisplay.blit (TextSurf, TextRect)
    return gameDisplay.blit (TextSurf, TextRect)

def quitgame():
    global RUNNER, dead, intro, OPTN
    pygame.quit ( )      #pygame
    quit ( )             #python


def sauvegarde(money, distance, parametre):
    if money:
        open("./data/cash.txt")
    if distance:
        open('./data/highscore.txt')
    if parametre:
        open("./data/skin.txt")


def restart():  # vider les listes + coordonnees initiales
    global STPSPWNBACK, distance,variableInutile7,questionposee, toDelete,animationup,animationdown, RUNNER, intro, OPTN, obstacles,speedPlayer, tempsApparition, Money, acceleration, posPlayerX, posPlayerY, obstaclesPos, obstacles, profondeurJ, obstacles, SAUTER, GLISSER, STPSPWNOB, STPSPWNBANDE, STPSPWNCOIN, coins, bandesPos
    obstaclesPos = []
    obstacles = []
    bandesPos = []
    coins = []
    toDelete = []
    questionposee = []
    tempsApparition = 3333
    acceleration = 1
    variableInutile7 = 0
    SAUTER = False
    GLISSER = False
    STPSPWNOB = False
    STPSPWNBANDE = False
    STPSPWNCOIN = False
    STPSPWNBACK = False
    animationdown = False
    animationup = False
    distance = 0
    speedPlayer = 8
    profondeurJ = 1
    posPlayerX = 20
    posPlayerY = 250
    gameloop()     #relance apres reinitialisation


def apparitionBandes():
    global nbrBandeVisible, bandePos, bandesPos, posBandeY, STPSPWNBANDE
    if not STPSPWNBANDE:
        for w in range (nbrBandeVisible):
            bandePos = (15 + (130 * w), posBandeY[0]) #15 pr s'eloigner bordure, 100+30 pr eloigner bandes entre elles
            bandesPos.append (bandePos) #pr en avoir plusieure
        for w in range (nbrBandeVisible):
            bandePos = (15 + (130 * w), posBandeY[1])
            bandesPos.append (bandePos)


def apparitionBack():
    global Back, BackPos, STPSPWNBACK
    BackPos = random.choice (posBackY)      #coordonnees
    if not STPSPWNBACK:
        if randint (0, 1) == 0:
            Back.append ([palmier, BackPos])
        else:
            Back.append ([arbre, BackPos])


def apparitionCoin():
    global coin, coinHauteur, coinLargeur, obstacles, COIN, coins, STPSPWNCOIN, couloir, typeBonus, shield
    if not STPSPWNCOIN:
        randomNU = randint(0,5)
        if randomNU == 0 or randomNU == 1 or randomNU == 2 or randomNU == 3 or randomNU == 4 :
            bonus = coin
        if randomNU == 5 :
            bonus = shield
        randomNUM = randint (0, 5)
        if randomNUM == 0 or randomNUM == 1 or randomNUM == 2 or randomNUM == 3 or randomNUM == 4:
            bonus1 = coin
        if randomNUM == 5:
            bonus1 = shield
        bonuss = [bonus, bonus1]
        for y in range (len (obstacles)): #de gauche a droite
            if obstacles[y][1] == couloir[0]:
                coins.append ([random.choice(bonuss), (couloir[1])])
                coins.append ([random.choice(bonuss), (couloir[2])])
            if obstacles[y][1] == couloir[1]:
                coins.append ([random.choice(bonuss), (couloir[0])])
                coins.append ([random.choice(bonuss), (couloir[2])])
            if obstacles[y][1] == couloir[2]:
                coins.append ([random.choice(bonuss), (couloir[1])])
                coins.append ([random.choice(bonuss), (couloir[0])])
#2 pieces, 1 obstacle en mm temps

def apparitionObstacles():
    global obstacles, taxiPos, busPos, obstacles, obstaclesPos, obtstacleType, obstaclePos, Position, STPSPWNOB, Positionmoto, couloirmoto
    Position = random.choice (couloir)
    Positionmoto = random.choice (couloirmoto)
    # randint(0, 1) # 0 = taxi et 1 = bus
    if not STPSPWNOB:
        if randint (0, 4) == 0 or 1:
            obstacles.append ([moto, Positionmoto])
        elif randint (0, 4) == 2:
            obstacles.append ([bus, Position])
        elif randint (0, 4) == 3 or 4:
            obstacles.append ([taxi, Position])


def unpause():
    global PAUSE
    global dead
    PAUSE = False
    dead = False


def paused():
    gameDisplay.blit (mort, (300,100))
    ecriture ("arial", 115, "Pause !", GREY, 650, 250)
    while PAUSE:
        for event in pygame.event.get ( ): # verifie ts les mvmnts
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                unpause ( )

        button ("Continue", 400, 450, 100, 50, GREY, B_GREEN, unpause)
        button ("Quit", 550, 450, 100, 50, GREY, BROWN, gameintro)
        button ("Restart", 700, 450, 100, 50, GREY, B_GREEN, restart)

        pygame.display.update ( )
        clock.tick (15)


# def suppr_list(list , element):
#   list.remove(element)


def text_objects(text, font, color): #definir un texte qu'on ecrira avec ecriture()
    textSurface = font.render (text, True, color)
    return textSurface, textSurface.get_rect ( )


def button(msg, x, y, w, h, ic, ac, action=None): # message / x / y / largeur / hauteur / couleur / couleur(par dessus) / action
    mouse = pygame.mouse.get_pos ( ) # donne en sorti la position de la souris
    click = pygame.mouse.get_pressed ( ) # donne si on clique et sur quel clique (droit ou gauche)

    if x + w > mouse[0] > x and y + h > mouse[1] > y: # si en ordonnee(mouse[0]) la souris est dans le bouton et en abscisse[1]
        pygame.draw.rect (gameDisplay, ac, (x, y, w, h)) # dessiner le rectangle avec couleur (lorsque on est par dessus)
        if click[0] == 1 and action != None: # si on clique et qu'une action a ete definie
            action ( ) # faire l'action
    else: # Si la souris n'est pas sur le bouton
        pygame.draw.rect (gameDisplay, ic, (x, y, w, h))  # dessiner le rectangle avec couleur (par default)
    # Ecriture des caractere au sein du bouton
    smallText = pygame.font.SysFont ("arial", 30)
    textSurf, textRect = text_objects (msg, smallText, WHITE)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit (textSurf, textRect)

def quiz():
    global QUIZ, FIRSTDEATH, dead, variableInutile11,variableInutile7,STPSPWNOB,previousposPlayer, reponsechoisie, questionposee,profondeurJ,animationdown,animationup, timeshield,SHIELDED,posPlayerY,posPlayerX,obstacles
    while QUIZ and FIRSTDEATH:
        gameDisplay.fill(BLACK)
        if variableInutile11 == 0:
            questionposee = random.choice(quizz)
            variableInutile11 = 1
        ecriture ("arial",40 , questionposee[0], WHITE, 650, 100)
        button (questionposee[1][0],400, 250, 200,100,GREY,GREEN,firstChoice)
        button (questionposee[1][1],700, 250, 200,100,GREY,GREEN,secondeChoice)
        button (questionposee[1][2],400, 400, 200,100,GREY,GREEN,thirdChoice)
        button (questionposee[1][3],700, 400, 200,100,GREY,GREEN,forthChoice)
        if reponsechoisie == questionposee[2]:
            FIRSTDEATH = False
            QUIZ = False
            posPlayerY = previousposPlayer
            obstacles = []
            STPSPWNOB = False
            profondeurJ = 1
            variableInutile7 = 0
            animationdown = False
            animationup = False
            gameloop()
        elif reponsechoisie != questionposee[2] and reponsechoisie != 0:
            FIRSTDEATH = False
            dead = True
            QUIZ = False
            deadFenetre()
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
        pygame.draw.rect(gameDisplay,GREY,(300,20,700,50))
        pygame.draw.rect(gameDisplay,RED,(300,20,(((pygame.time.get_ticks() - quiztimer)/10000)*-700)+700,50))
        ecriture("comic sans ms",30,str(int(-(pygame.time.get_ticks() - quiztimer)/1000)+10) + " sec",WHITE,650,45)
        if pygame.time.get_ticks() - quiztimer > 10000:
            FIRSTDEATH = False
            QUIZ = False
            dead = True
            deadFenetre()
        button ("Quitter", 550, 550, 200, 50, RED, B_RED, gameintro)
        pygame.display.update()
def firstChoice():
    global reponsechoisie
    reponsechoisie = 1

def secondeChoice():
    global reponsechoisie
    reponsechoisie = 2

def thirdChoice():
    global reponsechoisie
    reponsechoisie = 3

def forthChoice():
    global reponsechoisie
    reponsechoisie = 4

def deadFenetre(): #ce qui s'affiche qd on meurt
    global dead, textMort, variableInutile7, quiztimer, QUIZ, FIRSTDEATH
    if dead :
        gameDisplay.fill (BLACK)
        #ecriture("arial",70,textMort,WHITE,650,250)
    while dead:
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
        ###################MISE EN PLACE DU quizz####################
        if dead and variableInutile7 == 0 :
            FIRSTDEATH = True
            variableInutile7 = 1
        if FIRSTDEATH:
            QUIZ = True
            dead = False
            quiztimer = pygame.time.get_ticks()
            quiz()
        ecriture("arial",70,textMort,WHITE,650,250)
        ################################################################
        button ("Quitter", 400, 450, 180, 50, RED, B_RED, gameintro)
        button ("Recommencer", 700, 450, 180, 50, GREEN, B_GREEN, restart)

        pygame.display.update ( )


def optionbutton(): #
    global intro, OPTN
    intro = False
    OPTN = True
    optionFenetre()

def descriptionbutton():
    global intro, DESC
    intro = False
    DESC = True
    descriptionFenetre()

def skinbutton():
    global intro, SKIN
    intro = False
    SKIN = True
    skinFenetre()

def scorebutton():
    global intro, SCORE
    intro = False
    SCORE = True
    scoreFenetre()

def optionFenetre():
    global OPTN, gameDisplay, displayLargeur,Difficulty, displayHauteur, intro, dead, OPTN, poscurseurX,poscurseurY, soundboxX,soundboxY, soundboxH, soundboxW, MUSIC, Variableinutile2, couleurchangement
    OPTN = True
    displayHauteur = 500
    displayLargeur = 500
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    while OPTN and not intro and not DESC and not SKIN and not SCORE: #verification sinon chevauchements
        mouse = pygame.mouse.get_pos ( ) #coordonnees
        click = pygame.mouse.get_pressed ( ) #Bool #
        curseurW = 30
        curseurH = 30
        gameDisplay.fill (WHITE)
        initDifficulty ( )
        ecriture("arial", 25,"Option",BLACK,250,50)
        ecriture ("arial", 25, "Difficulte", BLACK, 50, 115)
        pygame.draw.rect(gameDisplay,GREY_Alpha,(100,100,300,30)) #grand rect
        pygame.draw.rect (gameDisplay, BROWN, (poscurseurX, poscurseurY, curseurW,curseurH)) #petit rect
        if poscurseurX + curseurW > mouse[0] > poscurseurX - curseurW and poscurseurY + curseurH > mouse[1] > poscurseurY - curseurH: #si la souris est dans petit rect
            pygame.draw.rect(gameDisplay,GREEN,(poscurseurX,poscurseurY,curseurW,curseurH)) #petit rect devient vert
            if click[0] == 1 and 100 < mouse[0] < 370 and 100 < mouse[1] < 130: #verifie si appuye et dans grand rect
                poscurseurX = mouse[0] #petit carre suit curseur
        if 100 <= poscurseurX < 190 :
            ecriture ("arial", 25, "Easy", BLACK, 450, 115)
            Difficulty = 1
        if 190 <= poscurseurX < 280 :
            ecriture ("arial", 25, "Normal", BLACK, 450, 115)
            Difficulty = 2
        if 280 <= poscurseurX < 370 :
            ecriture ("arial", 25, "Hard", BLACK, 450, 115)
            Difficulty = 3
        ecriture ("arial", 25, "Sons", BLACK, 35, 200)
        soundboxH = 75
        soundboxW = 150
        pygame.draw.rect(gameDisplay,GREY,(soundboxX,soundboxY,soundboxW,soundboxH))
        if soundboxX + soundboxW > mouse[0] > soundboxX and soundboxY + soundboxH > mouse[1] > soundboxY:
            pygame.draw.rect (gameDisplay, couleurchangement, (soundboxX, soundboxY, soundboxW, soundboxH))
        if MUSIC == True :
            couleurchangement = B_GREEN
            if not pygame.mixer.get_busy ( ) : #pas occupe
                pygame.mixer.Sound.play(gameMusic,-1,0, 500)
            pygame.draw.rect (gameDisplay, GREEN, (soundboxX + (soundboxW/2), soundboxY, soundboxW/2, soundboxH))
            ecriture ("arial", 40, "ON", BLACK, soundboxX + (soundboxW/4), soundboxY + (soundboxH/2))
            if click[0] == 1 and soundboxX + soundboxW > mouse[0] > soundboxX and soundboxY + soundboxH > mouse[1] > soundboxY and Variableinutile2 == 1:
                MUSIC = False
                Variableinutile2 = 0 #detecte superposition d'etat car si on reste clique ca va basculer indefinimenent entre les modes
        if MUSIC == False :
            couleurchangement = B_RED
            pygame.mixer.stop()
            pygame.draw.rect (gameDisplay, RED, (soundboxX , soundboxY, soundboxW/2, soundboxH))
            ecriture ("arial", 40, "OFF", BLACK, soundboxX + (soundboxW/4*3), soundboxY + (soundboxH/2))
            if click[0] == 1 and soundboxX + soundboxW > mouse[0] > soundboxX and soundboxY + soundboxH > mouse[1] > soundboxY and Variableinutile2 == 1:
                MUSIC = True
                Variableinutile2 = 0
        if click[0] == 0:
            Variableinutile2 = 1
        sett = open("./data/settings.txt","r+")
        sett.seek(0)
        sett.write(str(Difficulty))
        sett.seek(2)
        if MUSIC:
            sett.write("1\n")
        if not MUSIC:
            sett.write("0\n")
        sett.seek(4)
        sett.write("#")
        sett.close()
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit ( )
                    quit ( )
        button ("Quitter", 100, 350, 100, 50, GREY, B_RED, quitgame)
        button ("Retour", 300, 350, 100, 50, GREY, BROWN, gameintro)
        pygame.display.update()

def descriptionFenetre():
    global OPTN, gameDisplay, displayLargeur, displayHauteur, intro, dead, OPTN
    DESC = True
    displayHauteur = 500
    displayLargeur = 500
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    while DESC and not intro and not OPTN and not SKIN and not SCORE:
        gameDisplay.fill (BROWN)
        ecriture ("arial", 15, "Un personnage qui peut se deplacer sur 3 voies (flèches sur le clavier).", BLACK, 250, 100)
        ecriture("arial",15,"Il y a des obstacles qui arrivent (environnement casablancais), le personnage ",BLACK,250,130)
        ecriture("arial",15,"peut sauter (espace); S’il meurt, une question apparaît et le joueur devra ",BLACK,250,160)
        ecriture("arial",15,"y repondre justement dans un temps imparti pour continuer le niveau, sinon il perd ",BLACK,250,190)
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit ( )
                    quit ( )
        button ("Quitter", 100, 350, 100, 50, GREY, B_RED, quitgame)
        button ("Retour", 300, 350, 100, 50, GREY, BROWN, gameintro)
        pygame.display.update ( )


def skinFenetre():
    global OPTN, gameDisplay, displayLargeur, displayHauteur,variableInutile8,variableInutile9, variableInutile10, intro, dead,lignes,SKIN, dessinage, playerSprite, Money, ALLRED, erreurtime, ALLGREEN,GOLD
    SKIN = True
    displayHauteur = 700
    displayLargeur = 700
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    while SKIN and not intro and not OPTN and not DESC and not SCORE:
        mouse = pygame.mouse.get_pos ( )
        click = pygame.mouse.get_pressed ( )
        gameDisplay.blit (moulhanout,(0,0))
        ecriture ("arial", 25, "Choisissez votre skin ! " + " Vous avez : " + str(Money) + " Dihrams.", BLACK, 350, 50)
        if 50 < mouse[0] < 250 and 100 < mouse[1] < 300 :
            pygame.draw.rect (gameDisplay, RED, (50, 100, 200, 200))
            if click[0] == 1:
                if Money >= 45 and ALLRED == False:
                    Money -= 45
                    pygame.mixer.Sound.play(buyskin)
                    playerSprite = [player_allred,player1_allred,player2_allred,player3_allred,player4_allred,player5_allred,player6_allred,saute_allred,glisse_allred]
                    cash = open ("./data/cash.txt", "r+")
                    cash.seek(0)
                    cash.write(str(int(Money)))
                    cash.truncate()
                    cash.close()
                    ALLRED = True

                    if variableInutile10 == 0:
                        skin = open ("./data/skin.txt", "r+")
                        skin.seek (0)
                        if ALLRED and not GOLD and not ALLGREEN:
                            skin.truncate ( )
                            skin.writelines (["ALLRED", "\n", "\n", "\n#"])
                        if ALLRED and GOLD and ALLGREEN:
                            skin.truncate ( )
                            skin.writelines (["ALLRED\n", "ALLGREEN", "\nGOLD", "\n#"])
                        if ALLRED and GOLD and not ALLGREEN:
                            skin.truncate ( )
                            skin.writelines (["ALLRED\n", "\n", "\nGOLD", "\n#"])
                        if ALLRED and not GOLD and ALLGREEN:
                            skin.truncate ( )
                            skin.writelines (["ALLRED\n", "ALLGREEN", "\n", "\n#"])
                        skin.close ( )
                        variableInutile10 = 1
                if Money < 45 :
                    erreurtime = pygame.time.get_ticks()
        else :
            pygame.draw.rect (gameDisplay, GREY, (50, 100, 200, 200))
        if 450 < mouse[0] < 650 and 100 < mouse[1] < 300 :
            pygame.draw.rect (gameDisplay, GREEN, (450, 100, 200, 200))
            if click[0] == 1 and ALLGREEN == False:
                if Money >= 150 :
                    Money -= 150
                    pygame.mixer.Sound.play(buyskin)
                    playerSprite = [player_allgreen,player1_allgreen,player2_allgreen,player3_allgreen,player4_allgreen,player5_allgreen,player6_allgreen,saute_allgreen,glisse_allgreen]
                    cash = open ("./data/cash.txt", "r+")
                    cash.seek(0)
                    cash.write(str(int(Money)))
                    cash.truncate()
                    cash.close()
                    ALLGREEN = True
                    if variableInutile9 == 0:
                        skin = open ("./data/skin.txt", "r+")
                        skin.seek (0)
                        if ALLGREEN and not ALLRED and not GOLD:
                            skin.truncate ( )
                            skin.writelines (["\n", "ALLGREEN", "\n", "\n#"])
                        if ALLGREEN and ALLRED and GOLD:
                            skin.truncate ( )
                            skin.writelines (["ALLRED\n", "ALLGREEN", "\nGOLD", "\n#"])
                        if ALLGREEN and ALLRED and not GOLD:
                            skin.truncate ( )
                            skin.writelines (["ALLRED\n", "ALLGREEN", "\n", "\n#"])
                        if ALLGREEN and not ALLRED and GOLD:
                            skin.truncate ( )
                            skin.writelines (["\n", "ALLGREEN", "\nGOLD", "\n#"])
                        skin.close ( )
                        variableInutile9 = 1
                if Money < 150 :
                    erreurtime = pygame.time.get_ticks()
        else:
            pygame.draw.rect(gameDisplay,GREY,(450,100,200,200))
        if 250 < mouse[0] < 450 and 350 < mouse[1] < 550 :
            pygame.draw.rect (gameDisplay, GOLD_color, (250, 350, 200, 200))
            if click[0] == 1 and GOLD == False:
                if Money >= 1000 :
                    Money -= 1000
                    pygame.mixer.Sound.play(buyskin)
                    playerSprite = [player_gold,player1_gold,player2_gold,player3_gold,player4_gold,player5_gold,player6_gold,saute_gold,glisse_gold]
                    cash = open ("./data/cash.txt", "r+")
                    cash.seek(0)
                    cash.write(str(int(Money)))
                    cash.truncate()
                    cash.close()
                    GOLD = True
                    if variableInutile8 == 0:
                        skin = open ("./data/skin.txt", "r+")
                        skin.seek(0)
                        if GOLD and not ALLRED and not ALLGREEN:
                            skin.truncate ( )
                            skin.writelines (["\n", "\n","\nGOLD","\n#"])
                        if GOLD and ALLRED and ALLGREEN:
                            skin.truncate ( )
                            skin.writelines (["ALLRED\n", "ALLGREEN", "\nGOLD","\n#"])
                        if GOLD and ALLRED and not ALLGREEN:
                            skin.truncate ( )
                            skin.writelines (["ALLRED\n", "\n", "\nGOLD","\n#"])
                        if GOLD and not ALLRED and ALLGREEN:
                            skin.truncate ( )
                            skin.writelines (["\n", "ALLGREEN", "\nGOLD","\n#"])
                        skin.close ( )
                        variableInutile8 = 1
                if Money < 1000 :
                    erreurtime = pygame.time.get_ticks()
        else:
            pygame.draw.rect (gameDisplay, GREY, (250, 350, 200, 200))
        if 0 <= pygame.time.get_ticks ( ) - dessinage <= 142:
            gameDisplay.blit (player_allred, (150-((player_allred.get_size()[0])/2), 100))
            gameDisplay.blit (player_allgreen, (550 - ((player_allgreen.get_size ( )[0]) / 2), 100))
            gameDisplay.blit (player_gold, (350 - ((player_gold.get_size ( )[0]) / 2), 350))
        elif 142 <= pygame.time.get_ticks ( ) - dessinage <= 284:
            gameDisplay.blit (player1_allred, (150-((player1_allred.get_size()[0])/2), 100))
            gameDisplay.blit (player1_allgreen, (550 - ((player_allred.get_size ( )[0]) / 2), 100))
            gameDisplay.blit (player1_gold, (350 - ((player_gold.get_size ( )[0]) / 2), 350))
        elif 284 <= pygame.time.get_ticks ( ) - dessinage <= 426:
            gameDisplay.blit (player2_allred, (150-((player2_allred.get_size()[0])/2),100))
            gameDisplay.blit (player2_allgreen, (550 - ((player_allred.get_size ( )[0]) / 2), 100))
            gameDisplay.blit (player2_gold, (350 - ((player_gold.get_size ( )[0]) / 2), 350))
        elif 426 <= pygame.time.get_ticks ( ) - dessinage <= 568:
            gameDisplay.blit (player3_allred, (150-((player3_allred.get_size()[0])/2), 100))
            gameDisplay.blit (player3_allgreen, (550 - ((player_allred.get_size ( )[0]) / 2), 100))
            gameDisplay.blit (player3_gold, (350 - ((player_gold.get_size ( )[0]) / 2), 350))
        elif 568 <= pygame.time.get_ticks ( ) - dessinage <= 710:
            gameDisplay.blit (player4_allred, (150-((player4_allred.get_size()[0])/2), 100))
            gameDisplay.blit (player4_allgreen, (550 - ((player_allred.get_size ( )[0]) / 2), 100))
            gameDisplay.blit (player4_gold, (350 - ((player_gold.get_size ( )[0]) / 2), 350))
        elif 710 <= pygame.time.get_ticks ( ) - dessinage <= 852:
            gameDisplay.blit (player5_allred, (150-((player5_allred.get_size()[0])/2), 100))
            gameDisplay.blit (player5_allgreen, (550 - ((player_allred.get_size ( )[0]) / 2), 100))
            gameDisplay.blit (player5_gold, (350 - ((player_gold.get_size ( )[0]) / 2), 350))
        elif 852 <= pygame.time.get_ticks ( ) - dessinage <= 1000:
            gameDisplay.blit (player6_allred, (150-((player6_allred.get_size()[0])/2), 100))
            gameDisplay.blit (player6_allgreen, (550 - ((player_allred.get_size ( )[0]) / 2), 100))
            gameDisplay.blit (player6_gold, (350 - ((player_gold.get_size ( )[0]) / 2), 350))
        else:
            dessinage = pygame.time.get_ticks ( )
        if pygame.time.get_ticks() - erreurtime < 1000 and not (GOLD or ALLGREEN or ALLRED):
            ecriture("arial", 30,"Vous n'avez pas assez d'argent" , BLACK, 350,350)
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit ( )
                    quit ( )
        if ALLRED:
            ecriture("arial", 25, "Achete !", BLACK,150, 275)
        else:
            ecriture ("arial", 25, "Prix : 45 Dihrams", BLACK, 150, 275)
        if ALLGREEN:
            ecriture ("arial", 25, "Achete !", BLACK, 550, 275)
        else:
            ecriture ("arial", 25, "Prix : 150 Dihrams", BLACK, 550, 275)
        if GOLD:
            ecriture ("arial", 25, "Achete !", BLACK, 350, 525)
        else:
            ecriture ("arial", 25, "Prix : 1000 Dihrams", BLACK, 350, 525)
        if not GOLD:
            variableInutile8 = 0
        if not ALLGREEN :
            variableInutile9 = 0
        if not ALLRED:
            variableInutile10 = 0

        button ("Quitter", 140, 600, 100, 50, GREY, B_RED, quitgame)
        button ("Retour", 420, 600, 100, 50, GREY, BROWN, gameintro)
        pygame.display.update ( )


def scoreFenetre():
    global OPTN, gameDisplay, displayLargeur, displayHauteur, intro, dead, SKIN
    SCORE = True
    displayHauteur = 500
    displayLargeur = 500
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    while SCORE and not intro and not OPTN and not DESC and not SKIN:
        gameDisplay.fill (WHITE)
        hisc = open ("./data/highscore.txt", "r+")
        highscore = hisc.read ( )
        highscore_in_no = int (highscore)
        ligne = hisc.readlines ( )
        if distance >= highscore_in_no:
            hisc.seek (len (ligne))
            hisc.write (str (int (distance)))
            highscore_in_no = distance
        ecriture ("arial",30, "Le meilleur score actuel est de :" + str(highscore_in_no) + " m", BLACK, 250, 100)
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit ( )
                    quit ( )
        button ("Quitter", 100, 350, 100, 50, GREY, B_RED, quitgame)
        button ("Retour", 300, 350, 100, 50, GREY, BROWN, gameintro)
        hisc.close()
        pygame.display.update ( )


def gameintro():
    global gameDisplay, gameMusic,poscurseurX,questionposee, displayLargeur, displayHauteur, intro, dead, OPTN, RUNNER, PAUSE, SCORE, DESC, SKIN, Money, ALLRED,ALLGREEN,GOLD,MUSIC
    displayLargeur = 1024
    displayHauteur = 768
    intro = True
    dead = False
    PAUSE = False
    OPTN = False
    DESC = False
    SKIN = False
    SCORE = False
    questionposee = []
    initDifficulty()
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    pygame.mixer.Sound.set_volume(gameMusic,1)
    pygame.mixer.Sound.stop(ambianceRunner)
    while intro and not OPTN and not DESC and not SKIN:
        sett = open ("./data/settings.txt", "r")
        lignes = sett.readlines ( )
        if lignes[0] == "1\n":
            poscurseurX = 100
        if lignes[0] == "2\n":
            poscurseurX = 200
        if lignes[0] == "3\n":
            poscurseurX = 300
        if lignes[1] == "0\n":
            MUSIC = False
        if lignes[1] == "1\n":
            MUSIC = True
        sett.close ( )
        if not pygame.mixer.get_busy ( ) and MUSIC:
            pygame.mixer.Sound.play (gameMusic, -1) #-1 pr qu'il tourne infini
        cash = open ("./data/cash.txt", "r+")
        banque = cash.read ( )
        Money = int (banque)
        ligne = cash.readlines ( )
        if Money != int(banque):
            cash.seek (len (ligne))
            cash.write (str (int (Money)))
        for event in pygame.event.get ( ):
            if event.type == pygame.QUIT:
                pygame.quit ( )
                quit ( )
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit ( )
                    quit ( )
        cash.close()
        skin = open("./data/skin.txt", "r")
        lignes = skin.readlines()
        if lignes[0] == "ALLRED\n":
            ALLRED = True
        if lignes[1]== "ALLGREEN\n":
            ALLGREEN = True
        if lignes[2] == "GOLD\n":
            GOLD = True
        skin.close()
        gameDisplay.blit (introback, (0, 0))
        ecriture("comic sans ms", 105,"Casa Surfer",B_GREEN,displayLargeur / 2,displayHauteur / 12)
        ecriture("arial", 50, "Vous avez actuellement " + str(Money)+ " Dirhams !",BLACK, displayLargeur / 2, 9.5*displayHauteur / 12)
        button ("Jouer", 250, 200, 200, 50, GREY, B_GREEN, restart)
        button ("Option", 550, 200, 200, 50, GREY, B_RED, optionbutton)
        button ("Description", 250, 350, 200, 50, GREY, B_GREEN, descriptionbutton)
        button ("Apparence", 550, 350, 200, 50, GREY, B_RED, skinbutton)
        button ("Meilleur scores", 250, 500, 200, 50, GREY, B_GREEN, scorebutton)
        button ("Quitter", 550, 500, 200, 50, GREY, B_RED, quitgame)
        pygame.display.update ( )
        clock.tick (15)


def DynamiqueduJeu():
    global taxiPos, distance,ENDSHIELD,randomsound,variableInutile12,var_tempsApparition,shieldduration, var_acceleration,var_distanceSecu,var_speedPlayer,var_timeannimation, SHIELDED,timeshield,timeendshield, Money, RUNNER,speedPlayer,timeannimation, coinspawn, speedBus, distanceSecu, previousposPlayer, speedTaxi, acceleration, STPSPWNBACK, toDelete, tempsApparition, variableInutile, obstacleReuse, decospawn, typeDeco, posBackY, moving, STPSPWNBANDE, STPSPWNCOIN, nbrObstacleVisible, typeObstacle, STPSPWNOB, speedTaxi, speedBande, speedBus, obstacleSpawn, dead, positionPlayer, playerHauteur, playerLargeur, posPlayerY, posPlayerX, gradualApparition, randomlist, EXPLO, textMort, profondeurJ, obtstacleType, obstacles, obstaclesPos, obstaclePos, nbrBandeVisible, posBandeX, posBandeY, bandesPos, bandePos
    apparitionBandes ( )
    initDifficulty()
    # if pygame.time.get_ticks() - coinspawn >= 1000:
    #   apparitionCoin()
    #  coinspawn = pygame.time.get_ticks()
    if pygame.time.get_ticks ( ) - decospawn >= 500:
        apparitionBack ( )
        decospawn = pygame.time.get_ticks ( )
    if pygame.time.get_ticks ( ) - obstacleSpawn >= 3333:
        apparitionObstacles ( )
        apparitionCoin ( )
        obstacleSpawn = pygame.time.get_ticks ( )
    if len (Back) >= nbrDecoVisible:
        STPSPWNBACK = True
    if len (obstacles) >= nbrObstacleVisible: #liste plus longues var
        STPSPWNOB = True
    if len (bandesPos) >= nbrBandeVisible:
        STPSPWNBANDE = True
    if len (coins) >= nbrCoinVisible:
        STPSPWNCOIN = True
    for t in range (len (obstacles)):
        if obstacles[t][0][0] == "taxi" or obstacles[t][0][0] == "bus" or obstacles[t][0][0] == "moto": #inception 0
            obstacles[t][1] = [obstacles[t][1][0] + obstacles[t][0][2] * acceleration, obstacles[t][1][1]]
            ############################################TRAVAIL SUR LES BOT#############################################
            # Travail sur les taxi qui ralentissent a la rencontre d un bus plus lent
    for x in range (len (obstacles)):
        for y in range (len (obstacles)):
            if obstacles[x][1][1] - obstacles[y][1][1] == 0 and abs (int (obstacles[x][1][0]) - int (obstacles[y][1][0])) <= obstacles[y][0][1][1] + (distanceSecu + distanceSecu/2) and obstacles[x][0][0] == "taxi" and obstacles[y][0][0] == "bus":
                obstacles[x] = [[obstacles[x][0][0], obstacles[x][0][1], obstacles[y][0][2]], obstacles[x][1]]
                if variableInutile12 == 0:
                    pygame.mixer.Sound.set_volume (klaxtaxi, 1)
                    pygame.mixer.Sound.play(klaxtaxi)
                    variableInutile12 = 1
            elif obstacles[x][1][1] - obstacles[y][1][1] == 0 and abs (int (obstacles[x][1][0]) - int (obstacles[y][1][0])) <= obstacles[x][0][1][1] + distanceSecu + 25 and obstacles[x][0][0] == "taxi" and obstacles[y][0][0] == "taxi":
                obstacles[y] = [[obstacles[y][0][0], obstacles[y][0][1], obstacles[x][0][2]], obstacles[y][1]]
            if not obstacles[x][1][1] - obstacles[y][1][1] == 0 and abs (int (obstacles[x][1][0]) - int (obstacles[y][1][0])) <= obstacles[y][0][1][1] + (distanceSecu + distanceSecu/2) and obstacles[x][0][0] == "taxi" and obstacles[y][0][0] == "bus":
                variableInutile12 = 0
    ##########################################################################################################

    for x in range (len (obstacles)):
        if obstacles[x][0][0] == "taxi" and -taxiLargeur <= int (obstacles[x][1][0]) - int (posPlayerX) <= playerLargeur and abs (int (posPlayerY) - int (obstacles[x][1][1])) == 0 and (profondeurJ == 0 or profondeurJ == 1):  # collision obstacle joueur
            if not SHIELDED and not ENDSHIELD:
                dead = True
                textMort = 'Un taxi vous a ecrase !'
                pygame.mixer.Sound.set_volume (klaxtaxi, 1)
                pygame.mixer.Sound.play(klaxtaxi)
                pygame.mixer.Sound.play (deathshot)
                pygame.mixer.Sound.play (deathfall)
            if SHIELDED :
                pygame.mixer.Sound.play(shieldcollision,0,1000)
    for y in range (len (obstacles)):
        if obstacles[y][0][0] == "bus" and -busLargeur <= int (obstacles[y][1][0]) - int (posPlayerX) <= playerLargeur and abs (int (posPlayerY) - int (obstacles[y][1][1])) == 0 and (profondeurJ == 2 or profondeurJ == 1):
            if not SHIELDED and not ENDSHIELD:
                dead = True
                textMort = 'Un bus vous a ecrase !'
                pygame.mixer.Sound.set_volume (klaxbus, 1)
                pygame.mixer.Sound.play(klaxbus)
                pygame.mixer.Sound.play (deathshot)
                pygame.mixer.Sound.play (deathfall)
            if SHIELDED :
                pygame.mixer.Sound.play(shieldcollision,0,1000)
    for z in range (len (obstacles)):
        if obstacles[z][0][0] == "moto" and -motoLargeur <= int (obstacles[z][1][0]) - int (posPlayerX) <= playerLargeur and 0 <= abs (int (posPlayerY) - int (obstacles[z][1][1])) <= 50 :  # collision obstacle joueur
            if previousposPlayer == 50 and animationdown and obstacles[z][1][1] == 50 :
                if not SHIELDED and not ENDSHIELD:
                    dead = True
                    textMort = 'Une moto vous a ecrase !'
                    pygame.mixer.Sound.set_volume (klaxmoto, 1)
                    pygame.mixer.Sound.play (klaxmoto)
                    pygame.mixer.Sound.play (deathshot)
                    pygame.mixer.Sound.play (deathfall)
                if SHIELDED:
                    pygame.mixer.Sound.play (shieldcollision,0,1000)
            if previousposPlayer == 450 and animationup and obstacles[z][1][1] == 250 :
                if not SHIELDED and not ENDSHIELD:
                    dead = True
                    textMort = 'Une moto vous a ecrase !'
                    pygame.mixer.Sound.set_volume (klaxmoto, 1)
                    pygame.mixer.Sound.play (klaxmoto)
                    pygame.mixer.Sound.play (deathshot)
                    pygame.mixer.Sound.play (deathfall)
                if SHIELDED:
                    pygame.mixer.Sound.play (shieldcollision,0,1000)
            if previousposPlayer == 250 and animationdown and obstacles[z][1][1] == 250 :
                if not SHIELDED and not ENDSHIELD:
                    dead = True
                    textMort = 'Une moto vous a ecrase !'
                    pygame.mixer.Sound.set_volume (klaxmoto, 1)
                    pygame.mixer.Sound.play (klaxmoto)
                    pygame.mixer.Sound.play (deathshot)
                    pygame.mixer.Sound.play (deathfall)
                if SHIELDED:
                    pygame.mixer.Sound.play (shieldcollision,0,1000)
            if previousposPlayer == 250 and animationup and obstacles[z][1][1] == 50 :
                if not SHIELDED and not ENDSHIELD:
                    dead = True
                    textMort = 'Une moto vous a ecrase !'
                    pygame.mixer.Sound.set_volume (klaxmoto, 1)
                    pygame.mixer.Sound.play (klaxmoto)
                    pygame.mixer.Sound.play (deathshot)
                    pygame.mixer.Sound.play (deathfall)
                if SHIELDED:
                    pygame.mixer.Sound.play (shieldcollision,0,1000)
    for y in range (len (coins)):
        if coins[y][0][0] == "coin" and -coinLargeur <= int (coins[y][1][0]) - int (posPlayerX) <= playerLargeur and abs (int (posPlayerY) - int (coins[y][1][1])) == 0 and (profondeurJ == 0 or profondeurJ == 1):
            Money += 1
            pygame.mixer.Sound.play(coinSound)
            randomNU1 = randint (0, 10)
            if randomNU1 == 0 or randomNU1 == 1 or randomNU1 == 2 or randomNU1 == 3 or randomNU1 == 4 or randomNU1 == 5 or randomNU1 == 6 or randomNU1 == 7 or randomNU1 == 8 or randomNU1 == 9:
                bonus3 = coin
            if randomNU1 == 10:
                bonus3 = shield
            coins[y] = [bonus3,random.choice(couloir)]
        if coins[y][0][0] == "shield" and -shieldLargeur <= int (coins[y][1][0]) - int (posPlayerX) <= playerLargeur and abs (int (posPlayerY) - int (coins[y][1][1])) == 0 and (profondeurJ == 0 or profondeurJ == 1):
            SHIELDED = True
            timeshield = pygame.time.get_ticks()
            randomNU2 = randint (0, 10)
            pygame.mixer.Sound.play(shieldON)
            if randomNU2 == 0 or randomNU2 == 1 or randomNU2 == 2 or randomNU2 == 3 or randomNU2 == 4 or randomNU2 == 5 or randomNU2 == 6 or randomNU2 == 7 or randomNU2 == 8 or randomNU2 == 9:
                bonus3 = coin
            if randomNU2 == 10:
                bonus3 = shield
            coins[y] = [bonus3,random.choice(couloir)]
    for c in range (len (coins)): #avancer pieces
        if coins[c][1][0] != -(coins[c][0][1][0]):
            coins[c][1] = [coins[c][1][0] + coins[c][0][2], coins[c][1][1]]
    for c in range (len (coins)): #reutilisation pieces
        if coins[c][1][0] <= -(coins[c][0][1][0]):
            randomNU = randint (0, 10)
            if randomNU == 0 or randomNU == 1 or randomNU == 2 or randomNU == 3 or randomNU == 4 or randomNU == 5 or randomNU == 6 or randomNU == 7 or randomNU == 8 or randomNU == 9:
                bonus = coin
            if randomNU == 10:
                bonus = shield
            coins[c] = [bonus,random.choice(couloir)]
    for b in range (nbrBandeVisible * 2):  # pour fr avancer les 2 bandes
        bandesPos[b] = (bandesPos[b][0] + speedBande, bandesPos[b][1])
    for b in range (nbrBandeVisible * 2):
        if bandesPos[b][0] <= -100:
            distance += 5 / 2  #augmentation score dist
            bandesPos[b] = (1335, bandesPos[b][1]) # pour fr revenir les bandes
    #############################################Reutilisation##########################################
    for x in range (len (obstacles)):
        if obstacles[x][1][0] <= -(obstacles[x][0][1][0]) and pygame.time.get_ticks ( ) - obstacleReuse >= tempsApparition:
            randomN = randint (0, 4)
            Position = random.choice (couloir)
            Positionmoto = random.choice(couloirmoto)
            if randomN == 0 or randomN == 1:
                obstacles[x] = [moto, Positionmoto]
                apparitionCoin()
            if randomN == 2:
                obstacles[x] = [bus, Position]
                apparitionCoin()
            if randomN == 3 or randomN == 4:
                obstacles[x] = [taxi, Position]
                apparitionCoin()
            obstacleReuse = pygame.time.get_ticks ( )
    if SHIELDED and not ENDSHIELD and pygame.time.get_ticks() - timeshield > shieldduration :
        ENDSHIELD = True
        timeendshield = pygame.time.get_ticks()
    if SHIELDED and ENDSHIELD and pygame.time.get_ticks() - timeendshield > 2500 :
        ENDSHIELD = False
        SHIELDED = False
        pygame.mixer.Sound.play(shieldOFF)
    if pygame.time.get_ticks() - randomsound >= randint(3000,10000) and MUSIC:
        pygame.mixer.Sound.set_volume(klaxtaxi,0.1)
        pygame.mixer.Sound.set_volume(klaxbus,0.1)
        pygame.mixer.Sound.set_volume(klaxmoto,0.1)
        sounds = [klaxtaxi,klaxbus,klaxmoto]
        pygame.mixer.Sound.play(random.choice(sounds))
        randomsound = pygame.time.get_ticks()
    ###################################################################################################
    for x in range (len (Back)):
        Back[x][1] = [Back[x][1][0] + Back[x][0][2], Back[x][1][1]]
        if Back[x][1][0] <= -(Back[x][0][1][0]):
            Back[x] = [random.choice (typeDeco), random.choice (posBackY)] #recyclage
    #############################ACCELERATION#############################################
    if distance % 25 == 0 and variableInutile == 0:  #chaque 25 m, le reste =0
        tempsApparition *= var_tempsApparition #0.95
        # for x in range(len(obstacles)):
        acceleration += var_acceleration #0.1
        variableInutile = 1 #change de valeur pour ne plus refaire
        distanceSecu += var_distanceSecu #20
        speedPlayer += var_speedPlayer #1
        timeannimation -= var_timeannimation #20
    if distance % 25 != 0:
        variableInutile = 0 #reprend sa valeur 0 apres 25m
    ####################################BLOCAGE ACCELERATION SINON JEU TROP DUR#################################################
    if tempsApparition <= 800:
        tempsApparition = 800
    #####################################SAUVEGARDE DES SCORES#################################################################
    cash = open ("./data/cash.txt", "r+")
    banque = cash.read ( )
    ligne = cash.readlines ( )
    if Money != int (banque):
        cash.seek (len (ligne))
        cash.write (str (int (Money)))
    cash.close()
    hisc = open ("./data/highscore.txt", "r+")
    highscore = hisc.read ( )
    highscore_in_no = int (highscore)
    ligne = hisc.readlines ( )
    if distance >= highscore_in_no:
        hisc.seek (len (ligne))
        hisc.write (str (int (distance)))
        highscore_in_no = distance
    hisc.close()

def initDifficulty():
    global Difficulty,playerSprite,speedPlayer,acceleration,var_tempsApparition,var_acceleration,var_distanceSecu,var_speedPlayer,var_timeannimation,speedTaxi,speedMoto,speedBus,shieldduration,nbrObstacleVisible,nbrCoinVisible,tempsApparition,distanceSecu,speedBande,timeannimation
    if Difficulty == 1:
        speedTaxi = -15
        speedBus = -7
        speedMoto = -18
        nbrObstacleVisible = 7
        nbrCoinVisible = 10
        tempsApparition = 3500
        speedPlayer = 4
        acceleration = 1
        distanceSecu = 25
        timeannimation = 650
        shieldduration = 6000
        var_tempsApparition = 0.99
        var_acceleration = 0.1
        var_distanceSecu = 20
        var_speedPlayer = 1
        var_timeannimation = 30
    if Difficulty == 2:
        speedTaxi = -18
        speedBus = -10
        speedMoto = -20
        nbrObstacleVisible = 8
        nbrCoinVisible = 9
        tempsApparition = 3333
        speedPlayer = 5
        acceleration = 1
        distanceSecu = 35
        timeannimation = 500
        shieldduration = 5000
        var_tempsApparition = 0.95
        var_acceleration = 0.15
        var_distanceSecu = 35
        var_speedPlayer = 1
        var_timeannimation = 20
    if Difficulty == 3:
        speedTaxi = -21
        speedBus = -12
        speedMoto = -25
        nbrObstacleVisible = 9
        nbrCoinVisible = 8
        tempsApparition = 3000
        speedPlayer = 7
        acceleration = 1
        distanceSecu = 50
        timeannimation = 400
        shieldduration = 4000
        var_tempsApparition = 0.95
        var_acceleration = 0.1
        var_distanceSecu = 50
        var_speedPlayer = 1
        var_timeannimation = 10
    if ALLRED:
        playerSprite = [player_allred, player1_allred, player2_allred, player3_allred, player4_allred, player5_allred, player6_allred, saute_allred, glisse_allred]
    if ALLGREEN:
        playerSprite = [player_allgreen, player1_allgreen, player2_allgreen, player3_allgreen, player4_allgreen, player5_allgreen, player6_allgreen, saute_allgreen, glisse_allgreen]
    if GOLD:
        playerSprite = [player_gold, player1_gold, player2_gold, player3_gold, player4_gold, player5_gold, player6_gold, saute_gold, glisse_gold]


def dessiner():
    global taxiPos, obstacles, intro, taxi,SHIELDED,clignote, playerSprite,footsteps,variableInutile4, obstacleSpawn,posPlayerY,variableInutile3,previousposPlayer, typeObstacle,animationdown ,animationup, coins, dessinage, taxi_sprite, bus_sprite, tick, bus, GLISSER, SAUTER, nbrBandeVisible, bandePos, bandesPos, posBandeY, OPTN
    intro = False
    gameDisplay.blit (background, (0, 0))
    for b in range (nbrBandeVisible * 2):
        gameDisplay.blit (bande, bandesPos[b])
    if GLISSER:
        gameDisplay.blit (playerSprite[8], (posPlayerX, posPlayerY))
    if SAUTER:
        gameDisplay.blit (playerSprite[7], (posPlayerX, posPlayerY))
    if not GLISSER and not SAUTER and not dead:  #GIF persotb
        if 0 <= pygame.time.get_ticks ( ) - dessinage <= 142:
            gameDisplay.blit (playerSprite[0], (posPlayerX, posPlayerY))
        elif 142 <= pygame.time.get_ticks ( ) - dessinage <= 284:
            gameDisplay.blit (playerSprite[1], (posPlayerX, posPlayerY))
        elif 284 <= pygame.time.get_ticks ( ) - dessinage <= 426:
            gameDisplay.blit (playerSprite[2], (posPlayerX, posPlayerY))
        elif 426 <= pygame.time.get_ticks ( ) - dessinage <= 568:
            gameDisplay.blit (playerSprite[3], (posPlayerX, posPlayerY))
        elif 568 <= pygame.time.get_ticks ( ) - dessinage <= 710:
            gameDisplay.blit (playerSprite[4], (posPlayerX, posPlayerY))
        elif 710 <= pygame.time.get_ticks ( ) - dessinage <= 852:
            gameDisplay.blit (playerSprite[5], (posPlayerX, posPlayerY))
        elif 852 <= pygame.time.get_ticks ( ) - dessinage <= 1000:
            gameDisplay.blit (playerSprite[6], (posPlayerX, posPlayerY))
        else:
            dessinage = pygame.time.get_ticks ( )
    if MUSIC and not GLISSER and not SAUTER :
        if 0 <= pygame.time.get_ticks() - footsteps <= 500 and variableInutile4 == 0:
            pygame.mixer.Sound.play (leftFoot,0)
            variableInutile4 = 1
        elif 500 <= pygame.time.get_ticks() - footsteps <= 1000 and variableInutile4 == 1:
            pygame.mixer.Sound.play (rightFoot,0)
            variableInutile4 = 0
        elif 1000 < pygame.time.get_ticks() - footsteps :
            footsteps = pygame.time.get_ticks()
    if dead:
        gameDisplay.blit (glisse_default, (posPlayerX, posPlayerY))
    if SHIELDED and not ENDSHIELD:
        gameDisplay.blit (shield_sprite,(posPlayerX-(shieldLargeur/2),posPlayerY))
    if SHIELDED and ENDSHIELD :
        if 0 < pygame.time.get_ticks() - clignote < 150 :
            gameDisplay.blit (shield_sprite, (posPlayerX - (shieldLargeur / 2), posPlayerY))
        elif 150 < pygame.time.get_ticks() - clignote < 300 :
            pass
        else:
            clignote = pygame.time.get_ticks()
    for x in range (len (obstacles)):
        if obstacles[x][0][0] == "taxi":
            gameDisplay.blit (taxi_sprite, (obstacles[x][1]))
        if obstacles[x][0][0] == "bus":
            gameDisplay.blit (bus_sprite, (obstacles[x][1]))
        if obstacles[x][0][0] == "moto":
            gameDisplay.blit (moto103, (obstacles[x][1]))
    for x in range (len (coins)):
        if coins[x][0][0] == "coin":
            gameDisplay.blit (coin_sprite, coins[x][1])
        if coins[x][0][0] == "shield":
            gameDisplay.blit (shield_bonus, coins[x][1])
    for x in range (len (Back)):
        if Back[x][0][0] == "palmier" and Back[x][1][1] == 0:
            gameDisplay.blit (palmier_sprite_Up, Back[x][1])
        if Back[x][0][0] == "palmier" and Back[x][1][1] == 610:
            gameDisplay.blit (palmier_sprite_Down, Back[x][1])
        if Back[x][0][0] == "arbre" and Back[x][1][1] == 0:
            gameDisplay.blit (arbre_sprite_Up, Back[x][1])
        if Back[x][0][0] == "arbre" and Back[x][1][1] == 610:
            gameDisplay.blit (arbre_sprite_Down, Back[x][1])
    if animationdown:
        variableInutile3 = 0
        if 0 < pygame.time.get_ticks ( ) - repereanim <= timeannimation/5 and variableInutile3 == 0:
            posPlayerY += 5 +(5 -((timeannimation*5)/500))
            variableInutile3 = 1
        if timeannimation/5 < pygame.time.get_ticks ( ) - repereanim <= 2*(timeannimation/5) and variableInutile3 == 0:
            posPlayerY += 14 +(14 -((timeannimation*14)/500))
            variableInutile3 = 1
        if 2*(timeannimation/5) < pygame.time.get_ticks ( ) - repereanim <= 3*(timeannimation/5) and variableInutile3 == 0:
            posPlayerY += 15 +(15 -((timeannimation*15)/500))
            variableInutile3 = 1
        if 3*(timeannimation/5) < pygame.time.get_ticks ( ) - repereanim <= 4*(timeannimation/5) and variableInutile3 == 0:
            posPlayerY += 14 +(14 -((timeannimation*14)/500))
            variableInutile3 = 1
        if 4*(timeannimation/5) < pygame.time.get_ticks ( ) - repereanim <= timeannimation and variableInutile3 == 0:
            if previousposPlayer == 250:
                posPlayerY = 450
            if previousposPlayer == 50:
                posPlayerY = 250
            variableInutile3 = 1
            animationdown = False
    if animationup:
        variableInutile3 = 0
        if 0 < pygame.time.get_ticks ( ) -  repereanim <= timeannimation/5 and variableInutile3 == 0:
            posPlayerY -= 5 +(5 -((timeannimation*5)/500))
            variableInutile3 = 1
        if timeannimation/5 < pygame.time.get_ticks ( ) - repereanim <= 2*(timeannimation/5) and variableInutile3 == 0:
            posPlayerY -= 14 +(14 -((timeannimation*14)/500))
            variableInutile3 = 1
        if 2*(timeannimation/5) < pygame.time.get_ticks ( ) - repereanim <= 3*(timeannimation/5) and variableInutile3 == 0:
            posPlayerY -= 15 +(15-((timeannimation*15)/500))
            variableInutile3 = 1
        if 3*(timeannimation/5) < pygame.time.get_ticks ( ) - repereanim <= 4*(timeannimation/5) and variableInutile3 == 0:
            posPlayerY -= 14 +(14-((timeannimation*14)/500))
            variableInutile3 = 1
        if 4*(timeannimation/5) < pygame.time.get_ticks ( ) - repereanim <= timeannimation and variableInutile3 == 0:
            if previousposPlayer == 250:
                posPlayerY = 50
            if previousposPlayer == 450:
                posPlayerY = 250
            variableInutile3 = 1
            animationup = False
    if posPlayerY > 450 :
        posPlayerY = 450
    if posPlayerY < 50 :
        posPlayerY = 50
    ##########################DEBUGAGE COLLISION ENLEVER LES HASHTAGS############################
    #for x in range(len(obstacles)):
     #  pygame.draw.rect (gameDisplay, BLUE, (obstacles[x][1], obstacles[x][0][1]), 5)
    #for x in range(len(coins)):
     #  pygame.draw.rect (gameDisplay, GREEN, (coins[x][1], coins[x][0][1]), 5)
    #pygame.draw.rect(gameDisplay,BLUE,(posPlayerX,posPlayerY,200,200),5)
    #############################################################################################

    #score dist
    pygame.draw.rect (gameDisplay, GREY_Alpha, (0, 645, 250, 100))
    ecriture ("arial", 20, "Distances :" + " " + str (int (distance)) + " m", BLACK, 125, 675)
    #en haut gauche
    pygame.draw.rect (gameDisplay, BLACK, (0, 0, 250, 53))
    ecriture("arial",20, str (int (Money)),WHITE, 110,25)
    gameDisplay.blit (coin_sprite, (50, -75))

def controleclavier():
    global positionPlayer, posPlayerX, posPlayerY, profondeurJ, mouvement, GLISSER, SAUTER, PAUSE, presseRight, repereanim, animation, animationdown, animationup, previousposPlayer
    if pygame.time.get_ticks ( ) - mouvement >= 1500 and (profondeurJ == 0 or profondeurJ == 2):
        profondeurJ = 1
        GLISSER = False
        SAUTER = False
    touchePresse = pygame.key.get_pressed ( )
    presseRight = 0
    for event in pygame.event.get ( ):
        if event.type == pygame.QUIT:
            pygame.quit ( )
            quit ( )
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE and PAUSE == False:
                PAUSE = True
                paused ( )
            if event.key == pygame.K_ESCAPE and PAUSE == True:
                PAUSE = False
        if event.type == pygame.KEYDOWN:  # pr touche pressee
            if event.key == pygame.K_a and not GLISSER and not SAUTER:
                profondeurJ = 0
                GLISSER = True
                mouvement = pygame.time.get_ticks ( )
            if event.key == pygame.K_SPACE and not GLISSER and not SAUTER:
                profondeurJ = 2
                SAUTER = True
                mouvement = pygame.time.get_ticks ( )
                if MUSIC :
                    pygame.mixer.Sound.play(jumpSound)
            if event.key == pygame.K_DOWN and posPlayerY < 450 and animationdown == False and animationup == False:
                animationdown = True
                repereanim = pygame.time.get_ticks ( )
                previousposPlayer = posPlayerY
                if MUSIC :
                    pygame.mixer.Sound.play(changeCouloir)
            if event.key == pygame.K_UP and posPlayerY > 50 and animationup == False and animationdown == False:  # pour pas qu'il sorte du cadre
                animationup = True
                repereanim = pygame.time.get_ticks ( )
                previousposPlayer = posPlayerY
                if MUSIC :
                    pygame.mixer.Sound.play(changeCouloir)
            if event.key == pygame.K_f:
                # pygame.display.toggle_fullscreen()
                pygame.display.set_mode (pygame.display.list_modes ( )[0], pygame.FULLSCREEN)
    if touchePresse[pygame.K_RIGHT] and posPlayerX <= 700:
        posPlayerX += speedPlayer
    if touchePresse[pygame.K_LEFT] and posPlayerX >= 20:
        posPlayerX -= speedPlayer


def gameloop():
    global gameDisplay,reponsechoisie, dead, OPTN, PAUSE,variableInutile11, variableInutile5,variableInutile6, chanson1time, chansontime, variableInutile7, questionposee
    displayLargeur = 1300
    displayHauteur = 700
    gameDisplay = pygame.display.set_mode ((displayLargeur, displayHauteur))
    intro = False
    dead = False
    PAUSE = False
    variableInutile11 = 0
    reponsechoisie = 0
    pygame.mixer.Sound.stop (gameMusic)
    pygame.mixer.Sound.set_volume (ambianceRunner,0.5)
    pygame.mixer.Sound.set_volume(gameMusic,0.5)
    initDifficulty()
    while not intro and not OPTN and not DESC and not SKIN and not SCORE:
        if MUSIC and variableInutile5 == 0:
            pygame.mixer.Sound.play (ambianceRunner)
            variableInutile5 = 1
            chansontime = pygame.time.get_ticks()
        if pygame.time.get_ticks() - chansontime > (pygame.mixer.Sound.get_length(ambianceRunner)*1000):
            variableInutile5 = 0
        if MUSIC and variableInutile6 == 0:
            pygame.mixer.Sound.play (gameMusic)
            variableInutile6 = 1
            chanson1time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - chanson1time > (pygame.mixer.Sound.get_length(gameMusic)*1000):
            variableInutile6 = 0
        deadFenetre ( )
        clock.tick (70)
        controleclavier ( )
        DynamiqueduJeu ( )
        dessiner ( )
        pygame.display.update ( )
        pygame.display.flip ( )






gameintro ( )
gameloop ( )