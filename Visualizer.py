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
        self.toggle = True
        self.sticky = tk.W+tk.E+tk.N+tk.S
        
        self.frame1 = tk.Frame(self.master, bg="blue", height="20", width="20")
        self.frame1.grid(row=0, column=0, sticky=self.sticky)
        self.frame2 = tk.Frame(self.master, bg="red", height="20", width="20")
        self.frame2.grid(row=1, column=1, sticky=self.sticky)
        
        rows = 0
        cols = 0
        while rows < 26:
            while cols < 22:
                self.master.columnconfigure(cols,weight=1)
                cols += 1
            self.master.rowconfigure(rows, weight=1)
            
            rows += 1
        
    def draw_thing(self):
        if self.toggle:
            self.toggle = False
            self.frame1.config(bg="purple")
            self.frame2.config(bg="green")
        else:
            self.toggle = True
            self.frame1.config(bg="blue")
            self.frame2.config(bg="red")

def show():
    root = tk.Tk()
    app = GameWindow(root)
    
    a1 = TetrisAgent("1", GA())
    a2 = TetrisAgent("2", GA())
    pieces = ["O", "I", "T", "L", "J", "S", "Z"]
    i = 0
    
    # root.mainloop()
    while True:
        if i < 10:
            p = pieces[random.randint(0,6)]
            a1.set_current_piece(TetrisPiece(p))
            a1.random_move()
        
        app.draw_thing(a1.game_board)
        root.update_idletasks()
        root.update()
    
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
    # show()
    test()
