from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry('650x750+500+0')
        self.root.resizable(False, False)
        self.root['bg'] = 'white'
        self.Register()

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
            bg="white")
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
            command=self.Register,
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
                        "Error", "Invalid Username And Password", parent=self.root)
                    self.loginclear()
                    self.username.focus()

                else:
                    self.appscreen()
                    con.close()

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root
                )


    def Register(self):
        self.logo = ImageTk.PhotoImage(file="img/register_logo.png")

        logo = Label(root, image=self.logo,bd='0').place(x=15, y=-15)

        self.side_bar = Image.open('img/side_bar_register_page.png')
        self.side_bar_resized = self.side_bar.resize((310, 750))
        self.new_side_bar = ImageTk.PhotoImage(self.side_bar_resized)
        img_side_bar = Label(root, image=self.new_side_bar)
        img_side_bar.place(x=390, y=0)

        self.entry_img = Image.open('img/entry_img.png')
        self.entry_img_resized = self.entry_img.resize((320, 50))
        self.new_entry_img = ImageTk.PhotoImage(self.entry_img_resized)
        new_entry_img = Label(root, image=self.new_entry_img,bd=0)
        new_entry_img.place(x=55, y=360)

        self.entry_img_2 = Image.open('img/entry_img_2.png')
        self.entry_img_resized_2 = self.entry_img_2.resize((320, 50))
        self.new_entry_img_2 = ImageTk.PhotoImage(self.entry_img_resized_2)
        new_entry_img_2 = Label(root, image=self.new_entry_img_2,bd=0)
        new_entry_img_2.place(x=55, y=460)

        self.entry_img_3 = Image.open('img/entry_img_2.png')
        self.entry_img_resized_3 = self.entry_img_3.resize((320, 50))
        self.new_entry_img_3 = ImageTk.PhotoImage(self.entry_img_resized_3)
        new_entry_img_3 = Label(root, image=self.new_entry_img_3, bd=0)
        new_entry_img_3.place(x=55, y=542)

        self.entry_img_4 = Image.open('img/entry_img_2.png')
        self.entry_img_resized_4 = self.entry_img_4.resize((320, 50))
        self.new_entry_img_4 = ImageTk.PhotoImage(self.entry_img_resized_4)
        new_entry_img_4 = Label(root, image=self.new_entry_img_4, bd=0)
        new_entry_img_4.place(x=55, y=270)

        label2 = Label(
            root,
            text = "Username",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",

        )

        label2.place(x=55, y=335)

        self.entry = Entry(
            root, font=("times new roman", 14, "bold"), bg="white",bd = 0

        )

        self.entry.place(x=68, y=368, width=300, height=30)

        label3 = Label(
            root,
            text="Password",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",
        )

        label3.place(x=55, y=425)

        self.entry2 = Entry(
                root, font=("times new roman", 15, "bold"), bg="white",bd=0,
        )

        self.entry2.place(x=67, y=469.5, width=300, height=30)

        label4 = Label(
            root,
            text="Email-id",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",
        )

        label4.place(x=55, y=245)

        self.entry3 = Entry(
            root, font=("times new roman", 15, "bold"), bg="white", bd=0
        )

        self.entry3.place(x=65, y=278, width=300, height=30)

        label5 = Label(
            root,
            text="Confirm Password",
            font=("Bauhaus 93", 12),
            fg="Black",
            bg="white",
        )

        label5.place(x=60, y=515)

        self.entry4 = Entry(
            root, font=("times new roman", 15, "bold"), bg="white", bd=0
        )

        self.entry4.place(x=65, y=550, width=300, height=30)

        self.register_button = Image.open('img/register_button.png')
        self.register_button_resized = self.register_button.resize((210, 80))
        self.new_register_button = ImageTk.PhotoImage(self.register_button_resized)
        register_button = Button(image=self.new_register_button,
                                     cursor='hand2', bg='white', borderwidth='0',
                                     command=self.register)
        register_button.place(x='100', y='590')
        btn3 = Button(
            root,
            command=self.loginform,
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
                self.entry.get() == ""
                or self.entry2.get() == ""
                or self.entry3.get() == ""
                or self.entry4.get() == ""
        ):

            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)

        elif self.entry2.get() != self.entry4.get():

            messagebox.showerror(
                "Error",
                "Password and Confirm Password Should Be Same",
                parent=self.root,
            )

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
                    "select * from register where emailid=%s", self.entry3.get()
                )

                row = cur.fetchone()

                if row is not None:

                    messagebox.showerror(
                        "Error",
                        "User already Exist,Please try with another Email",
                        parent=self.root,
                    )

                    self.regclear()

                    self.entry.focus()

                else:
                    cur.execute(
                        "insert into register values(%s,%s,%s,%s)",
                        (
                            self.entry.get(),
                            self.entry3.get(),
                            self.entry2.get(),
                            self.entry4.get(),
                        ),
                    )

                    con.commit()

                    con.close()

                    messagebox.showinfo(
                        "Success", "Register Succesfull", parent=self.root
                    )

                    self.regclear()

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Error due to:{str(es)}", parent=self.root
                )

    def loginclear(self):
        self.username.delete(0, END)
        self.password.delete(0, END)

    def regclear(self):

        self.entry.delete(0, END)

        self.entry2.delete(0, END)

        self.entry3.delete(0, END)

        self.entry4.delete(0, END)

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

        label1.place(x=375, y=100)
        label2 = Label(
            Frame_login,
            text="This is a safe space for you to \n express and understand your emotions",
            font=("times new roman", 32, "bold"),
            fg="black",
            bg="white",
        )

        label2.place(x=235, y=160)

        label3 = Label(
            Frame_login,
            text="App is under development",
            font=("times new roman", 32, "bold"),
            fg="black",
            bg="white",
        )

        label3.place(x=340, y=400)

        btn2 = Button(
            Frame_login,
            text="Logout",
            command=self.loginform,
            cursor="hand2",
            font=("times new roman", 15),
            fg="white",
            bg="orangered",
            bd=0,
            width=15,
            height=1,
        )

        btn2.place(x=1000, y=10)



root = Tk()

ob = Login(root)

root.mainloop()
