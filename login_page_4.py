from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, Entry
import bcrypt
import pymysql


# class for the login form
class Login:

    def __init__(self, root):

        # initializing and modifying the window

        self.root = root

        self.root.title("Login page")

        self.root.geometry("650x750+500+0")

        self.root.resizable(False, False)

        self.loginform()

    def loginform(self):

        # Widgets on the login form

        Frame_login = Frame(self.root, bg="white")

        Frame_login.place(x=0, y=0, height=750, width=750)

        # All the widgets in the form go in this frame

        frame_input = Frame(self.root, bg="white")

        frame_input.place(x=30, y=150, height=600, width=350)

        # The logo for the page

        self.logo = ImageTk.PhotoImage(file="img/register_logo.png")

        logo = Label(self.root, image=self.logo, bd='0').place(x=15, y=-15)

        # entry box for username

        self.entry_img = Image.open('img/entry_img.png')
        self.entry_img_resized = self.entry_img.resize((320, 50))
        self.new_entry_img = ImageTk.PhotoImage(self.entry_img_resized)
        new_entry_img = Label(frame_input, image=self.new_entry_img, bd=0)
        new_entry_img.place(x=20, y=138)

        # entry box for password

        self.entry_img_2 = Image.open('img/entry_img_2.png')
        self.entry_img_resized_2 = self.entry_img_2.resize((320, 50))
        self.new_entry_img_2 = ImageTk.PhotoImage(self.entry_img_resized_2)
        new_entry_img_2 = Label(frame_input, image=self.new_entry_img_2, bd=0)
        new_entry_img_2.place(x=20, y=240)

        # yellow side bar with emojis

        self.side_bar = Image.open('img/side_bar_register_page.png')
        self.side_bar_resized = self.side_bar.resize((310, 750))
        self.new_side_bar = ImageTk.PhotoImage(self.side_bar_resized)

        # image for the login button

        self.login_img = Image.open('img/login.png')
        self.login_resized_img = self.login_img.resize((330, 115))
        self.new_login_img = ImageTk.PhotoImage(self.login_resized_img)

        # label for the side bar

        label1 = Label(
            Frame_login,
            image=self.new_side_bar
        )

        label1.place(x=390, y=0)

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
            frame_input, font=("times new roman", 15,), bg="white", bd=0
        )

        self.username.place(x=30, y=145, width=300, height=33)

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
            frame_input, font=("times new roman", 15, "bold"), bg="white", bd=0
        )

        self.password.place(x=30, y=245, width=300, height=35)

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

        # If the user is not registerred, this button would direct them back to register page.

        btn3 = Button(
            frame_input,
            command=self.sign_up,
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

        # validating if the user leaves the feild empty

        if self.username.get() == "" or self.password.get() == "":

            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:

            try:

                # establishing a connection with the database

                con = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="Ajith@05",
                    database="pythongui",
                )

                cur = con.cursor()

                # selecting hashed password that matches with the username entered by the end-user

                cur.execute(
                    "SELECT `password` FROM register WHERE `username`=%s",
                    (self.username.get()),
                )

                row = cur.fetchone()

                # hashing the entered plain text and verifying with the password in database

                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid username", parent=self.root
                    )

                    self.loginclear()

                    self.username.focus()

                elif row is not None and bcrypt.checkpw(bytes(self.password.get(), 'utf-8'), bytes(row[0], 'utf-8')):
                    self.home_page()
                    con.close()

                else:

                    messagebox.showerror(
                        "Error", "Invalid Password", parent=self.root
                    )

                    self.loginclear()

                    self.username.focus()

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root
                )

    # this function links the login page to register page

    def sign_up(self):
        root.destroy()
        import register_page_6

    # this function redirects the user to the app

    def home_page(self):
        root.destroy()
        import index_2

    # this function clears the entry fields after the login is succesfull

    def loginclear(self):
        self.username.delete(0, END)
        self.password.delete(0, END)


# running the mainloopl


root = Tk()
ob = Login(root)
root.mainloop()
