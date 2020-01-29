import pygame
from pygame.locals import *
pygame.init()

def main():
# Initialisation de la fenêtre d'affichage
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption('Programme Pygame de base')
 
    # Remplissage de l'arrière-plan
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
################################################################################
    "définition du perso"
    xperso=1
    yperso=420
    monpersonnage = pygame.Rect(xperso, yperso, 32, 32)
    #perso_green = pygame.draw.rect(background, (0,255,0), monpersonnage)
    pygame.draw.rect(background,(0,255,0), monpersonnage)
########
    print('debut monperso : ',monpersonnage)
########
    "définition des murs"
     mur1 = pygame.Rect(160, 160, 40, 160)
    pygame.draw.rect((0,0,0), background, mur1)
    mur2 = pygame.Rect(160, 400, 40, 160)
    pygame.draw.rect(background, (0,0,0), mur2)
    mur3 = pygame.Rect(320, 240, 40, 240)
    pygame.draw.rect(background, (0,0,0), mur3)
    mur4 = pygame.Rect(400, 80, 200, 40)
    pygame.draw.rect(background, (0,0,0), mur4)
    mur5 = pygame.Rect(400, 560, 200, 40)
    pygame.draw.rect(background, (0,0,0), mur5)
    mur6 = pygame.Rect(700, 80, 200, 40)
    pygame.draw.rect(background, (0,0,0), mur6)
    mur7 = pygame.Rect(700, 560, 200, 40)
    pygame.draw.rect(background, (0,0,0), mur7)
    mur8 = pygame.Rect(920, 240, 40, 240)
    pygame.draw.rect(background, (0,0,0), mur8)
    mur9 = pygame.Rect(1080, 160, 40, 160)
    pygame.draw.rect(background, (0,0,0), mur9)
    mur10 = pygame.Rect(1080, 400, 40, 160)
    pygame.draw.rect(background, (0,0,0), mur10)
    mur11 = pygame.Rect(580, 340, 120, 40)
    pygame.draw.rect(background, (0,0,0), mur11)
    mur12 = pygame.Rect(620, 300, 40, 120)
    pygame.draw.rect(background, (0,0,0), mur12)
    mescollisions = [mur1,mur2,mur3,mur4,mur5,mur6,mur7,mur8,mur9,mur10,mur11,mur12,]########
 
    # Blitter le tout dans la fenêtre
    screen.blit(background,(0,0))
    pygame.display.flip()
################################################################################
    # Boucle d'évènements
    continuer = True
    pygame.key.set_repeat(200,1)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    print('KEYRIGHT',monpersonnage.collidelist(mescollisions))
                    if monpersonnage.collidelist(mescollisions) != -1:
                    #Le personnage ne peut pas bouger ! Il est en collision !
                    #on arrete le jeu au bout de 3 tentatives ne faire cela que pour cet exempl
                    #NB : La valeur retournée par la méthode collidelist donne
                    #le numero du mur dans la liste avec lequel il y a collision
                        print('COLLISION')
                        pygame.draw.rect(background,(255,255,255), monpersonnage)
                        monpersonnage.move_ip(-1,0)
                        pygame.draw.rect(background,(0,255,0), monpersonnage)
                     
                    else:
                    # Le personnage peut bouger, il n'est pas en collision
                        print('no collision')
                        print('KEYRIGHT',monpersonnage.collidelist(mescollisions))
                        pygame.draw.rect(background,(255,255,255), monpersonnage)
                        monpersonnage.move_ip(1,0)
                        pygame.draw.rect(background,(0,255,0), monpersonnage)
                        #screen.blit(background, (0,0))
                        print('bouge droit : ',monpersonnage)
                #####
 
                if event.key == K_LEFT:
                    print('KEYLEFT',monpersonnage.collidelist(mescollisions))
                    if monpersonnage.collidelist(mescollisions) != -1:
                    #Le personnage ne peut pas bouger ! Il est en collision !
                    #on arrete le jeu au bout de 3 tentatives ne faire cela que pour cet exempl
                    #NB : La valeur retournée par la méthode collidelist donne
                    #le numero du mur dans la liste avec lequel il y a collision
                        print('COLLISION')
                        pygame.draw.rect(background,(255,255,255), monpersonnage)
                        monpersonnage.move_ip(1,0)
                        pygame.draw.rect(background,(0,255,0), monpersonnage)
                         
                    else:
                    # Le personnage peut bouger, il n'est pas en collision
                        print('no collision')
                        print('KEYLEFT',monpersonnage.collidelist(mescollisions))
                        pygame.draw.rect(background,(255,255,255), monpersonnage)
                        monpersonnage.move_ip(-1,0)
                        pygame.draw.rect(background,(0,255,0), monpersonnage)
                        #screen.blit(background, (0,0))
                        print('bouge droit : ',monpersonnage)
                #####
                if event.key == K_UP:
                    print('KEYUP',monpersonnage.collidelist(mescollisions))
                    if monpersonnage.collidelist(mescollisions) != -1:
                    #Le personnage ne peut pas bouger ! Il est en collision !
                    #on arrete le jeu au bout de 3 tentatives ne faire cela que pour cet exempl
                    #NB : La valeur retournée par la méthode collidelist donne
                    #le numero du mur dans la liste avec lequel il y a collision
                        print('COLLISION')
                        pygame.draw.rect(background,(255,255,255), monpersonnage)
                        monpersonnage.move_ip(0,1)
                        pygame.draw.rect(background,(0,255,0), monpersonnage)
                         
                    else:
                    # Le personnage peut bouger, il n'est pas en collision
                        print('no collision')
                        print('KEYUP',monpersonnage.collidelist(mescollisions))
                        pygame.draw.rect(background,(255,255,255), monpersonnage)
                        monpersonnage.move_ip(0,-1)
                        pygame.draw.rect(background,(0,255,0), monpersonnage)
                        #screen.blit(background, (0,0))
                        print('bouge droit : ',monpersonnage)
                 
                #####
                if event.key == K_DOWN:
                    print('KEYDOWN',monpersonnage.collidelist(mescollisions))
                    if monpersonnage.collidelist(mescollisions) != -1: 
                    #Le personnage ne peut pas bouger ! Il est en collision !
                    #on arrete le jeu au bout de 3 tentatives ne faire cela que pour cet exempl
                    #NB : La valeur retournée par la méthode collidelist donne
                    #le numero du mur dans la liste avec lequel il y a collision
                        print('COLLISION')
                        pygame.draw.rect(background,(255,255,255), monpersonnage)
                        monpersonnage.move_ip(0,-1)
                        pygame.draw.rect(background,(0,255,0), monpersonnage)
 
                    else:
                    # Le personnage peut bouger, il n'est pas en collision
                        print('no collision')
                        print('KEYDOWN',monpersonnage.collidelist(mescollisions))
                        pygame.draw.rect(background,(255,255,255), monpersonnage)
                        monpersonnage.move_ip(0,1)
                        pygame.draw.rect(background,(0,255,0), monpersonnage)
                        #screen.blit(background, (0,0))
                        print('bouge droit : ',monpersonnage)
                                        
 
 
        screen.blit(background, (0,0))
        pygame.display.flip()
         
 
    pygame.quit()
 
if __name__ == '__main__': main()