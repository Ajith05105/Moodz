from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

import pymysql




class Login:
    def __init__(self, root):

        self.root = root

        self.root.title("Login page")

        self.root.geometry("650x750+500+0")

        self.root.resizable(False, False)

        self.loginform()



    def loginform(self):

        def creating_image(a, w, h, x, y):
            global photoimg  # keeping a reference

            self.original = Image.open(a).resize((w, h), Image.ANTIALIAS)  # calling it all in one line
            self.photoimg = ImageTk.PhotoImage(self.original)
            self.canvas = Label(self.root, image=self.photoimg,bg='white')

            self.canvas.place(x=x, y=y)
            return self.canvas

        Frame_login = Frame(self.root, bg="white")

        Frame_login.place(x=0, y=0, height=750, width=750)

        frame_input = Frame(self.root, bg="white")

        frame_input.place(x=30, y=150, height=600, width=350)

        self.logo = ImageTk.PhotoImage(file="img/register_logo.png")

        logo = Label(self.root, image=self.logo, bd='0').place(x=15, y=-15)

        creating_image('img/entry_img.png',320,50,50,295)

        self.entry_img_2 = Image.open('img/entry_img_2.png')
        self.entry_img_resized_2 = self.entry_img_2.resize((320, 50))
        self.new_entry_img_2 = ImageTk.PhotoImage(self.entry_img_resized_2)
        new_entry_img_2 = Label(frame_input, image=self.new_entry_img_2, bd=0)
        new_entry_img_2.place(x=20, y=240)

        self.side_bar = Image.open('img/side_bar_register_page.png')
        self.side_bar_resized = self.side_bar.resize((310, 750))
        self.new_side_bar = ImageTk.PhotoImage(self.side_bar_resized)

        self.login = Image.open('img/login.png')
        self.login_resized = self.login.resize((330, 115))
        self.new_login = ImageTk.PhotoImage(self.login_resized)

        label1 = Label(
            Frame_login,
            image=self.new_side_bar
        )

        label1.place(x=390, y=0)

        label2 = Label(
            frame_input,
            text="Username",
            font=("Bauhaus 93", 20),
            fg="black",
            bg="white",
        )

        label2.place(x=25, y=100)

        self.username = Entry(
            frame_input, font=("times new roman", 15,), bg="white", bd=0
        )

        self.username.place(x=30, y=145, width=300, height=33)

        label3 = Label(
            frame_input,
            text="Password",
            font=("Bauhaus 93", 20),
            fg="black",
            bg="white",
        )

        label3.place(x=25, y=200)

        self.password = Entry(
            frame_input, font=("times new roman", 15, "bold"), bg="white", bd=0
        )

        self.password.place(x=30, y=245, width=300, height=35)

        btn2 = Button(
            frame_input,
            command=self.login,
            cursor="hand2",
            bg='white',
            image=self.new_login,
            bd=0,

        )

        btn2.place(x=20, y=300)

        btn3 = Button(
            frame_input,
            command=self.login,
            text="Not Registered? register",
            cursor="hand2",
            font=("Bauhaus 93", 12),
            bg="white",
            fg="black",
            bd=0,
        )

        btn3.place(x=85, y=415)

    def login(self):

        if self.username.get() == "" or self.password.get() == "":

            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:

            try:

                con = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="Ajith@05",
                    database="pythongui",
                )

                cur = con.cursor()

                cur.execute(
                    "select * from register where username=%s and password=%s",
                    (self.username.get(), self.password.get()),
                )

                row = cur.fetchone()

                if row is None:

                    messagebox.showerror(
                        "Error", "Invalid Username And Password", parent=self.root
                    )

                    self.loginclear()

                    self.username.focus()

                else:

                    self.home_page()

                    con.close()

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root
                )

    def sign_up(self):
        root.destroy()
        import register_page_3

    def home_page(self):
        root.destroy()
        import index

    def loginclear(self):
        self.username.delete(0, END)
        self.password.delete(0, END)


root = Tk()
ob = Login(root)
root.mainloop()
