#Import all module inside tkinter
from tkinter import *

#import pillow module and related module like
from PIL import Image,ImageTk

#create a tkinter window
t=Tk()


#Create a size for tkinter window
t.geometry("400x600")#here use alphabet 'x' not '*' this one

#now set an image for moving
img1=ImageTk.PhotoImage(Image.open("h_a_img/h_a_1.png"))#make sure that you have a photo
#in you current folder that you are working with
img2=ImageTk.PhotoImage(Image.open("h_a_img/h_a_2.jpg"))

#Create a label
l=Label(t,font="bold")
l.pack()
#take a variable
x=1
#create a function for moving a picture
def move():#name anything but meaningful
    global x
    if x==4:
        x=1
    if x==1:
        l.config(image=img1)#by writing this line first picture will appear
    elif x==2:
        l.config(image=img2)

    #you can do it for thousands of images
    #now increase the count by one
    x+=1
    #set images to work automatically by "after" feature in tkinter
    t.after(1000,move)
#Call the function
move()

t.mainloop()

