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
    app = GameWindow(root)
    
    a1 = TetrisAgent("1", GAIndividual(occupied=0, holes=-0.65, pile=-0.10, wells=-0.20, completed=0.30)) # colin fahey weights
    # a2 = TetrisAgent("2", GAIndividual())
    a2 = TetrisAgent("2", random_individual())
    pieces = ["O", "I", "T", "L", "J", "S", "Z"]
    i = 0
    
    while True:
        if i < 50:
            p = pieces[random.randint(0,6)]
            
            a1.set_current_piece(TetrisPiece(p))
            a1.best_move()
            # a1.random_move()
            # a1.cheat(3)
            
            a2.set_current_piece(TetrisPiece(p))
            a2.random_move()
            
            app.draw_game(a1.game_board, a2.game_board)
            root.update_idletasks()
            root.update()
            time.sleep(0.5)
            
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
            
            i += 1
        
        app.draw_game(a1.game_board, a2.game_board)
        root.update_idletasks()
        root.update()
        time.sleep(0.25)
    
    return
    
    
if __name__ == "__main__":
    show()
    # test()
