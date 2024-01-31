class Position:
    def __init__(self, rows, col):
        self.board = []
        self.rows = rows
        self.col = col
    # Le joueur ne peut revenir en arriere 
    # uniquement lorsqu'il doit manger un pion adverse
    def position_diagonal_lower (self):
        return [Position(self.rows + 1, self.col -1), 
        Position(self.rows + 1, self.col + 1)]

    def position_diagonal_top(sefl):
        return [Position(sefl.rows - 1, sefl.col - 1), 
        Position(sefl.rows - 1, sefl.col + 1)]
    
    def four_position_diagonal (self):
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

    def prendre_piece(self, rows, col):
        return self.board[rows][col]
        

    
    # Cette méthode spéciale compare deux instances d'une classe
    # ayant la même valeur et renvoie la valeur booléenne.
    def __eq__(sefl,other):
        return sefl.rows == other.rows and sefl.col == other.col
                    
    def __repr__(self):
        return "({},{})".format(self.rows,self.col)
 
        