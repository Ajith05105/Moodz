from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import bcrypt


class Register:

    def __init__(self,root):
        self.root = root
        self.root.title("register page")
        self.root.geometry('350x350+500+0')
        self.root['bg'] = 'white'
        self.root.resizable(False,False)
        self.images_list=[]

        self.Register()

    def creating_image(self, imgLoc, h,w, x, y):
        self.original = Image.open(f'img/{imgLoc}.png').resize((w, h), Image.ANTIALIAS)  # calling it all in one line
        self.photoimg = ImageTk.PhotoImage(self.original)
        self.label = Label(self.root, image = self.photoimg,bd=0)
        self.label.place(x=x,y=y)
        self.images_list.append(self.photoimg)
        return self.label


    def Register(self):
        img = self.creating_image('sad_emoji',100,100,100,100)
        img_2 = self.creating_image("meh_emoji",100,100,100,250)



root = Tk()
ob = Register(root)
root.mainloop()
