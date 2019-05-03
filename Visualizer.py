# Visualizer.py

import time
import tkinter as tk
from TetrisAgent import *
from GA import *

class GameWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)               
        self.master = master
        self.master.title("Battle Tetris")
        self.frames = [[None for j in range(24)] for i in range(22)]
        self.sticky = tk.W+tk.E+tk.N+tk.S
        
        for row in range(22):
            for col in range(24):
                # TODO: don't draw frames on the border grids
                self.frames[row][col] = tk.Frame(self.master, bg="gray", bd="1", relief="solid", height="20", width="20")
                self.frames[row][col].grid(row=row, column=col, sticky=self.sticky)
                col += 1
            row += 1
        for row in [0,21]:
            for col in range(24):
                self.frames[row][col].config(bd="0")
        for col in [0, 11, 12, 23]:
            for row in range(22):
                self.frames[row][col].config(bd="0")
            
    def draw_game(self, board1, board2):
        offset_col_a = 1
        offset_col_b = 13
        
        bh = board1.height - 2
        
        for row in range(bh):
            for col in range(board1.width):
                self.frames[bh - row][col + offset_col_a].config(bg=board1.get_color(row, col))
                self.frames[bh - row][col + offset_col_b].config(bg=board2.get_color(row, col))
                col += 1
            row += 1
            col = 0
        
        offset_col = 15
        pass

def show():
    root = tk.Tk()
    root.geometry("+200+150")

    app = GameWindow(root)
    
    # a1 = TetrisAgent("bot", GAIndividual([0, -0.65, -0.10, -0.20, 0.30])) # fahey weights
    # [0.62, -0.96, 0.19, -0.26, 0.27]
    # [-0.44, -0.58, -0.10, -0.26, 0.71]
    # a1 = TetrisAgent("1", GAIndividual([0.99, -1.00, -0.11, -0.90, 0.59])) # pop=20, gen=5, mut=2%
    # a2 = TetrisAgent("amy", GAIndividual([0.62, -0.96, 0.19, -0.26, 0.27])) # pop=50, gen=5, mut=2%
    # a2 = TetrisAgent("amy", GAIndividual([-0.73, -0.92, -0.01, -0.19, 0.78])) # pop=50, gen=5, mut=10%
    # a2 = TetrisAgent("amy", GAIndividual([-0.91, -0.97, -0.24, -0.16, 0.88])) # pop=50, gen=5, mut=10%, 20% parents second best
    # a2 = TetrisAgent("amy2", GAIndividual([-0.44, -0.58, -0.10, -0.26, 0.71])) # pop=50, gen=10, mut=2%
    # a2 = TetrisAgent("amy", GAIndividual([-0.93, -0.96, -0.17, -0.01, 0.61])) # pop=80, gen=10, mut=5% best so far
    
    a1 = TetrisAgent("dumb", GAIndividual([-0.27, 0.81, 0.57, -0.55, 0.97]))
    a2 = TetrisAgent("dumber", GAIndividual([0.23, -0.71, -0.43, 0.72, 0.56])) # builds towers
    
    pieces = ["O", "I", "T", "L", "J", "S", "Z"]
    
    while True:
        p = pieces[random.randint(0,6)]
        
        a1.set_current_piece(TetrisPiece(p))
        a1.best_move()
        # a1.cheat(3)
        
        a2.set_current_piece(TetrisPiece(p))
        a2.best_move()
        
        app.draw_game(a1.game_board, a2.game_board)
        root.update_idletasks()
        root.update()
        time.sleep(0.1)
        
        a1_score = a1.score()
        a2_score = a2.score()
        
        a1.update(a2_score)
        a2.update(a1_score)
        
        if a1.is_game_over():
            print("{} wins with score {}!".format(a2.name, a2.total_score))
            break
        elif a2.is_game_over():
            print("{} wins with score {}!".format(a1.name, a1.total_score))
            break
        
        app.draw_game(a1.game_board, a2.game_board)
        root.update_idletasks()
        root.update()
        time.sleep(0.1)
    
    # print stats:
    print("\nGame Duration: {} Rounds".format(a1.round_counter))
    
    for a in [a1, a2]:
        print("{} Stats:".format(a.name))
        print("Final score: {}".format(a.total_score))
        print("Rows cleared: {}".format(a.rows_cleared))
        print("Lines sent: {}".format(a.lines_sent))
        print("")
    return
    
    
if __name__ == "__main__":
    show()
    # test()
