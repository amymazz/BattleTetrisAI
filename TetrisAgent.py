# TetrisAgent.py
from GameBoard import *
from TetrisPiece import *

class TetrisAgent:
    def __init__(self):
        self._field = GameBoard()
        self._current_piece = None
        self.garbage_lines = 0

    def random_move(self):
        return

if __name__ == "__main__":
    a = TetrisAgent()
