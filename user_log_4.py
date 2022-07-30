from login_page_4 import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import pymysql
import datetime


# creating a class
class User_logs:

    def __init__(self, root):  # initialise method
        self.root = root
        self.root.title("Moodz")  # title of the window
        self.root.geometry('550x700+500+0')  # geometry of the window
        self.root['bg'] = 'white'  # background colour of the window
        self.images_list = []
        self.root.resizable = (False, False)
        self.y = 0
        self.user_logs()

    def creating_button(self, command, imgLoc, h, w, x, y):
        self.original = Image.open(f'img/{imgLoc}.png').resize((w, h), Image.ANTIALIAS)  # calling it all in one line
        self.photoimg = ImageTk.PhotoImage(self.original)
        button = Button(self.root, image=self.photoimg, bd=0, command=command, highlightthickness=0)
        button.place(x=x, y=y)
        self.images_list.append(self.photoimg)
        return button

    def login_page(self):
        root.destroy()
        import login_page_5

    def entry_page(self):
        root.destroy()
        import index_3

    def fetching_info(self):
        try:
            con = pymysql.connect(
                host="sql6.freemysqlhosting.net",
                user="sql6509714",
                password="XGJALitivY",
                database="sql6509714",
            )

            cur = con.cursor()
            cursor = con.cursor()

            cursor.execute(
                "select * from user_logins"
            )
            self.results = cursor.fetchall()
            self.username = self.results[len(self.results) - 1][0]

            cur.execute(
                "select emoji_id,entry_date,entry_time,UserId from entry_info where username = %s",
                (self.username)
            )

            self.rows = cur.fetchall()
            return self.rows


        except Exception as es:
            print(f"Error due to:{str(es)}")

    def user_logs(self):

        self.great_emoji = Image.open('img/great_emoji.png')
        self.great_emoji_resized = self.great_emoji.resize((75, 70))
        self.new_great_emoji = ImageTk.PhotoImage(self.great_emoji_resized)

        # feeling happy emoji
        self.happy_emoji = Image.open('img/happy_emoji.png')
        self.happy_emoji_resized = self.happy_emoji.resize((75, 70))
        self.new_happy_emoji = ImageTk.PhotoImage(self.happy_emoji_resized)

        # feeling meh emoji
        self.meh_emoji = Image.open('img/meh_emoji.png')
        self.meh_emoji_resized = self.meh_emoji.resize((75, 70))
        self.new_meh_emoji = ImageTk.PhotoImage(self.meh_emoji_resized)

        # feeling sad emoji
        self.sad_emoji = Image.open('img/sad_emoji.png')
        self.sad_emoji_resized = self.sad_emoji.resize((75, 70))
        self.new_sad_emoji = ImageTk.PhotoImage(self.sad_emoji_resized)

        # feeling awful emoji
        self.awful_emoji = Image.open('img/awful_emoji.png')
        self.awful_emoji_resized = self.awful_emoji.resize((75, 70))
        self.new_awful_emoji = ImageTk.PhotoImage(self.awful_emoji_resized)

        self.emoji_images = [('none', 'none'), (self.new_great_emoji, 'Great'), (self.new_happy_emoji, 'Happy'),
                             (self.new_meh_emoji, 'Meh'), (self.new_sad_emoji, 'Sad'),
                             (self.new_awful_emoji, 'Awful')]

        self.rows = self.fetching_info()
        wrapper1 = LabelFrame(root, bg='#FEDC69', height=100)
        self.title_img = PhotoImage(file='img/title.png')
        self.title = Label(wrapper1,
                           image=self.title_img,
                           bd=0
                           )
        self.title.place(x=115, y=15)

        wrapper2 = LabelFrame(root, highlightbackground='black')
        wrapper3 = LabelFrame(root, highlightbackground='black', height=70, bg='#FEDC69')

        mycanvas = Canvas(wrapper2, bg='#FFFDD0', height=490, width=505)
        mycanvas.pack(side='left', fill=Y, )

        yscrollbar = ttk.Scrollbar(wrapper2, orient="vertical", command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill="y")

        mycanvas.configure(yscrollcommand=yscrollbar.set)

        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))

        self.myframe = Frame(mycanvas, bg='#FFFDD0')
        mycanvas.create_window((100, 3), window=self.myframe, anchor="nw")

        self.creating_button('', 'entries', 60, 75, 35, 629)
        self.creating_button('', 'stats', 60, 71, 138, 629)
        self.creating_button(self.entry_page, "plus", 60, 61, 245, 629)
        self.creating_button('', "calendar", 60, 75, 340, 629)
        self.creating_button(self.login_page, 'sign_out', 60, 75, 435, 626)

        wrapper1.pack(fill="x", expand="yes", padx=10)
        wrapper2.pack(fill="both", expand="yes", padx=10, )
        wrapper3.pack(fill="x", expand="yes", padx=10, )

        for i in self.rows:
            self.y += 1
            self.emoji_id = i[0]
            self.entry_date = str(i[1])
            self.entry_time = str(i[2])
            self.user_id = i[3]

            tk.Label(self.myframe,
                     image=self.emoji_images[self.emoji_id][0]
                     ).grid(row=self.y, column=1)
            self.images_list.append(self.emoji_images[self.emoji_id][0])

            tk.Label(
                self.myframe,
                text=f' {datetime.datetime.strptime(self.entry_date, "%Y-%m-%d").strftime("%A %d %b")} '
                     f'  {datetime.datetime.strptime(self.entry_time, "%H:%M:%S").strftime("%I:%M %p")}',
                bg='#FFFDD0',
                fg="black",
                borderwidth=3,
                font=("TkMenuFont", 10)).grid(row=self.y, column=2)

            tk.Label(self.myframe,
                     text=self.emoji_images[self.emoji_id][1],
                     font=("TkMenuFont", 14, 'bold'),
                     bg='#FFFDD0',
                     fg='black', ).grid(column=0, row=self.y, pady=40)


# running the root
root = Tk()
ob = User_logs(root)
root.mainloop()
