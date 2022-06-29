from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import bcrypt







class Register:

    def __init__(self,root):
        self.root = root
        self.root.title("register page")
        self.root.geometry('650x750+500+0')
        self.root['bg'] = 'white'
        self.root.resizable(False,False)
        self.Register()



    def Register(self):
        def creating_image(a, w, h, x, y):
            global photoimg  # keeping a reference

            self.original = Image.open(a).resize((w, h), Image.ANTIALIAS)  # calling it all in one line
            self.photoimg = ImageTk.PhotoImage(self.original)
            self.canvas = Label(self.root, image=self.photoimg, bg='white')

            self.canvas.place(x=x, y=y)
            return self.canvas

        self.logo = ImageTk.PhotoImage(file="img/register_logo.png")

        logo = Label(self.root, image=self.logo, bd='0').place(x=15, y=-15)

        self.side_bar = Image.open('img/side_bar_register_page.png')
        self.side_bar_resized = self.side_bar.resize((310, 750))
        self.new_side_bar = ImageTk.PhotoImage(self.side_bar_resized)
        img_side_bar = Label(self.root, image=self.new_side_bar)
        img_side_bar.place(x=390, y=0)

        self.entry_img = Image.open('img/entry_img.png')
        self.entry_img_resized = self.entry_img.resize((320, 50))
        self.new_entry_img = ImageTk.PhotoImage(self.entry_img_resized)
        new_entry_img = Label(self.root, image=self.new_entry_img, bd=0)
        new_entry_img.place(x=55, y=360)

        self.entry_img_2 = Image.open('img/entry_img_2.png')
        self.entry_img_resized_2 = self.entry_img_2.resize((320, 50))
        self.new_entry_img_2 = ImageTk.PhotoImage(self.entry_img_resized_2)
        new_entry_img_2 = Label(self.root, image=self.new_entry_img_2, bd=0)
        new_entry_img_2.place(x=55, y=460)

        self.entry_img_3 = Image.open('img/entry_img_2.png')
        self.entry_img_resized_3 = self.entry_img_3.resize((320, 50))
        self.new_entry_img_3 = ImageTk.PhotoImage(self.entry_img_resized_3)
        new_entry_img_3 = Label(self.root, image=self.new_entry_img_3, bd=0)
        new_entry_img_3.place(x=55, y=542)

        self.entry_img_4 = Image.open('img/entry_img_2.png')
        self.entry_img_resized_4 = self.entry_img_4.resize((320, 50))
        self.new_entry_img_4 = ImageTk.PhotoImage(self.entry_img_resized_4)
        new_entry_img_4 = Label(self.root, image=self.new_entry_img_4, bd=0)
        new_entry_img_4.place(x=55, y=270)

        label2 = Label(
            self.root,
            text="Username",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",

        )

        label2.place(x=55, y=335)

        self.entry1 = Entry(
            self.root, font=("times new roman", 14, "bold"), bg="white", bd=0

        )

        self.entry1.place(x=68, y=368, width=300, height=30)

        label3 = Label(
            self.root,
            text="Password",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",
        )

        label3.place(x=55, y=425)

        self.entry2 = Entry(
            self.root, font=("times new roman", 15, "bold"), bg="white", bd=0,
        )

        self.entry2.place(x=67, y=469.5, width=300, height=30)

        label4 = Label(
            self.root,
            text="Email-id",
            font=("Bauhaus 93", 12),
            fg="black",
            bg="white",
        )

        label4.place(x=55, y=245)

        self.entry3 = Entry(
            self.root, font=("times new roman", 15, "bold"), bg="white", bd=0
        )

        self.entry3.place(x=65, y=278, width=300, height=30)

        label5 = Label(
            self.root,
            text="Confirm Password",
            font=("Bauhaus 93", 12),
            fg="Black",
            bg="white",
        )

        label5.place(x=60, y=515)

        self.entry4 = Entry(
            self.root, font=("times new roman", 15, "bold"), bg="white", bd=0
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
            self.root,
            command = self.login_page,
            text="Already Registered? Login",
            cursor="hand2",
            font=("calibri", 10),
            bg="white",
            fg="black",
            bd=0,
        )

        btn3.place(x=140, y=670)


    def register(self):
        self.userid = 0
        if (
                self.entry1.get() == ""
                or self.entry2.get() == ""
                or self.entry3.get() == ""
                or self.entry4.get() == ""
        ):

            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)

        elif self.entry2.get() == self.entry4.get():
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

                    self.entry1.focus()

                else:

                    self.password = bytes(self.entry2.get(),"utf-8")
                    self.hashedPW = bcrypt.hashpw(self.password,bcrypt.gensalt())
                    print(self.hashedPW)
                    cur.execute(
                        "insert into register (username,emailid,password) values(%s,%s,%s)",
                        (
                            self.entry1.get(),
                            self.entry3.get(),
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


            except Exception as es:

                messagebox.showerror(
                    "Error", f"Error due to:{str(es)}", parent=self.root
                )



        else:

            messagebox.showerror(
                "Error",
                "Password and Confirm Password Should Be Same",
                parent=self.root,
            )



    def regclear(self):
        self.entry1.delete(0, END)

        self.entry2.delete(0, END)

        self.entry3.delete(0, END)

        self.entry4.delete(0, END)

    def login_page(self):
        root.destroy()
        import login_page_4


root = Tk()
ob = Register(root)
root.mainloop()
