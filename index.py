from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql



class appscreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Moodz")
        self.root.geometry('650x750+500+0')
        self.root.resizable(False, False)
        self.root['bg'] = 'white'
        self.appscreen()



    def appscreen(self):
        Frame_login = Frame(self.root, bg="white")

        Frame_login.place(x=0, y=0, height=700, width=1366)

        label1 = Label(
            Frame_login,
            text="Hi! Welcome to MOODZ",
            font=("times new roman", 32, "bold"),
            fg="black",
            bg="white",
        )

        label1.place(x=60, y=100)

        label2 = Label(
            Frame_login,
            text="This is a safe space for you to \n express and understand your\n emotions",
            font=("times new roman", 32, "bold"),
            fg="black",
            bg="white",
        )

        label2.place(x=40, y=160)

        label3 = Label(
            Frame_login,
            text="App is under development",
            font=("times new roman", 32, "bold"),
            fg="black",
            bg="white",
        )

        label3.place(x=60, y=400)

        btn2 = Button(
            Frame_login,
            text="Logout",
            command = self.login_page,
            cursor="hand2",
            font=("times new roman", 15),
            fg="white",
            bg="orangered",
            bd=0,
            width=15,
            height=1,
        )

        btn2.place(x=460, y=10)

    def login_page(self):
        root.destroy()
        import login_page

root = Tk()
ob = appscreen(root)
root.mainloop()