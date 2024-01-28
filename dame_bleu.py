import pygame as pygame

class Dame(py.sprite.Sprite):
	def__init__(self,x,y):
		super().init__()
		self.image=py.image.load('asset/dame_bleu.jpg')
		self.rest = self.image.get_rect()
		self.rect.x = x
        self.rect.y = y