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
        self._shape = tetriminos.get(type)[0]
        self._rotation = 0
        self._location = (20, 3)

    def __repr__(self):
        repr = "\n"
        tmp = [[0 for j in range(4)] for i in range(4)]
        for x,y in self._shape:
            tmp[y+2][x] = 1
        for i in reversed(range(4)):
            repr += "{}\n".format(tmp[i])
        return repr

    def rotate(self):
        """ Rotates piece 90 degrees """
        x = (self._rotation + 1) % 4
        self._shape = tetriminos.get(self._type)[x]
        self._rotation = x
        return

    def drop(self, board):
        """ Drops piece to bottom of board """
        return

    def is_legal_position(self, board):
        """ Returns True if the piece can be placed on the board """
        return False

    def move_left(self, board):
        """ Moves the piece left one square """
        return

    def move_right(self, board):
        """ Moves the piece right one square """
        return


if __name__ == "__main__":
    pieceL = TetrisPiece("L")
    print(pieceL)

    # pieceL.rotate()
    # print(pieceL)
    #
    # pieceL.rotate()
    # print(pieceL)
    #
    # pieceL.rotate()
    # print(pieceL)
    #
    # pieceL.rotate()
    # print(pieceL)

    pieceI = TetrisPiece("I")
    print(pieceI)

    pieceO = TetrisPiece("O")
    print(pieceO)
