# GameBoard.py

class GameBoard:
    def __init__(self):
        self.width = 10
        self.height = 20
        self.board = [[0]* self.width] * self.height

    def __repr__(self):
        repr = "\n"
        for x in range(self.height):
            repr += "{}\n".format(self.board[x])
        return repr

    def get_occupied_cells(self):
        return 0

    def get_num_holes(self):
        return 0

    def get_pile_height(self):
        return 0

    def get_sum_well_heights(self):
        return 0

if __name__ == '__main__':
    tetrisBoard = GameBoard()
    print("Current board: {}".format(tetrisBoard))
