import pygame as py
import sys
from partie import Partie
from Pion_noiroir import Pion_noiroir
py.init()

py.display.set_caption("La Dame")
screen=py.display.set_mode((748,616))

#importer l'image d'arriere plan
background= py.image.load('asset/table_dame.jpg')


#charger le jeu
partie = Partie()
pionNoir= []
#pionNoir= 

running = True

#boucle tant que cette condition est vrai
while running:
    #appliquer l'arriere plan de notre jeu
    screen.blit(background,(0,0))

    screen.blit(partie.pion1.image, partie.pion1.rect)
    screen.blit(partie.pion13.image, partie.pion13.rect)
    screen.blit(partie.pion2.image, partie.pion2.rect)
    screen.blit(partie.pion3.image, partie.pion3.rect)

    #mettre a jour l'ecran
    py.display.flip()
    #def get_position(x,y):
    #    row= y//Square
    #    col=x//Square

    pos_souris = (0, 0)
    #si le joueur ferme cette fenetre
    for event in py.event.get():
        if event.type == py.QUIT:
            running=False
            py.QUIT()
            print("fermerture du")
        
        elif event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT :
                print("deplacement en diagonal droit")
            elif event.key == py.K_LEFT :
                print("deplacement en diagonal gauche")

        elif event.type == py.MOUSEBUTTONDOWN:
            if event.button ==1 :
                location= py.mousse.get_pos()
                #row,col =get_position(locat)
                print("clique gache de la souris", event.pos )

        elif event.type == py.MOUSEMOTION:
            pos_souris = event.pos
            print("position de la souris", pos_souris)
main()