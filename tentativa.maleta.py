# -*- coding: utf-8 -*-
__author__ = 'LuizJR'

import time

from tkinter import *

import time
from threading import Thread

root = Tk()

frame = Frame(root)
frame.pack()

current = 0

def animate_frame():
    canvas.delete("all")
    canvas.create_image(50 + current*2, 10, image = gifs[current], anchor = NW)
    root.update()
    time.sleep(0)
    print("+")
    global current
    current +=1
    current = current % len(gifs)
    canvas.after(50, animate_frame)


# create the canvas, size in pixels
canvas = Canvas(frame, width=500, height=200, bd=0, highlightthickness=0)

# pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)

# Load aniamted gifs
gifs = []
gifs.append(PhotoImage(file='maletasilvio.gif'))
gifs.append(PhotoImage(file='maletasilvio', format="gif -index 1"))
gifs.append(PhotoImage(file='maletasilvio', format="gif -index 2"))

# Inicia as chamadas recorrentes que fazem animação
animate_frame()

mainloop()