# TetrisAgent.py
from GameBoard import *
from TetrisPiece import *

class TetrisAgent:
    def __init__(self, name="Player", c=None):
        self.name = name
        self.game_board = GameBoard()
        self.total_score = 0
        self._chromosome = c
        self._current_piece = None
        self._round_counter = 0
        self.game_over = False
        
    def set_current_piece(self, piece):
        self._current_piece = piece
        
    def is_game_over(self):
        if self.game_board.game_over:
            return True
        max_height = self.game_board.height - 1
        for y in range(2):
            for x in range(self.game_board.width):
                if (self.game_board.board[max_height - y][x] > 0):
                    return True
        return False
        
    def state_value(self):
        """ Evaluates the current state based on provided weights """
        val = self._chromosome.occupied_weight * self.game_board.occupied_cells()
        val += self._chromosome.num_holes_weight * self.game_board.num_holes()
        val += self._chromosome.pile_height_weight * self.game_board.pile_height()
        val += self._chromosome.well_heights_weight * self.game_board.sum_well_heights()
        val += self._chromosome.completed_rows_weight * self.game_board.num_completed_rows()
        return val

    def random_move(self):
        """ For testing, returns a random move ignoring value """
        # choose a random rotation
        r = random.randint(0,3)
        self._current_piece.rotate(r)
        # choose a random column
        c = self.get_random_col()
        if c is None:
            self.game_over = True
        # put the piece there
        self.drop()
        self.place_current_piece()
        self._current_piece = None
        return
        
    def get_random_col(self):
        """ Returns a random column to put piece in (testing only) """
        # print("get random col for piece at: ({},{})".format(self._current_piece.location[0], self._current_piece.location[1]))
        tried = [0 for i in range(self.game_board.width)]
        # print(tried)
        c = random.randint(0, self.game_board.width-1)
        # print("c = {}".format(c))
        tried[c] = 1
        self._current_piece.move_to_col(c)
        
        while not self.in_range():
            if sum(tried) >= self.game_board.width:
                print("*** Tried all columns, could not place piece {} ***".format(self._current_piece.type))
                # print("piece loc: ({},{})".format(self._current_piece.location[0], self._current_piece.location[1]))
                return None
            c = random.randint(0, self.game_board.width-1)
            # print("\ttrying another c = {}".format(c))
            if tried[c] > 0:
                continue
            else:
                tried[c] = 1
            self._current_piece.move_to_col(c)
        # print("get_random_col returning {}".format(c))
        return c
        
    def place_current_piece(self):
        offset_x = self._current_piece.location[0]
        offset_y = self._current_piece.location[1]
        for x,y in self._current_piece.shape:
            self.game_board.board[y + offset_y][x + offset_x] = 1
        self._current_piece = None
            
    def drop(self):
        """ Drops piece to bottom of board """
        while(self.is_legal_position()):
            self._current_piece.location = (self._current_piece.location[0], self._current_piece.location[1] - 1)
        self._current_piece.location = (self._current_piece.location[0], self._current_piece.location[1] + 1)

    def is_legal_position(self):
        """ Returns True if the piece can be placed on the board """
        if not self.in_range():
            return False  # out of bounds
            
        offset_x = self._current_piece.location[0]
        offset_y = self._current_piece.location[1]
        for x,y in self._current_piece.shape:
            if self.game_board.board[y + offset_y][x + offset_x] > 0:
                return False # collision
        return True

    def in_range(self):
        offset_x = self._current_piece.location[0]
        offset_y = self._current_piece.location[1]
        for x,y in self._current_piece.shape:
            new_x = x + offset_x
            new_y = y + offset_y
            if (new_x >= self.game_board.width) or (new_x < 0) or (new_y < 0):
                # print("({},{}) out of range".format(new_x, new_y))
                return False
        return True
        
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
        s = self.game_board.clear_completed_rows()
        if s > 0:
            s = (s - 1) * 3
            self.total_score += s
        return s
        
    def vs(self, opponentScore):
        """ Updates board based on opponent score """
        lines = int(opponentScore / 3)
        while lines > 0:
            self.game_board.add_garbage_row()
        return

if __name__ == "__main__":
    a = TetrisAgent()
    piece = TetrisPiece("L")
    a.set_current_piece(piece)
    print(piece.location)
    print("({},{})".format(piece.location[0], piece.location[1]))
    a.place_current_piece()
    # a.random_move()
    print(a.game_board)
