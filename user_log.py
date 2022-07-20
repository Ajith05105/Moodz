from login_page_4 import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import datetime


class User_logs:
    def __init__(self, root):
        self.root = root
        self.root.title("Moodz")
        self.root.geometry('550x750+500+0')

        self.root['bg'] = 'white'
        self.images_list = []
        self.x = 0
        self.user_logs()
        self.load_frame2()

    def fetch_db(self):
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
            self.username = self.results[len(self.results) - 1]

            cur.execute(
                "select emoji_id,entry_date,entry_time,UserId from entry_info where username = %s",
                (self.username)
            )

            self.rows = cur.fetchall()
            return self.rows


        except Exception as es:

            print(

                f"Error due to:{str(es)}"

            )

    def load_frame2(self):
        self.frame2.tkraise()
        self.rows = self.fetch_db()

        for i in self.rows:
            self.emoji_id = i[0]
            self.entry_date = str(i[1])
            self.entry_time = str(i[2])
            self.user_id = i[3]

            def creating_image():
                if self.emoji_id == 1:
                    self.great_image = tk.PhotoImage(file="img/great_emoji.png")
                    tk.Label(
                        self.frame2,
                        image=self.great_image
                    ).pack()
                    self.images_list.append(self.great_image)
                    return tk.Label
                if self.emoji_id == 4:
                    self.sad_image = tk.PhotoImage(file="img/sad_emoji.png")
                    tk.Label(
                        self.frame2,
                        image=self.sad_image
                    ).pack()
                    self.images_list.append(self.sad_image)
                    return tk.Label
                if self.emoji_id == 5:
                    self.awful_image = tk.PhotoImage(file="img/awful_emoji.png")
                    tk.Label(
                        self.frame2,
                        image=self.awful_image
                    ).pack(side=tk.LEFT)
                    self.images_list.append(self.awful_image)
                    return tk.Label
                if self.emoji_id == 3:
                    self.meh_image = tk.PhotoImage(file="img/meh_emoji.png")
                    tk.Label(
                        self.frame2,
                        image=self.meh_image
                    ).pack()
                    self.images_list.append(self.meh_image)
                    return tk.Label
                if self.emoji_id == 2:
                    self.happy_image = tk.PhotoImage(file="img/happy_emoji.png")
                    tk.Label(
                        self.frame2,
                        image=self.happy_image
                    ).pack()
                    self.images_list.append(self.happy_image)
                    return tk.Label

            creating_image()

            tk.Label(
                self.frame2,
                text=f' {datetime.datetime.strptime(self.entry_date, "%Y-%m-%d").strftime("%A %d %b")} \n '
                     f' {datetime.datetime.strptime(self.entry_time, "%H:%M:%S").strftime("%I:%M %p")}',
                bg='light blue',
                fg="black",
                font=("TkMenuFont", 14)).pack()

    def user_logs(self):

        self.frame2 = tk.Frame(root, bg='light blue')

        self.frame2.place(x=150, y=0)


root = Tk()
ob = User_logs(root)
root.mainloop()
