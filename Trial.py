from tkinter import *

from PIL import Image, ImageTk

t = Tk()

t.geometry("1000x800")

img1 = ImageTk.PhotoImage(Image.open("h_a_img/h_a_1.png"))
img2 = ImageTk.PhotoImage(Image.open("h_a_img/h_a_2.jpg"))

l = Label(t, font="bold")
l.pack()

x = 1


def move():
    global x
    if x == 3:
        x = 1
    if x == 1:
        l.config(image=img1)
    elif x == 2:
        l.config(image=img2)

    x += 1
    t.after(700, move)


move()

t.mainloop()
