import pygame as py
import sys
from partie import Partie
py.init()

py.display.set_caption("La Dame")
screen=py.display.set_mode((748,616))

#importer l'image d'arriere plan
background= py.image.load('asset/table_dame.jpg')


#charger le jeu
partie = Partie()

running = True

#boucle tant que cette condition est vrai
while running:
    #appliquer l'arriere plan de notre jeu
    screen.blit(background,(0,0))

    screen.blit(partie.pion1.image, partie.pion1.rect)
    screen.blit(partie.pion13.image, partie.pion13.rect)

    #mettre a jour l'ecran
    py.display.flip()

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
                print("clique gache de la souris", event.pos )

        elif event.type == py.MOUSEMOTION:
            pos_souris = event.pos
            print("position de la souris", pos_souris)