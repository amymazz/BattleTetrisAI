# GameBoard.py
import random

color = ["gray", "#fff600","#00e9ff", "#c300ff", "#ffa500",
         "#4004e5", "#00cc00", "#e50b0b", "magenta"]
         
class GameBoard:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.width = 10
        self.height = 22
        self.board = [[0 for j in range(self.width)] for i in range(self.height)]
        self.total_cells = self.width * self.height
        self.completed_rows = []  # marks rows that can be removed
        self.double_hole = False  # for adding garbage lines
        self.game_over = False  # set if blocks pushed over the top

    def __repr__(self):
        repr = "\n"
        repr += "{}\n".format(self.board[self.height-1])
        repr += "{}\n".format(self.board[self.height-2])
        repr += "------------------------------------\n"
        for x in reversed(range(self.height-2)):
            repr += "{}\n".format(self.board[x])
        return repr

    def occupied_cells(self):
        """ Returns the number of occupied cells on the board """
        occupied = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] > 0:
                    occupied += 1
        return occupied

    def num_holes(self):
        """ Returns the number of buried empty spaces on the board """
        holes = 0

        for x in range(self.width):
            # find first block in this column:
            y = self.height - 1
            while y > 0 and self.board[y][x] == 0:
                y -= 1

            # count holes
            y -= 1
            while y >= 0:
                if self.board[y][x] == 0:
                    holes += 1
                y -= 1

        return holes

    def pile_height(self):
        """ Returns the tallest height of pieces on the board """
        for y in reversed(range(self.height)):
            for x in range(self.width):
                if self.board[y][x] > 0:
                    return y+1
        return 0

    def col_height(self, c):
        for j in reversed(range(self.height)):
            if self.board[j][c] > 0:
                return j + 1
        return 0

    def sum_well_heights(self):
        sum_heights = 0
        for i in range(self.width - 1):
            sum_heights += abs(self.col_height(i) - self.col_height(i + 1))
        return sum_heights

    def num_completed_rows(self):
        """ Returns the number of completed (full) rows """
        completed = 0

        for y in range(self.height):
            x = 0
            while x < self.width and self.board[y][x] > 0:
                x += 1
            if x == self.width:
                completed += 1
                self.completed_rows.append(y)  # save the row numbers that have been completed
        return completed

    def clear_completed_rows(self):
        """ Clears completed rows and moves everything above down """
        r = self.num_completed_rows()
        
        counter = 0  # offset once we remove rows
        for row in self.completed_rows:  # completed_rows is ordered from smallest index to largest
            self.board.pop(row - counter)
            counter += 1
            self.board.append([0 for j in range(self.width)])
        self.completed_rows = []
        return r

    def add_garbage_row(self):
        """ Adds garbage row from opponent """
        newRow = [8 for j in range(self.width)]

        h = [ None, None ]
        for i in range(len(h)):
            if h[0] is None:
                h[0] = random.randint(0, self.width-1)
                newRow[h[0]] = 0
            elif self.double_hole:
                h[1] = h[0]
                while h[1] == h[0]:
                    h[1] = random.randint(0, self.width-1)
                newRow[h[1]] = 0
        
        # find the first row above unbreakable blocks
        bottom_row = 0
        for i in range(self.height):
            if self.board[i][0] != -1:
                bottom_row = i
                break
        
        self.board = self.board[:bottom_row] + [newRow] + self.board[bottom_row:]
        self.double_hole = False if self.double_hole else True
        top = self.board.pop()

        # check if this made us lose
        for i in range(self.width):  # check if a block was pushed over the top
            if self.board[self.height-3][i] > 0:
                self.game_over = True
                
    def add_wall(self):
        """ Adds an unbreakable line to the bottom of the board """
        newRow = [-1 for j in range(self.width)]
        self.board = [newRow] + self.board
        top = self.board.pop()
        return
        
    def get_color(self, row, col):
        id = self.board[row][col]
        if id == -1:
            return "black"
        else:
            return color[id]
            
    def is_legal_position(self, piece):
        """ Returns True if the piece can be placed on the board """
        if not self.in_range(piece):
            return False  # out of bounds
            
        offset_x = piece.location[0]
        offset_y = piece.location[1]
        for x,y in piece.shape:
            if (self.board[y + offset_y][x + offset_x] > 0) or (self.board[y + offset_y][x + offset_x] == -1):
                return False # collision
        return True

    def in_range(self, piece):
        """ Returns true if the piece is within the board boundaries """
        offset_x = piece.location[0]
        offset_y = piece.location[1]
        for x,y in piece.shape:
            new_x = x + offset_x
            new_y = y + offset_y
            if (new_x >= self.width) or (new_x < 0) or (new_y < 0):
                # print("({},{}) out of range".format(new_x, new_y))
                return False
        return True
            
    def place_piece(self, piece):
        """ Place given piece on board """
        offset_x = piece.location[0]
        offset_y = piece.location[1]
        for x,y in piece.shape:
            self.board[y + offset_y][x + offset_x] = piece.id
            
    def drop_piece(self, piece):
        """ Drops piece to bottom of board """
        while(self.is_legal_position(piece)):
            piece.location = (piece.location[0], piece.location[1] - 1)
        piece.location = (piece.location[0], piece.location[1] + 1)

    def temp_add_piece(self, piece, value=1):
        """ Function to add arbitrary pieces to the board, for testing only """
        for x,y in piece:
            self.board[y][x] = value

if __name__ == '__main__':
    # Tests!

    tetrisBoard = GameBoard()

    tetrisBoard.temp_add_piece([(0,0), (1,0), (0,1), (1,1)])
    tetrisBoard.temp_add_piece([(2,0), (2,1), (2,2), (3,1)])

    print("Current board: {}".format(tetrisBoard))

    print("Occupied cells: {}".format(tetrisBoard.occupied_cells()))
    print("Pile Height: {}".format(tetrisBoard.pile_height()))
    print("Holes: {}".format(tetrisBoard.num_holes()))
    print("Sum Well Heights: {}".format(tetrisBoard.sum_well_heights()))
    tetrisBoard.clear_completed_rows() # this should not error

    tetrisBoard.temp_add_piece([(3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0)])
    print("Completed Rows: {}".format(tetrisBoard.num_completed_rows()))
    tetrisBoard.clear_completed_rows()
    print(tetrisBoard)

    tetrisBoard.add_garbage_row()
    tetrisBoard.add_garbage_row()
    tetrisBoard.add_garbage_row()
    print(tetrisBoard)
    print("Column 2 height: {}".format(tetrisBoard.col_height(2)))
    print("Column 9 height: {}".format(tetrisBoard.col_height(9)))

    tetrisBoard.reset()
    tetrisBoard.add_wall()
    tetrisBoard.add_garbage_row()
    tetrisBoard.add_wall()
    tetrisBoard.add_garbage_row()
    print(tetrisBoard)
    
    tetrisBoard.reset()
    tetrisBoard.temp_add_piece([(0,0), (1,0), (2,0), (3,0), (5,0), (6,0), (7,0), (8,0), (9,0)], 8)
    tetrisBoard.temp_add_piece([(4,0)], 3)
    print(tetrisBoard)
    tetrisBoard.clear_completed_rows()
    print(tetrisBoard)
