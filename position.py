class Position:
    def __init__(self, rows, col):
        self.board = []
        self.rows = rows
        self.col = col
    def position_diagonal_lower (self):
        return [Position(self.rows + 1, self.col -1), Position(self.rows + 1, self.col + 1)]

    def position_diagonal_top(sefl):
        return [Position(sefl.rows - 1, sefl.col - 1), Position(sefl.rows - 1, sefl.col + 1)]

    def four_position_diagonal (self):
        return[Position(self.rows - 1, self.col - 1),Position(self.rows - 1, self.col + 1),
               Position(self.rows + 1, self.col - 1),Position(self.rows + 1, self.col + 1)]

    def four_position_jumps (self):
        return[Position(self.rows - 2, self.col - 2),Position(self.rows - 2, self.col + 2),
               Position(self.rows + 2, self.col - 2),Position(self.rows + 2, self.col + 2)]

    def get_piece(self, rows, col):
        return self.board[rows][col]
        
    def create_board(self):
        for rows in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    # This special method compares two instances of a class with the same value and returns the boolean value
    def __eq__(sefl,other):
        return sefl.rows == other.rows and sefl.col == other.col
    # 
    def __rep__(self):
        return "({},{})".format(self.rows,self.col)
 
    # Unit testing
    if __name__ == '__main__':
        print("Test unitaires de la classe position")
        
    #unit testing   position_diagonal_lower
    position_1 = Position(0,1)
    assert Position(1,0).position_diagonal_Lower() == [Position(2,-1), Position(2,1)]
    assert Position(1, 1).position_diagonale_lower() == [Position(2, 0), Position(2, 2)]

               

        