import pygame as py
class Pion_noir(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.numero = numero
        self.nombre_jeton = 0
        self.nbre_max_jeton=12
        self.velocity=5
        self.image = py.image.load('asset/pion_noir.png')
        self.position = py.event.post
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0 

    
    
    def deplacer_pion_noir(self, pion, direction):
        if direction == "avant":
            pion.rect.y -= pion.velocity
        elif direction == "diagonale_gauche":
            pion.rect.x -= pion.velocity
            pion.rect.y -= pion.velocity
        elif direction == "diagonale_droite":
            pion.rect.x += pion.velocity
            pion.rect.y -= pion.velocity

    

    def promouvoir_en_dame(self, pion):
        # Vérifier si le pion atteint la rangée la plus éloignée
        if pion.rect.y <= 0:
            # Remplacer le pion par une dame
            nouvelle_dame = Dame_noire(pion.rect.x, pion.rect.y)
            self.pions_dames.add(nouvelle_dame)
            self.pions_bleus.remove(pion)


    