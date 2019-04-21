# Visualizer.py

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.master.title("Battle Tetris")
        
    def draw_thing(self):
        Frame(self.master, bg="blue", height="20", width="20").grid(row=0, column=0, sticky=W+E+N+S)
        Frame(self.master, bg="red", height="20", width="20").grid(row=1, column=1, sticky=W+E+N+S)

def show():
    root = Tk()
    app = Window(root)
    app.draw_thing()

    root.mainloop()
    return
    
def update():
    Frame(self.master, bg="purple", height="20", width="20").grid(row=0, column=0, sticky=W+E+N+S)
    Frame(self.master, bg="green", height="20", width="20").grid(row=1, column=1, sticky=W+E+N+S)
    
if __name__ == "__main__":
    show()
