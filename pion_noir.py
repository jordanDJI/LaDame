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

    
    

    """class Pion_noir1:
        list_pion_noir1 = []  # Liste pour stocker les pions noirs

        def __init__(self):
            self.rect = py.rect()  # Assurez-vous que Rect est importé ou défini

        def cree_les_pions1(self, pion_n):
            pion_n = Pion_noir()
            for i in range(pion_n.nbre_max_jeton - 1):
                pion_n.numero = i
                for j in range(3):  # Utilisation de 3 au lieu de 2 pour correspondre aux indices de 0 à 2
                    if j == 0:
                        pion_n.rect.y = 545
                    elif j == 1:
                        pion_n.rect.y = 468
                    elif j == 2:
                        pion_n.rect.y = 391

                    pion_n.rect.x = 110
                    for k in range(3):
                        if pion_n.rect.x <= 440:
                            pion_n.rect.x += 110
                        elif k == 2:  # Utilisation de 2 au lieu de 3 pour correspondre aux indices de 0 à 2
                            pion_n.rect.x = 410
                            Pion_noir.list_pion_noir.append(pion_n)"""
