import pygame
from pion_noir import Pion_noir
from pion_bleu import Pion_bleu


class Partie:
    def __init__(self):
        self.pion13 = Pion_bleu()
        self.pion1 =Pion_noir()

    def jouer(self):
        runining: true
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False



                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Gérer le clic de la souris pour effectuer les mouvements
                    pos = pygame.mouse.get_pos()


pygame.quit()

# Exemple d'utilisation
partie = Partie()
partie.jouer()