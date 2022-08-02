import tkinter as tk
from tkinter import messagebox
import bcrypt
import pymysql
from tkinter import *
from PIL import Image,ImageTk

import index_4
import register_page_7
from login_page_4 import Login as ln
import main_page
import Page_2


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.images_list = []
        self.loginform()

    def loginform(self):
        # Widgets on the login form
        Frame_login = Frame(self, bg="white")
        Frame_login.place(x=0, y=0, height=750, width=750)
        # All the widgets in the form go in this frame
        frame_input = Frame(self, bg="white")
        frame_input.place(x=30, y=150, height=600, width=350)
        # The logo for the page
        self.logo = ImageTk.PhotoImage(file="img/register_logo.png")
        logo = Label(self, image=self.logo, bd='0')
        logo.place(x=15, y=-15)
        # entry box for username
        self.entry_img = ln.creating_image(self, 'entry_img', 50, 320, 50, 290)
        # entry box for password
        self.entry_img_2 = ln.creating_image(self, 'entry_img', 50, 320, 50, 390)

        # image for the login button
        self.login_img = Image.open('img/login.png')
        self.login_resized_img = self.login_img.resize((330, 115))
        self.new_login_img = ImageTk.PhotoImage(self.login_resized_img)

        # label for the side bar
        self.side_bar = ln.creating_image(self, "side_bar_register_page", 750, 310, 390, 0)

        # label for the username text
        label2 = Label(
            frame_input,
            text="Username",
            font=("Bauhaus 93", 20),
            fg="black",
            bg="white",
        )
        label2.place(x=25, y=100)

        # entry field for the username
        self.username = Entry(
            self, font=("times new roman", 15,), bg="white", bd=0
        )
        self.username.place(x=60, y=297, width=300, height=33)

        # label for password text
        label3 = Label(
            frame_input,
            text="Password",
            font=("Bauhaus 93", 20),
            fg="black",
            bg="white",
        )
        label3.place(x=25, y=200)

        # entry field for the password
        self.password = Entry(
            self, font=("times new roman", 15, "bold"), bg="white", bd=0
        )

        self.password.place(x=60, y=396, width=300, height=35)

        # the login button which is linked to login function
        btn2 = Button(
            frame_input,
            command=self.login,
            cursor="hand2",
            bg='white',
            image=self.new_login_img,
            bd=0,
        )
        btn2.place(x=20, y=300)

        # If the user is not registered, this button would direct them back to register page.
        btn3 = Button(
            frame_input,
            command= lambda: self.controller.show_frame(register_page_7.Register_page),
            text="Not Registered? register",
            cursor="hand2",
            font=("Bauhaus 93", 12),
            bg="white",
            fg="black",
            bd=0,
        )
        btn3.place(x=85, y=415)

    # login function that verifies the password , username and directs to the app
    def login(self):
        # validating if the user leaves the field empty

        if self.username.get() == "" or self.password.get() == "":

            messagebox.showerror("Error", "All fields are required", parent=self)
        else:
            try:
                # establishing a connection with the database
                con = pymysql.connect(
                    host="sql6.freemysqlhosting.net",
                    user="sql6509714",
                    password="XGJALitivY",
                    database="sql6509714",
                )
                cur = con.cursor()
                cursor = con.cursor()

                # selecting hashed password that matches with the username entered by the end-user
                cur.execute(
                    "SELECT `password` FROM master_register WHERE `username`=%s",
                    (self.username.get()),
                )
                cursor.execute(
                    "SELECT `UserId` FROM master_register WHERE `username`=%s",
                    (self.username.get()),
                )
                row = cur.fetchone()

                # hashing the entered plain text and verifying with the password in database
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid username", parent=self
                    )
                    self.loginclear()
                    self.username.focus()

                elif row is not None and bcrypt.checkpw(bytes(self.password.get(), 'utf-8'),
                                                        bytes(row[0], 'utf-8')):
                    cur.execute(
                        "insert into user_logins (username) values(%s)",
                        (
                            self.username.get(),
                        ),
                    )

                    con.commit()
                    self.home_page()
                    con.close()

                else:
                    messagebox.showerror(
                        "Error", "Invalid Password", parent=self
                    )
                    self.loginclear()
                    self.username.focus()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self
                )

    # this function clears the entry fields after the login is succesfull
    def loginclear(self):
        self.username.delete(0, END)
        self.password.delete(0, END)

    def home_page(self):
        self.controller.show_frame(index_4.home_page)
