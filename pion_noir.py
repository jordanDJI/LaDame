import pygame as py
from position_initiale import Position
from pion_bleu import Pion_bleu
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
        self.position = Position(rows, col)
        self.pions_mangeables = []
    def position_diagonal_bas (self):
        return [Position(self.rows + 1, self.col -1), 
        Position(self.rows + 1, self.col + 1)]
    
    def position_diagonal_haut(sefl):
        return [Position(sefl.rows - 1, sefl.col - 1), 
        Position(sefl.rows - 1, sefl.col + 1)]
    #Les positions auxquels le pion peut se déplacer dans tous les sens 
    def Quatre_position_diagonal (self):
        return[Position(self.rows - 1, self.col - 1),
        Position(self.rows - 1, self.col + 1),
        Position(self.rows + 1, self.col - 1),
        Position(self.rows + 1, self.col + 1)]
    
    # Le pion peut se déplacer en diagonale lorsqu'il 
    # mange un autre pion d'un couleur différente
    def Quatre_position_sauter (self):
        return[Position(self.rows - 2, self.col - 2),
        Position(self.rows - 2, self.col + 2),
        Position(self.rows + 2, self.col - 2),
        Position(self.rows + 2, self.col + 2)]
    
    def peut_manger(self, grille):
        positions_saut = self.Quatre_position_sauter()
        for position_saut in positions_saut:
            self.position.rows, self.position.col = position_saut.rows,position_saut.col
            if 0<= self.position.rows <len (grille) and 0<= self.position.col < len(grille[0]):
                piece_a_manger = grille[self.position.rows][self.position.col]
                if isinstance(piece_a_manger, Pion_bleu):
                    self.pions_mangeables.append(piece_a_manger)
        return self.pions_mangeables



    # Cette méthode spéciale compare deux instances d'une classe
    # ayant la même valeur et renvoie la valeur booléenne.
    def __eq__(sefl,other):
        return sefl.position == other.position
                    
    def __repr__(self):
        return "({},{})".format(self.position)
    
    def deplacer_pion_noir(self, direction):
        if direction == "avant":
            self.position.rows -= 1,
        elif direction == "diagonale_gauche":
            self.position.rows -= 1
            self.position.col -= 1
        elif direction == "diagonale_droite":
            self.position.rows -= 1
            self.position.col += 1
        
    def promouvoir_en_dame(self, pion):
        # Vérifier si le pion atteint la rangée la plus éloignée
        if self.position.rows <= 0:
            # Remplacer le pion par une dame
            nouvelle_dame = Dame_noire(self.position.rows, self.position.col)
            return(nouvelle_dame)
        else:
            None # Aucune promotion en dame n'est effectuée


    