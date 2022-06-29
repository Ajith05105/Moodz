from tkinter import *

from tkinter import messagebox

import pymysql


class Login:
    def __init__(self, root):

        self.root = root

        self.root.title("Login and registration system for Apps")

        self.root.geometry("1366x700+0+0")

        self.root.resizable(False, False)

        self.loginform()

    def loginform(self):

        Frame_login = Frame(self.root, bg="white")

        Frame_login.place(x=0, y=0, height=700, width=1366)

        frame_input = Frame(self.root, bg="white")

        frame_input.place(x=320, y=130, height=450, width=350)

        label1 = Label(
            frame_input,
            text="Login Here",
            font=("impact", 32, "bold"),
            fg="black",
            bg="white",
        )

        label1.place(x=75, y=20)

        label2 = Label(
            frame_input,
            text="Username",
            font=("Goudy old style", 20, "bold"),
            fg="orangered",
            bg="white",
        )

        label2.place(x=30, y=95)

        self.username = Entry(
            frame_input, font=("times new roman", 15, "bold"), bg="lightgray"
        )

        self.username.place(x=30, y=145, width=270, height=35)

        label3 = Label(
            frame_input,
            text="Password",
            font=("Goudy old style", 20, "bold"),
            fg="orangered",
            bg="white",
        )

        label3.place(x=30, y=195)

        self.password = Entry(
            frame_input, font=("times new roman", 15, "bold"), bg="lightgray"
        )

        self.password.place(x=30, y=245, width=270, height=35)

        btn1 = Button(
            frame_input,
            text="forgot password?",
            cursor="hand2",
            font=("calibri", 10),
            bg="white",
            fg="black",
            bd=0,
        )

        btn1.place(x=125, y=305)

        btn2 = Button(
            frame_input,
            text="Login",
            command=self.login,
            cursor="hand2",
            font=("times new roman", 15),
            fg="white",
            bg="orangered",
            bd=0,
            width=15,
            height=1,
        )

        btn2.place(x=90, y=340)

        btn3 = Button(
            frame_input,
            command=self.sign_up,
            text="Not Registered?register",
            cursor="hand2",
            font=("calibri", 10),
            bg="white",
            fg="black",
            bd=0,
        )

        btn3.place(x=110, y=390)

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

