# TetrisPiece.py
from GameBoard import *

tetriminos = {
    "O": [[(0,0), (0,1), (1,1), (1,0)],
          [(0,0), (0,1), (1,1), (1,0)],
          [(0,0), (0,1), (1,1), (1,0)],
          [(0,0), (0,1), (1,1), (1,0)]],
    "I": [[(-1,0), (0,0), (1,0), (2,0)],
          [(1,1), (1,0), (1,-1), (1,-2)],
          [(-1,-1), (0,-1), (1,-1), (2,-1)],
          [(0,1), (0,0), (0,-1), (0,-2)]],
    "T": [[(-1,0), (0,0), (0,1), (1,0)],
          [(0,0), (0,1), (0,-1), (1,0)],
          [(-1,0), (0,0), (1,0), (0,-1)],
          [(0,0), (0,1), (0,-1), (-1,0)]],
    "L": [[(-1,0), (0,0), (1,0), (1,1)],
          [(0,1), (0,0), (0,-1), (1,-1)],
          [(-1,-1), (-1,0), (0,0), (1,0)],
          [(-1,1), (0,1), (0,0), (0,-1)]],
    "J": [[(-1,1), (-1,0), (0,0), (1,0)],
          [(0,-1), (0,0), (0,1), (1,1)],
          [(-1,0), (0,0), (1,0), (1,-1)],
          [(0,1), (0,0), (0,-1), (-1,-1)]],
    "S": [[(-1,0), (0,0), (0,1), (1,1)],
          [(0,1), (0,0), (1,0), (1,-1)],
          [(-1,-1), (0,-1), (0,0), (1,0)],
          [(-1,1), (-1,0), (0,0), (0,-1)]],
    "Z": [[(-1,1), (0,1), (0,0), (1,0)],
          [(0,-1), (0,0), (1,0), (1,1)],
          [(-1,0), (0,0), (0,-1), (1,-1)],
          [(-1,-1), (-1,0), (0,0), (0,1)]],
    "cheat": [[(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0)]]
}

id = [None, "O", "I", "T", "L", "J", "S", "Z", "cheat"]

class TetrisPiece:
    def __init__(self, type):
        self.type = type
        self.id = id.index(type)
        self.shape = tetriminos.get(type)[0]
        self.rotation = 0
        self.location = (4, 18)

    def __repr__(self):
        repr = "\n"
        tmp = [[0 for j in range(4)] for i in range(4)]
        for x,y in self.shape:
            tmp[y+2][x+1] = 1
        for i in reversed(range(4)):
            repr += "{}\n".format(tmp[i])
        return repr

    def rotate(self, r):
        """ Rotates piece 90 degrees """
        for i in range(r):
            x = (self.rotation + 1) % 4
            self.shape = tetriminos.get(self.type)[x]
            self.rotation = x
        return

    def move_to_col(self, col):
        """ Moves the piece to specified column """
        y = self.location[1]
        self.location = (col, y)

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
