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

def dislpay:
fen = Tk()
canvas = Canvas(fen, width=500, height=500, background='white')
for i in range (100):
    x = random.randint(0,500)
    y = random.randint(0,500)
    if p.guess(x,y) == 1:
        color = 'red'
    else:
        color = 'blue'
    point = canvas.create_oval(x-3, y-3, x+3, y+3, fill=color)
line = canvas.create_line(-100,400,600,200)
canvas.pack()
fen.mainloop()
