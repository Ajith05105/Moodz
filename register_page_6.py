from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from main import *
import email_validator
import pymysql
import bcrypt
import sys


class Register:
    # initialising the window and customising it
    def __init__(self, root):
        self.root = root
        self.root.title("register page")
        self.root.geometry('650x750+500+0')
        self.root['bg'] = 'white'
        self.root.resizable(False, False)
        self.images_list = []
        self.register_page()

    def login_page(self):
        root.destroy()
        modulename = "login_page_5"
        if modulename not in sys.modules:
            import login_page_5
        else:
            del sys.modules[modulename]
            import login_page_5

    # this function creates all the forms in the page
    def register_page(self):
        # This is the main logo
        self.logo = ImageTk.PhotoImage(file="img/register_logo.png")
        # This places the logo
        Label(self.root, image=self.logo, bd='0').place(x=15, y=-15)
        # using the function defined in another page to avoid duplication
        self.side_bar = main_page.creating_image(self,
                                                 'side_bar_register_page',
                                                 750, 310, 390, 0)
        # creating the entry fields
        self.entry_img = main_page.creating_image(self, 'entry_img',
                                                  50, 320, 55, 360)

        self.entry_img_2 = main_page.creating_image(self, 'entry_img', 50,
                                                    320, 55, 460)

        self.entry_img_3 = main_page.creating_image(self, 'entry_img', 50,
                                                    320, 55, 542)

        self.entry_img_4 = main_page.creating_image(self, 'entry_img', 50,
                                                    320, 55, 270)

        label2 = Label(
            self.root,
            text="Username",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",

        )
        label2.place(x=55, y=335)
        # entry box for username
        self.username = Entry(
            self.root, font=("times new roman", 14, "bold"), bg="white", bd=0

        )

        self.username.place(x=68, y=368, width=300, height=30)

        label3 = Label(
            self.root,
            text="Password",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",
        )

        label3.place(x=55, y=425)
        # entry box for password and it's encrypted
        self.password = Entry(
            self.root,
            font=("times new roman", 15, "bold"),
            show="*",
            bg="white",
            bd=0,
        )

        self.password.place(x=67, y=469.5, width=300, height=30)

        label4 = Label(
            self.root,
            text="Email-id",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",
        )

        label4.place(x=55, y=245)
        # entry field for emailID
        self.email = Entry(
            self.root, font=("times new roman", 15, "bold"), bg="white", bd=0
        )
        self.email.place(x=65, y=278, width=300, height=30)

        label5 = Label(
            self.root,
            text="Confirm Password",
            font=("Bauhaus 93", 12),
            fg="Black",
            bg="white",
        )

        label5.place(x=60, y=515)
        # entry field for confirm password
        self.confirm_pswd = Entry(self.root,
                                  font=("times new roman", 15, "bold"),
                                  bg="white",
                                  bd=0,
                                  show="*")

        self.confirm_pswd.place(x=65, y=550, width=300, height=30)

        # this is the button that runs that verifies if the
        # user entries are valid and enters data into db
        self.register_button = Image.open('img/register_button.png')
        self.register_button_resized = self.register_button.resize((210, 80))
        self.new_register_button = \
            ImageTk.PhotoImage(self.register_button_resized)
        register_button = Button(image=self.new_register_button,
                                 cursor='hand2', bg='white', borderwidth='0',
                                 command=self.register)
        register_button.place(x='100', y='590')
        btn3 = Button(
            self.root,
            command=self.login_page,
            text="Already Registered? Login",
            cursor="hand2",
            font=("calibri", 10),
            bg="white",
            fg="black",
            bd=0,
        )
        btn3.place(x=140, y=670)

    # this is the main function that verifies the
    # user entries and inserts info into DB
    def register(self):
        # validating for the blank entries
        for i in (self.username.get(),
                  self.email.get(),
                  self.confirm_pswd.get(),
                  self.password.get(),
                  ):
            if i == "":
                messagebox.showerror("Error",
                                     "All Fields Are Required",
                                     parent=self.root)
                return
        try:
            # validating email
            email = email_validator.validate_email(self.email.get()).email

            # validating username
            if self.username.get().isalpha() is False:
                messagebox.showerror("Error",
                                     "Username must only contain alphabets "
                                     "and it should not contain spaces",
                                     parent=self.root)

                # ensuring the password is longer than 6 characters to
                # increase the strength
            elif len(self.password.get()) < 6:
                messagebox.showerror("Error",
                                     "password must be at least 6 "
                                     "letters long",
                                     parent=self.root)

                # checking that the password = confirm password
            elif self.password.get() == self.confirm_pswd.get():
                con = pymysql.connect(
                    host="sql6.freemysqlhosting.net",
                    user="sql6509714",
                    password="XGJALitivY",
                    database="sql6509714",
                )

                cur = con.cursor()
                # checking weather the email_ID is present in the database
                cur.execute(
                    "select * from master_register where emailid=%s",
                    self.email.get()
                )

                row = cur.fetchone()
                # if the fetch returns with a value then the user
                # already exists
                if row is not None:
                    # prints error message
                    messagebox.showerror(
                        "Error",
                        "User already Exist,Please try with another Email",
                        parent=self.root,
                    )

                    self.regclear()

                    self.username.focus()

                else:
                    # if the email does not already exist,
                    # hash the password and insert values into DB
                    self.original_password = \
                        bytes(self.password.get(), "utf-8")
                    self.hashedPW = \
                        bcrypt.hashpw(self.original_password, bcrypt.gensalt())
                    cur.execute(
                        "insert into master_register "
                        "(username,emailid,password) values(%s,%s,%s)",
                        (
                            self.username.get(),
                            self.email.get(),
                            self.hashedPW,

                        ),
                    )

                    con.commit()

                    con.close()

                    messagebox.showinfo(
                        "Success", "Register Succesfull", parent=self.root
                    )

                    self.regclear()
                    self.login_page()

            else:
                messagebox.showerror(
                    "Error", "password and "
                             "confirm password dont match",
                    parent=self.root)

        except Exception as es:
            messagebox.showerror(
                "Error", f"Error due to: Invalid Email", parent=self.root)

    # clearing the fields
    def regclear(self):
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.email.delete(0, END)
        self.confirm_pswd.delete(0, END)


root = Tk()
ob = Register(root)
root.mainloop()
