from login_page_4 import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import datetime


# creating a class
class User_logs:

    def __init__(self, root):  # initialise method
        self.root = root
        self.root.title("Moodz")  # title of the window
        self.root.geometry('550x750+500+0')  # geometry of the window
        self.root['bg'] = 'white'  # background colour of the window
        self.images_list = []
        self.y = 0
        self.user_logs()

    def fetching_info(self):
        try:
            con = pymysql.connect(
                host="localhost",
                user="root",
                password="Ajith@05",
                database="pythongui",
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

        self.emoji_images = [('none','none'),(self.new_great_emoji, 'Great'), (self.new_happy_emoji, 'Happy'),
                             (self.new_meh_emoji, 'Meh'), (self.new_sad_emoji, 'Sad'),
                             (self.new_awful_emoji, 'Awful')]

        self.rows = self.fetching_info()
        self.upper_frame = Frame(root, bg='light blue', width=600, height=150)
        self.upper_frame.place(x=0, y=0)

        self.title = Label(self.upper_frame,
                           text=f'Welcome {self.username} \n These are your entries',
                           font=("TkMenuFont", 20, 'bold'),
                           bg='light blue',
                           fg='black')
        self.title.place(x=130, y=30)

        self.entries_frame = Frame(root, bg="light green", width=600, height=900)
        self.entries_frame.place(y=150, x=0)

        for i in self.rows:
            self.y += 90
            self.emoji_id = i[0]
            self.entry_date = str(i[1])
            self.entry_time = str(i[2])
            self.user_id = i[3]

            tk.Label(
                self.entries_frame,
                text=f' {datetime.datetime.strptime(self.entry_date, "%Y-%m-%d").strftime("%A %d %b")} \n \n'
                     f'                 {datetime.datetime.strptime(self.entry_time, "%H:%M:%S").strftime("%I:%M %p")}',
                bg='light green',
                fg="black",
                borderwidth=3,
                font=("TkMenuFont", 10)).place(x=180, y=self.y - 5)

            tk.Label(self.entries_frame,
                     image=self.emoji_images[self.emoji_id][0]
                     ).place(x=90, y=self.y)
            self.images_list.append(self.emoji_images[self.emoji_id][0])

            tk.Label(self.entries_frame,
                     text=self.emoji_images[self.emoji_id][1],
                     font=("TkMenuFont", 14, 'bold'),
                     bg='light green',
                     fg='black', ).place(x=190, y=self.y + 22)


# running the root
root = Tk()
ob = User_logs(root)
root.mainloop()
