# TetrisPiece.py
from GameBoard import *

class TetrisPiece:
    def __init__(self, type):
        pieces = {
            "O": [(1,0), (2,0), (1,1), (2,1)],
            "I": [(0,0), (1,0), (2,0), (3,0)],
            "T": [(0,0), (1,0), (2,0), (1,1)],
            "L": [(0,0), (1,0), (2,0), (2,1)],
            "J": [(0,1), (0,0), (1,0), (2,0)],
            "S": [(0,0), (1,0), (1,1), (2,1)],
            "Z": [(0,1), (1,0), (1,1), (2,0)]
        }
        self.shape = pieces.get(type)
        self.location = (20, 3)

    def __repr__(self):
        repr = "\n"
        tmp = [[0 for j in range(4)] for i in range(2)]
        for x,y in self.shape:
            tmp[y][x] = 1
        for i in reversed(range(2)):
            repr += "{}\n".format(tmp[i])
        return repr

    def rotate(self):
        return

    def drop(self, board):
        return

    def is_legal_position(self, board):
        return False

    def move_left(self, board):
        return

    def move_right(self, board):
        return


if __name__ == "__main__":
    pieceL = TetrisPiece("L")
    print(pieceL)

    pieceI = TetrisPiece("I")
    print(pieceI)

    pieceO = TetrisPiece("O")
    print(pieceO)
