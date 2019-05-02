# TetrisAgent.py
import copy
from GameBoard import *
from TetrisPiece import *

class TetrisAgent:
    def __init__(self, name="Player", GA=None):
        self.name = name
        self.game_board = GameBoard()
        self.total_score = 0
        self.weights = GA
        self.current_piece = None
        self.round_counter = 0
        self.game_over = False
        
    def __repr__(self):
        return "{}: {}".format(self.name, self.weights)
        
    def set_current_piece(self, piece):
        self.current_piece = piece
        
    def is_game_over(self):
        if self.game_board.game_over:
            return True
        max_height = self.game_board.height - 1
        for y in range(2):
            for x in range(self.game_board.width):
                if (self.game_board.board[max_height - y][x] > 0):
                    return True
        return False
        
    def state_value(self, board):
        """ Evaluates the current state based on provided weights """
        val = self.weights.occupied_weight * board.occupied_cells()
        val += self.weights.num_holes_weight * board.num_holes()
        val += self.weights.pile_height_weight * board.pile_height()
        val += self.weights.well_heights_weight * board.sum_well_heights()
        val += self.weights.completed_rows_weight * board.num_completed_rows()
        return val
    
    def best_move(self):
        """ Executes the best move given the current piece """
        rotate = 0
        col = -1
        neg_inf = float("-inf")
        high_score = neg_inf
        
        for r in range(4):
            for c in range(self.game_board.width):
                temp_board = copy.deepcopy(self.game_board)
                temp_piece = copy.deepcopy(self.current_piece)
                
                temp_piece.rotate(r)
                temp_piece.move_to_col(c)
                
                if temp_board.is_legal_position(temp_piece):
                    temp_board.drop_piece(temp_piece)
                    temp_board.place_piece(temp_piece)
                    score = self.state_value(temp_board)
                    if score > high_score:
                        high_score = score
                        rotate = r
                        col = c
        if high_score == neg_inf:
            # no valid moves
            self.game_over = True
            return
                        
        self.current_piece.rotate(rotate)
        self.current_piece.move_to_col(col)
        self.game_board.drop_piece(self.current_piece)
        self.game_board.place_piece(self.current_piece)
        return
        
    def score(self):
        """ Returns score """
        s = self.game_board.clear_completed_rows()
        if s > 0:
            s = (s - 1) * 3
            self.total_score += s
        return s
        
    def update(self, opponentScore):
        """ Updates board based on opponent score """
        # add lines from opponent
        lines = int(opponentScore / 3)
        for i in range(lines):
            self.game_board.add_garbage_row()
        
        # add unbreakable lines every 15 rounds
        self.round_counter += 1
        if (self.round_counter % 15) == 0:
            self.game_board.add_wall()
        return
    
    """ Everything below here is for testing only """
    
    def cheat(self, count):
        """ Straight up cheats and places complete lines (for testing) """
        for i in range(count):
            self.set_current_piece(TetrisPiece("cheat"))
            self.current_piece.move_to_col(0)
            self.game_board.drop_piece(self.current_piece)
            self.game_board.place_piece(self.current_piece)

    def random_move(self):
        """ For testing, returns a random move ignoring value """
        # choose a random rotation
        r = random.randint(0,3)
        self.current_piece.rotate(r)
        # choose a random column
        c = self.get_random_col()
        if c is None:
            self.game_over = True
        # put the piece there
        self.game_board.drop_piece(self.current_piece)
        self.game_board.place_piece(self.current_piece)
        
    def get_random_col(self):
        """ Returns a random column to put piece in (testing only) """
        tried = [0 for i in range(self.game_board.width)]
        c = random.randint(0, self.game_board.width-1)
        tried[c] = 1
        self.current_piece.move_to_col(c)
        
        while not self.game_board.in_range(self.current_piece):
            if sum(tried) >= self.game_board.width:
                print("*** Tried all columns, could not place piece {} ***".format(self.current_piece.type))
                return None
            c = random.randint(0, self.game_board.width-1)
            if tried[c] > 0:
                continue
            else:
                tried[c] = 1
            self.current_piece.move_to_col(c)
        return c

if __name__ == "__main__":
    pass
