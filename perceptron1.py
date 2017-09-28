from tkinter import *
import random

class perceptron:
    def __init__(self):
        self.wx = 1
        self.wy = -1
    def guess(self,x,y):
        if x*self.wx + y*self.wy > 0:
            return 1
        else:
            return -1
        
p = perceptron()

fen = Tk()
canvas = Canvas(fen, width=500, height=500, background='white')
for i in range (50):
    x = random.randint(0,500)
    y = random.randint(0,500)
    if p.guess(x,y) == 1:
        color = 'red'
    else:
        color = 'blue'
    point = canvas.create_oval(x-3, y-3, x+3, y+3, fill=color)
line = canvas.create_line(-100,150,600,400)
canvas.pack()
fen.mainloop()
