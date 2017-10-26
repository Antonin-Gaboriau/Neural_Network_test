from tkinter import *
import random
import time

class Perceptron:
    def __init__(self):
        self.wx = 1
        self.wy = 1
        self.lr = 0.0001
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

class Line:
    def __init__(self):
        self.slope = (random.random()) * 4
    def function (self, x):
        return self.slope * x 
    def test_side (self, x, y):
        if y > self.function(x):
            return +1
        else:
            return -1
        
def display(points, line, i, canvas):
    clear = canvas.create_rectangle(0,0,500,500, fill='white')
    for p in points:
        if line.test_side(p.x, p.y) == neuron.guess(p.x,p.y):
            color = 'green'
        else:
            color = 'red'
        if neuron.guess(p.x,p.y) == 1:
            point = canvas.create_oval(p.x-4, p.y-4, p.x+4, p.y+4, fill=color)
        else:
            point = canvas.create_rectangle(p.x-3, p.y-3, p.x+3, p.y+3, fill=color)
    separator = canvas.create_line(0,line.function(0),600,line.function(600))   

#main-------------------------------------------------------    
fen = Tk()
canvas = Canvas(fen, width=500, height=500, background='white')
canvas.pack()
neuron = Perceptron()
points = []
line = Line()
for i in range (200):
    p = Point()
    points.append(p)
for main_loop in range (50):
    display(points, line, main_loop, canvas)
    fen.update()
    time.sleep(1)
    for p in points:
        target = line.test_side(p.x,p.y)
        neuron.improve(p.x,p.y,target)
    print("test")
fen.mainloop()
