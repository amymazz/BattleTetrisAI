# TetrisPiece.py
from GameBoard import *

tetriminos = {
    "O": [[(1,0), (2,0), (1,1), (2,1)],
          [(1,0), (2,0), (1,1), (2,1)],
          [(1,0), (2,0), (1,1), (2,1)],
          [(1,0), (2,0), (1,1), (2,1)]],
    "I": [[(0,0), (1,0), (2,0), (3,0)],
          [(2,-2), (2,-1), (2,0), (2,1)],
          [(0,-1), (1,-1), (2,-1), (3,-1)],
          [(1,-2), (1,-1), (1,0), (1,1)]],
    "T": [[(0,0), (1,0), (2,0), (1,1)],
          [(1,-1), (1,0), (1,1), (2,0)],
          [(0,0), (1,0), (2,0), (1,-1)],
          [(0,0), (1,0), (1,1), (1,-1)]],
    "L": [[(0,0), (1,0), (2,0), (2,1)],
          [(1,1), (1,0), (1,-1), (2,-1)],
          [(0,0), (1,0), (2,0), (0,-1)],
          [(1,1), (1,0), (1,-1), (0,1)]],
    "J": [[(0,1), (0,0), (1,0), (2,0)],
          [(1,1), (1,0), (1,-1), (2,1)],
          [(0,0), (1,0), (2,0), (2,-1)],
          [(1,1), (1,0), (1,-1), (0,-1)]],
    "S": [[(0,0), (1,0), (1,1), (2,1)],
          [(1,1), (1,0), (2,0), (2,-1)],
          [(0,-1), (1,-1), (1,0), (2,0)],
          [(0,1), (0,0), (1,0), (1,-1)]],
    "Z": [[(0,1), (1,0), (1,1), (2,0)],
          [(1,-1), (1,0), (2,0), (2,1)],
          [(0,0), (1,0), (1,-1), (2,-1)],
          [(1,1), (1,0), (0,0), (0,-1)]]
}

class TetrisPiece:
    def __init__(self, type):
        self._type = type
        self.shape = tetriminos.get(type)[0]
        self._rotation = 0
        self.location = (3, 19)

    def __repr__(self):
        repr = "\n"
        tmp = [[0 for j in range(4)] for i in range(4)]
        for x,y in self.shape:
            tmp[y+2][x] = 1
        for i in reversed(range(4)):
            repr += "{}\n".format(tmp[i])
        return repr

    def rotate(self, r):
        """ Rotates piece 90 degrees """
        for i in range(r):
            x = (self._rotation + 1) % 4
            self.shape = tetriminos.get(self._type)[x]
            self._rotation = x
        return

    def drop(self, board):
        """ Drops piece to bottom of board """
        while(self.is_legal_position(board)):
            self.location = (self.location[0], self.location[1] - 1)
        self.location = (self.location[0], self.location[1] + 1)

    def is_legal_position(self, board):
        """ Returns True if the piece can be placed on the board """
        if not self.in_range(board):
            return False  # out of bounds
            
        offset_x = self.location[0]
        offset_y = self.location[1]
        for x,y in self.shape:
            if board.board[y + offset_y][x + offset_x] > 0:
                return False # collision
        return True

    def in_range(self, board):
        offset_x = self.location[0]
        offset_y = self.location[1]
        for x,y in self.shape:
            new_x = x + offset_x
            new_y = y + offset_y
            if (new_x >= board.width) or (new_x < 0) or (new_y < 0):
                return False
        return True

    def move_to_col(self, col):
        """ Moves the piece to specified column """
        self.location = (col, self.location[1])
        
def get_random_piece():
    r = random.randint(0,6)
    x = ["O", "I", "T", "L", "J", "S", "Z"][r]
    print("Piece: " + x)
    return TetrisPiece(x)


if __name__ == "__main__":
    pieceL = TetrisPiece("L")
    print(pieceL)

    # pieceL.rotate(1)
    # print(pieceL)
    #
    # pieceL.rotate(1)
    # print(pieceL)
    #
    # pieceL.rotate(1)
    # print(pieceL)
    #
    # pieceL.rotate(1)
    # print(pieceL)

    pieceI = TetrisPiece("I")
    print(pieceI)

    pieceO = TetrisPiece("O")
    print(pieceO)
