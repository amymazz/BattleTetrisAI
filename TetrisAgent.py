# TetrisAgent.py
from GameBoard import *
from TetrisPiece import *

class TetrisAgent:
    def __init__(self, name, c):
        self.name = name
        self.board = GameBoard()
        self.total_score = 0
        self._chromosome = c
        self._current_piece = None
        self._round_counter = 0
        
    def set_current_piece(self, piece):
        self._current_piece = piece
        
    def state_value(self):
        """ Evaluates the current state based on provided weights """
        val = self._chromosome.occupied_weight * self.board.occupied_cells()
        val += self._chromosome.num_holes_weight * self.board.num_holes()
        val += self._chromosome.pile_height_weight * self.board.pile_height()
        val += self._chromosome.well_heights_weight * self.board.sum_well_heights()
        val += self._chromosome.completed_rows_weight * self.board.num_completed_rows()
        return val

    def random_move(self):
        """ For testing, returns a random move ignoring value """
        # choose a random rotation
        r = random.randint(0,3)
        self._current_piece.rotate(r)
        # choose a random column
        c = self.board.get_random_col(self._current_piece)
        # put the piece there
        self._current_piece.drop(self.board)
        self.board.add_piece(self._current_piece)
        return
        
    def best_move(self):
        """ Returns the best move given the current piece """
        return

    def update(self):
        """ Updates field at end of round """
        if self._round_counter == 15:
            print("Round 15, adding solid line to bottom")
        return
        
    def score(self):
        """ Returns score """
        s = self.board.clear_completed_rows()
        if s > 0:
            s = (s - 1) * 3
            self.total_score += s
        return s
        
    def vs(self, opponentScore):
        """ Updates board based on opponent score """
        lines = int(opponentScore / 3)
        while lines > 0:
            self.board.add_garbage_row()
        return

if __name__ == "__main__":
    a = TetrisAgent()
    print(a.random_move())
