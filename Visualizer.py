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
        self.frames = [[None for j in range(26)] for i in range(22)]
        self.sticky = tk.W+tk.E+tk.N+tk.S
        
        for row in range(22):
            for col in range(26):
                # TODO: don't draw frames on the border grids
                self.frames[row][col] = tk.Frame(self.master, bg="gray", bd="1", relief="solid", height="20", width="20")
                self.frames[row][col].grid(row=row, column=col, sticky=self.sticky)
                col += 1
            row += 1
        
        # # for the test thing:
        # self.toggle = True
        # self.frame1 = tk.Frame(self.master, bg="blue", bd="2", relief="solid", height="20", width="20")
        # self.frame1.grid(row=0, column=0, sticky=self.sticky)
        # self.frame2 = tk.Frame(self.master, bg="red", bd="2", relief="solid", height="20", width="20")
        # self.frame2.grid(row=1, column=1, sticky=self.sticky)
        
    def draw_thing(self):
        if self.toggle:
            self.toggle = False
            self.frame1.config(bg="purple")
            self.frame2.config(bg="green")
        else:
            self.toggle = True
            self.frame1.config(bg="blue")
            self.frame2.config(bg="red")
            
    def draw_game(self, board1, board2):
        offset_row = 1
        offset_col = 1
        
        bh = board1.height - 2
        
        for row in range(bh):
            for col in range(board1.width):
                color = board1.get_color(row, col)
                self.frames[(bh - row) - offset_row][col + offset_col].config(bg=color) # this is upside down
                col += 1
            row += 1
            col = 0
        
        offset_col = 15
        pass

def show():
    root = tk.Tk()
    app = GameWindow(root)
    
    a1 = TetrisAgent("1", GA())
    a2 = TetrisAgent("2", GA())
    pieces = ["O", "I", "T", "L", "J", "S", "Z"]
    i = 0
    
    while True:
        if i < 5:
            p = pieces[random.randint(0,6)]
            a1.set_current_piece(TetrisPiece(p))
            a1.random_move()
            i += 1
        
        app.draw_game(a1.game_board, a2.game_board)
        root.update_idletasks()
        root.update()
        time.sleep(1)
    
    return
    
def test():
    root = tk.Tk()
    app = GameWindow(root)
    
    while True:
        app.draw_thing()
        root.update_idletasks()
        root.update()
        time.sleep(0.5)
    
if __name__ == "__main__":
    show()
    # test()
