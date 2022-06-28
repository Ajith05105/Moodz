from tkinter import Tk, Frame, Menu, Canvas, PhotoImage
import easygui
from PIL import Image, ImageFilter, ImageTk

class App():
    def __init__(self):


def creating_image(a,w,h,x,y):
    global photoimg #keeping a reference

    original = Image.open(a).resize((w, h), Image.ANTIALIAS) #calling it all in one line
    photoimg = ImageTk.PhotoImage(original)
    canvas = Canvas(root, width=799, height=799)
    imagesprite = canvas.create_image(10, 10,anchor='nw', image=photoimg)
    canvas.place(x=x,y=y)
    print("in image")
    return imagesprite

root = Tk()
ob = Register(root)
root.mainloop()
