# GameBoard.py

class GameBoard:
    def __init__(self):
        self._width = 10
        self._height = 20
        self._board = [[0 for j in range(self._width)] for i in range(self._height)]
        self._total_cells = self._width * self._height
        self._completed_rows = []  # marks rows that can be removed

    def __repr__(self):
        repr = "\n"
        for x in reversed(range(self._height)):
            repr += "{}\n".format(self._board[x])
        return repr

    def occupied_cells(self):
        """ Returns the number of occupied cells on the board """
        occupied = 0
        for y in range(self._height):
            for x in range(self._width):
                if self._board[y][x] > 0:
                    occupied += 1
        return occupied

    def num_holes(self):
        """ Returns the number of buried empty spaces on the board """
        holes = 0

        for x in range(self._width):
            # find first block in this column:
            y = self._height - 1
            while y > 0 and self._board[y][x] == 0:
                y -= 1

            # count holes
            y -= 1
            while y >= 0:
                if self._board[y][x] == 0:
                    holes += 1
                y -= 1

        return holes

    def pile_height(self):
        """ Returns the tallest height of pieces on the board """
        for y in reversed(range(self._height)):
            for x in range(self._width):
                if self._board[y][x] > 0:
                    return y+1
        return 0

    def sum_well_heights(self):
        return 0

    def num_completed_rows(self):
        """ Returns the number of completed (full) rows """
        completed = 0

        for y in range(self._height):
            x = 0
            while x < self._width and self._board[y][x] == 1:
                x += 1
            if x == self._width:
                completed += 1
                self._completed_rows.append(y)

        return completed

    def clear_rows(self):
        """ Clears completed rows and moves everything above down """
        for row in self._completed_rows:
            self._board.pop(row)
            self._board.append([0 for j in range(self._width)])
        self._completed_rows = []

    def temp_add_piece(self, piece):
        """ Function to add arbitrary pieces to the board, for testing only """
        for x,y in piece:
            self._board[y][x] = 1

if __name__ == '__main__':
    tetrisBoard = GameBoard()

    tetrisBoard.temp_add_piece([(0,0), (1,0), (0,1), (1,1)])
    tetrisBoard.temp_add_piece([(2,0), (2,1), (2,2), (3,1)])

    print("Current board: {}".format(tetrisBoard))

    print("Occupied cells: {}".format(tetrisBoard.occupied_cells()))
    print("Pile Height: {}".format(tetrisBoard.pile_height()))
    print("Holes: {}".format(tetrisBoard.num_holes()))
    tetrisBoard.clear_rows() # this should not error

    tetrisBoard.temp_add_piece([(3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0)])
    print("Completed Rows: {}".format(tetrisBoard.num_completed_rows()))
    tetrisBoard.clear_rows()
    print(tetrisBoard)
