import tkinter as tk
import pymysql
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import index_4
import login_page_6
import datetime


class Log(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        self.y = 0
        self.images_list = []
        self.printing_entries()


    def creating_button(self, command, imgLoc, h, w, x, y):
        self.original = Image.open(f'img/{imgLoc}.png').resize((w, h), Image.ANTIALIAS)  # calling it all in one line
        self.photoimg = ImageTk.PhotoImage(self.original)
        button = Button(self, image=self.photoimg, bd=0, command=command, highlightthickness=0)
        button.place(x=x, y=y)
        self.images_list.append(self.photoimg)
        return button

    # imports to login page
    def login_page(self):
        self.controller.show_frame(login_page_6.Login)

    # imports to entry_page
    def entry_page(self):
        self.controller.show_frame(index_4.home_page)

    # this function fetches all the entries from the user
    def fetching_info(self):
        # establishing db connection
        try:
            con = pymysql.connect(
                host="sql6.freemysqlhosting.net",
                user="sql6509714",
                password="XGJALitivY",
                database="sql6509714",
            )

            cur = con.cursor()  # this cursor fetches the current user
            cursor = con.cursor()  # this cursor fetches the user's entries

            cursor.execute(
                "select * from user_logins"
            )
            # This fetches all rows in the user_logins table
            results = cursor.fetchall()
            # This identifies the last entry as the current user.
            self.username = results[len(results) - 1]

            # this fetches all the entries from the current user from
            # entry info table.
            cur.execute(
                "select emoji_id,entry_date,entry_time,UserId from entry_info where username = %s",
                (self.username)
            )
            # this stores all entries from the current user
            self.rows = cur.fetchall()
            return self.rows


        except Exception as es:
            print(f"Error due to:{str(es)}")



    def printing_entries(self):
        # loading and resizing great_emoji image
        self.fetching_info()

        self.great_emoji = Image.open('img/great_emoji.png')
        self.great_emoji_resized = self.great_emoji.resize((75, 70))
        self.new_great_emoji = ImageTk.PhotoImage(self.great_emoji_resized)

        # loading and resizing  happy emoji image
        self.happy_emoji = Image.open('img/happy_emoji.png')
        self.happy_emoji_resized = self.happy_emoji.resize((75, 70))
        self.new_happy_emoji = ImageTk.PhotoImage(self.happy_emoji_resized)

        # loading and resizing meh emoji image
        self.meh_emoji = Image.open('img/meh_emoji.png')
        self.meh_emoji_resized = self.meh_emoji.resize((75, 70))
        self.new_meh_emoji = ImageTk.PhotoImage(self.meh_emoji_resized)

        # loading and resizing sad emoji image
        self.sad_emoji = Image.open('img/sad_emoji.png')
        self.sad_emoji_resized = self.sad_emoji.resize((75, 70))
        self.new_sad_emoji = ImageTk.PhotoImage(self.sad_emoji_resized)

        # loading and resizing awful emoji image
        self.awful_emoji = Image.open('img/awful_emoji.png')
        self.awful_emoji_resized = self.awful_emoji.resize((75, 70))
        self.new_awful_emoji = ImageTk.PhotoImage(self.awful_emoji_resized)

        # creating an array of lists, each list has an image and it correlating emoji.
        self.emoji_images = [('none', 'none'), (self.new_great_emoji, 'Great'), (self.new_happy_emoji, 'Happy'),
                             (self.new_meh_emoji, 'Meh'), (self.new_sad_emoji, 'Sad'),
                             (self.new_awful_emoji, 'Awful')]

        wrapper1 = LabelFrame(self, bg='#FEDC69', height=100)

        # loading and placing moodz title in wrapper 1
        self.title_img = PhotoImage(file='img/title.png')
        self.title = Label(wrapper1,
                           image=self.title_img,
                           bd=0
                           )
        self.title.place(x=115, y=15)

        wrapper2 = LabelFrame(self, highlightbackground='black')
        wrapper3 = LabelFrame(self, highlightbackground='black', height=70, bg='#FEDC69')

        # creating a canvas is wrapper 2
        mycanvas = Canvas(wrapper2, bg='#FFFDD0', height=490, width=505)
        mycanvas.pack(side='left', fill=Y, )

        # placing a scrollbar in wrapper2
        yscrollbar = ttk.Scrollbar(wrapper2, orient="vertical", command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill="y")

        # setting up the scrollbar in the canvas
        mycanvas.configure(yscrollcommand=yscrollbar.set)

        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))

        # this is the frame that goes in the canvas, and all the entries go inside this frame
        self.myframe = Frame(mycanvas, bg='#FFFDD0')
        # creating the frame inside the canvas
        mycanvas.create_window((100, 3), window=self.myframe, anchor="nw")

        # using our user defined function to create buttons
        self.creating_button('', 'entries', 60, 75, 35, 629)
        self.creating_button('', 'stats', 60, 71, 138, 629)
        self.creating_button(lambda : [self.fetching_info(),self.entry_page()], "plus", 60, 61, 245, 629)
        self.creating_button('', "calendar", 60, 75, 340, 629)
        self.creating_button(self.login_page, 'sign_out', 60, 75, 435, 626)

        # packing all the frames
        wrapper1.pack(fill="x", expand=1, padx=10)
        wrapper2.pack(fill="both", expand=1, padx=10, )
        wrapper3.pack(fill="x", expand=1, padx=10, )

        # looping through all the user entries
        for i in self.rows:
            # this is to increment the row count to print a new entry
            self.y += 1
            # since i is a array, I am braking it down and associating it
            # to its corresponding values
            self.emoji_id = i[0]
            self.entry_date = str(i[1])
            self.entry_time = str(i[2])
            self.user_id = i[3]

            # This label goes back to the array that we previously defined
            # and if you can notice the array is arranged according to the
            # emoji_id. So, when the emoji_id is 2, the image would be the
            # image from the second list in the array

            tk.Label(self.myframe,
                     image=self.emoji_images[self.emoji_id][0]
                     ).grid(row=self.y, column=1)
            self.images_list.append(self.emoji_images[self.emoji_id][0])

            # This label prints the date and time
            tk.Label(
                self.myframe,
                text=f' {datetime.datetime.strptime(self.entry_date, "%Y-%m-%d").strftime("%A %d %b")} '
                     f'  {datetime.datetime.strptime(self.entry_time, "%H:%M:%S").strftime("%I:%M %p")}',
                bg='#FFFDD0',
                fg="black",
                borderwidth=3,
                font=("TkMenuFont", 10)).grid(row=self.y, column=2)

            # This label prints what the emoji actually is, this label
            # also acceces the  array that we defined previously.
            tk.Label(self.myframe,
                     text=self.emoji_images[self.emoji_id][1],
                     font=("TkMenuFont", 14, 'bold'),
                     bg='#FFFDD0',
                     fg='black', ).grid(column=0, row=self.y, pady=40)
