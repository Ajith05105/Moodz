import tkinter as tk
from tkinter import messagebox
import bcrypt
import pymysql
from tkinter import *
from PIL import Image, ImageTk
import login_page_6
from login_page_4 import Login as ln
import email_validator


class Register_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'white')
        self.controller = controller
        self.images_list = []
        self.registerform()

    def registerform(self):

        self.logo = ImageTk.PhotoImage(file="img/register_logo.png")

        logo = Label(self, image=self.logo, bd='0').place(x=15, y=-15)

        self.side_bar = ln.creating_image(self, 'side_bar_register_page', 750, 310, 390, 0)

        self.entry_img = ln.creating_image(self, 'entry_img', 50, 320, 55, 360)

        self.entry_img_2 = ln.creating_image(self, 'entry_img', 50, 320, 55, 460)

        self.entry_img_3 = ln.creating_image(self, 'entry_img', 50, 320, 55, 542)

        self.entry_img_4 = ln.creating_image(self, 'entry_img', 50, 320, 55, 270)

        label2 = Label(
            self,
            text="Username",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",

        )

        label2.place(x=55, y=335)

        self.username = Entry(
            self, font=("times new roman", 14, "bold"), bg="white", bd=0

        )

        self.username.place(x=68, y=368, width=300, height=30)

        label3 = Label(
            self,
            text="Password",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",
        )

        label3.place(x=55, y=425)

        self.password = Entry(
            self, font=("times new roman", 15, "bold"), bg="white", bd=0,
        )

        self.password.place(x=67, y=469.5, width=300, height=30)

        label4 = Label(
            self,
            text="Email-id",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",
        )

        label4.place(x=55, y=245)

        self.email = Entry(
            self, font=("times new roman", 15, "bold"), bg="white", bd=0
        )

        self.email.place(x=65, y=278, width=300, height=30)

        label5 = Label(
            self,
            text="Confirm Password",
            font=("Bauhaus 93", 12),
            fg="Black",
            bg="white",
        )

        label5.place(x=60, y=515)

        self.confirm_pswd = Entry(
            self, font=("times new roman", 15, "bold"), bg="white", bd=0
        )

        self.confirm_pswd.place(x=65, y=550, width=300, height=30)

        self.register_button = Image.open('img/register_button.png')
        self.register_button_resized = self.register_button.resize((210, 80))
        self.new_register_button = ImageTk.PhotoImage(self.register_button_resized)
        register_button = Button(self,image=self.new_register_button,
                                 cursor='hand2', bg='white', borderwidth='0',
                                 command=self.register)
        register_button.place(x='100', y='590')
        btn3 = Button(
            self,
            command=self.login_page,
            text="Already Registered? Login",
            cursor="hand2",
            font=("calibri", 10),
            bg="white",
            fg="black",
            bd=0,
        )

        btn3.place(x=140, y=670)

    def register(self):

        if (
                self.username.get() == ""
                or self.password.get() == ""
                or self.email.get() == ""
                or self.confirm_pswd.get() == ""
        ):

            messagebox.showerror("Error", "All Fields Are Required", parent=self)

        elif self.password.get() == self.confirm_pswd.get():
            try:
                email = email_validator.validate_email(self.email.get()).email

                con = pymysql.connect(
                    host="sql6.freemysqlhosting.net",
                    user="sql6509714",
                    password="XGJALitivY",
                    database="sql6509714",
                )

                cur = con.cursor()

                cur.execute(
                    "select * from master_register where emailid=%s", self.email.get()
                )

                row = cur.fetchone()

                if row is not None:

                    messagebox.showerror(
                        "Error",
                        "User already Exist,Please try with another Email",
                        parent=self,
                    )

                    self.regclear()

                    self.username.focus()

                else:

                    self.original_password = bytes(self.password.get(), "utf-8")
                    self.hashedPW = bcrypt.hashpw(self.original_password, bcrypt.gensalt())
                    cur.execute(
                        "insert into master_register (username,emailid,password) values(%s,%s,%s)",
                        (
                            self.username.get(),
                            self.email.get(),
                            self.hashedPW,

                        ),
                    )

                    con.commit()

                    con.close()

                    messagebox.showinfo(
                        "Success", "Register Succesfull", parent=self
                    )

                    self.regclear()
                    self.login_page()


            except Exception as es:

                messagebox.showerror(
                    "Error", f"Error due to:{str(es)}", parent=self
                )



        else:

            messagebox.showerror(
                "Error",
                "Password and Confirm Password Should Be Same",
                parent=self,
            )

    def regclear(self):
        self.username.delete(0, END)

        self.password.delete(0, END)

        self.email.delete(0, END)

        self.confirm_pswd.delete(0, END)

    def login_page(self):
        self.controller.show_frame(login_page_6.Login)