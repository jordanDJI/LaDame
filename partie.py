import pygame as py
from pion_noir import Pion_noir 
from pion_bleu import Pion_bleu



class partie():
    def __init__(self):
        self.duree :int
        self.vainqueur : str
        self.list_pion_noir=[]
        self.list_pion_bleu=[]
    
    

    
    def cree_classer_les_pions(self):
       for i in range(Pion_noir.nbre_max_jeton-1):
            pion_n= Pion_noir()
            pion_n.numero = i
            for j in range (2):
                if j == 0:
                    pion_n.rect.y=545
                    pion_n.rect.x = 110
                    for k in range(2):
                        if pion_n.rect.x <= 440:
                            pion_n.rect.x += 110
                            self.list_pion_noir.append(pion_n)
                        elif k==3 and self.rect.x >=500:
                            pion_n.rect.x= 410
                            self.list_pion_noir.append(pion_n)
                elif j == 1:
                    pion_n.rect.y= 468
                    for k in range(2):
                        if pion_n.rect.x < 16:
                            pion_n.rect.x=16
                            self.list_pion_noir.append(pion_n)
                        elif pion_n.rect.x <= 16:
                            pion_n.rect.x += 94
                            self.list_pion_noir.append(pion_n)
                        elif pion_n.rect.x <= 440:
                            pion_n.rect.x += 110
                            self.list_pion_noir.append(pion_n)
                        elif k==3 and self.rect.x >=500:
                            pion_n.rect.x= 410
                            self.list_pion_noir.append(pion_n)
                elif j == 2:
                    pion_n.rect.y=391
                    pion_n.rect.x = 110
                    for k in range(3):
                        if pion_n.rect.x <= 440:
                            pion_n.rect.x += 110
                            self.list_pion_noir.append(pion_n)
                        elif k==3 and self.rect.x >=500:
                            pion_n.rect.x= 410
                            self.list_pion_noir.append(pion_n)

    print(self.list_pion_noir)


"""def afficher_pieces(self, pion_couleur,list_pions_couleur):
        for pion_couleur in list_pions_couleur:
            py.screen.blit(pion_couleur.image, pion_couleur.rect)"""
#self1 = self()
#self1.cree_les_pions(Pion_noir)    
#print(self1)

