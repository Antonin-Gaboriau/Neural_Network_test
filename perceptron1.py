from tkinter import *
import random

import time

class Perceptron:
    def __init__(self):
        self.wx = 0.1
        self.wy = -50
        self.lr = 0.0005
    def guess(self,x,y):
        if x*self.wx + y*self.wy > 0:
            return 1
        else:
            return -1
    def improve(self,x,y,target):
        error = (target - self.guess(x,y)) * self.lr
        self.wx += error*x
        self.wy += error*y

class Point:
    def __init__(self):
        self.x = random.randint(0,500)
        self.y = random.randint(0,500)
        
def display(points, i, canvas):
    clear = canvas.create_rectangle(0,0,500,500, fill='white')
    for p in points:
        if neuron.guess(p.x,p.y) == 1:
            color = 'red'
        else:
            color = 'blue'
        point = canvas.create_oval(p.x-3, p.y-3, p.x+3, p.y+3, fill=color)
    line = canvas.create_line(0,0,500,1000)
    time.sleep(1)

#main-------------------------------------------------------    
fen = Tk()
canvas = Canvas(fen, width=500, height=500, background='white')
canvas.pack()
neuron = Perceptron()
points = []
for i in range (200):
    p = Point()
    points.append(p)
for i in range (50):
    display(points, i, canvas)
    fen.update()
    for p in points:
        if 2*p.x > p.y:
            target = 1
        else:
            target = -1
        neuron.improve(p.x,p.y,target)
fen.mainloop()
