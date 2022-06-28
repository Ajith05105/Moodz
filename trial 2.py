from tkinter import *

from PIL import Image, ImageTk

t = Tk()

t.geometry("1000x800")

img1 = ImageTk.PhotoImage(Image.open("h_a_img/h_a_1.png"))
img2 = ImageTk.PhotoImage(Image.open("h_a_img/h_a_2.jpg"))

l = Label(t, font="bold")
l.pack()



t.mainloop()
