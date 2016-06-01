# Adapted from
# https://www.daniweb.com/programming/software-development/code/216550/tkinter-to-put-a-gif-image-on-a-canvas-python
import time

from tkinter import *

import time
from threading import Thread

root = Tk()

frame = Frame(root)
frame.pack()


# create the canvas, size in pixels
canvas = Canvas(frame, width=500, height=320, bd=0, highlightthickness=0)

canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'maletasilvio.gif')
gif2 = PhotoImage(file='maletasilvio.gif', format="gif -index 2")

def animate():
    while(True):
        canvas.create_image(0, 0, image = gif1, anchor = NW)
        root.update()
        time.sleep(0.1)
        canvas.create_image(0, 0, image = gif2, anchor = NW)
        root.update()
        time.sleep(0.1)
        print("*")


t = Thread(target=animate)
t.start()

mainloop()

