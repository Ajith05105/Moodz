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
        self.images_list = []  # this list keeps a reference of the images
        self.loginform()

    def creating_image(self, imgLoc, h, w, x, y):
        self.original = Image.open(f'img/{imgLoc}.png').resize((w, h), Image.ANTIALIAS)  # calling it all in one line
        self.photoimg = ImageTk.PhotoImage(self.original)
        label = Label(self.root, image=self.photoimg, bd=0)
        label.place(x=x, y=y)
        self.images_list.append(self.photoimg)
        return label

    def loginform(self):
        # Widgets on the login form
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, height=750, width=750)
        # All the widgets in the form go in this frame
        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=30, y=150, height=600, width=350)
        # The logo for the page
        self.logo = ImageTk.PhotoImage(file="img/register_logo.png")
        logo = Label(self.root, image=self.logo, bd='0')
        logo.place(x=15, y=-15)
        # entry box for username
        self.entry_img = self.creating_image('entry_img', 50, 320, 50, 290)
        # entry box for password
        self.entry_img_2 = self.creating_image('entry_img', 50, 320, 50, 390)

        # image for the login button
        self.login_img = Image.open('img/login.png')
        self.login_resized_img = self.login_img.resize((330, 115))
        self.new_login_img = ImageTk.PhotoImage(self.login_resized_img)

        # label for the side bar
        self.side_bar = self.creating_image("side_bar_register_page", 750, 310, 390, 0)

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
            self.root, font=("times new roman", 15,), bg="white", bd=0
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
            self.root, font=("times new roman", 15, "bold"), bg="white", bd=0
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
                        "Error", "Invalid username", parent=self.root
                    )
                    self.loginclear()
                    self.username.focus()

                elif row is not None and bcrypt.checkpw(bytes(self.password.get(), 'utf-8'), bytes(row[0], 'utf-8')):
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
        import index_3

    # this function clears the entry fields after the login is succesfull
    def loginclear(self):
        self.username.delete(0, END)
        self.password.delete(0, END)


# running the mainloop if the following condition is true
if __name__ == "__main__":
    root = Tk()
    ob = Login(root)
    root.mainloop()
