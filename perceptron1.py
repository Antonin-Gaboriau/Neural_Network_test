from tkinter import *
import random

fen = Tk()

canvas = Canvas(fen, width=500, height=500, background='white')
for i in range (50):
    x = random.randint(0,500)
    y = random.randint(0,500)
    point = canvas.create_oval(x, y, x+5, y+5, fill='black')
line = canvas.create_line(-100,150,600,400)
    
canvas.pack()

fen.mainloop()
