import pygame as py
class Pion_noir(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nombre_jeton=12
        self.nbre_max_jeton=12
        self.velocity=5
        self.image = py.image.load('asset/pion_noir.png')
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y= 545