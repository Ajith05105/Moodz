from login_page_4 import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import datetime


class Appscreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Moodz")
        self.root.geometry('550x750+500+0')
        self.root.resizable(False, False)
        self.root['bg'] = 'white'
        self.images_list = []
        self.x = 0
        self.appscreen()

    def make_something(self, value):
        self.x = value

    def appscreen(self):
        emoji_frame = LabelFrame(self.root, width=450, height=70, fg='black', bd=0, bg='white')
        emoji_frame.place(y=210, x=60)

        # emoji bar
        Login.creating_image(self, 'emoji_bar', 300, 560, 0, 390)

        # calendar icon
        Login.creating_image(self, 'img_1', 40, 40, 110, 122)
        # feeling great emoji
        self.great_emoji = Image.open('img/great_emoji.png')
        self.great_emoji_resized = self.great_emoji.resize((75, 70))
        self.new_great_emoji = ImageTk.PhotoImage(self.great_emoji_resized)
        img_great_emoji = Button(emoji_frame, image=self.new_great_emoji,
                                 bd=0, bg='white',
                                 command=lambda: [self.make_something(1),
                                                  self.assigning_emoji_values(),
                                                  self.fetching_login_info(),
                                                  self.entering_info_into_entry_table(),
                                                  self.user_log()])
        img_great_emoji.place(x=0, y=0)

        # feeling happy emoji
        self.happy_emoji = Image.open('img/happy_emoji.png')
        self.happy_emoji_resized = self.happy_emoji.resize((75, 70))
        self.new_happy_emoji = ImageTk.PhotoImage(self.happy_emoji_resized)
        img_happy_emoji = Button(emoji_frame, image=self.new_happy_emoji, bd=0,
                                 bg='white',
                                 command=lambda: [self.make_something(2),
                                                  self.assigning_emoji_values(),
                                                  self.fetching_login_info(),
                                                  self.entering_info_into_entry_table(),
                                                  self.user_log()])
        img_happy_emoji.place(x=80, y=0)

        # feeling meh emoji
        self.meh_emoji = Image.open('img/meh_emoji.png')
        self.meh_emoji_resized = self.meh_emoji.resize((75, 70))
        self.new_meh_emoji = ImageTk.PhotoImage(self.meh_emoji_resized)
        img_meh_emoji = Button(emoji_frame, image=self.new_meh_emoji, bd=0, bg='white',
                               command=lambda: [self.make_something(3),
                                                self.assigning_emoji_values(),
                                                self.fetching_login_info(),
                                                self.entering_info_into_entry_table(),
                                                self.user_log()])
        img_meh_emoji.place(x=165, y=0)

        # feeling sad emoji
        self.sad_emoji = Image.open('img/sad_emoji.png')
        self.sad_emoji_resized = self.sad_emoji.resize((75, 70))
        self.new_sad_emoji = ImageTk.PhotoImage(self.sad_emoji_resized)
        img_sad_emoji = Button(emoji_frame,
                               image=self.new_sad_emoji,
                               bd=0,
                               bg='white',
                               command=lambda: [self.make_something(4),
                                                self.assigning_emoji_values(),
                                                self.fetching_login_info(),
                                                self.entering_info_into_entry_table(),
                                                self.user_log()])
        img_sad_emoji.place(x=250, y=0)

        # feeling awful emoji
        self.awful_emoji = Image.open('img/awful_emoji.png')
        self.awful_emoji_resized = self.awful_emoji.resize((75, 70))
        self.new_awful_emoji = ImageTk.PhotoImage(self.awful_emoji_resized)
        img_awful_emoji = Button(emoji_frame, image=self.new_awful_emoji, bd=0, bg='white',
                                 command=lambda: [self.make_something(5),
                                                  self.assigning_emoji_values(),
                                                  self.fetching_login_info(),
                                                  self.entering_info_into_entry_table(),
                                                  self.user_log()])
        img_awful_emoji.place(x=335, y=0)

        self.emoji_dictionary = {self.new_great_emoji: 1,
                                 self.new_happy_emoji: 2,
                                 self.new_meh_emoji: 3,
                                 self.new_sad_emoji: 4,
                                 self.new_awful_emoji: 5}

        label_1 = Label(
            self.root,
            text="How are you ?",
            font=("Bauhaus 93", 36),
            fg="#ffb772",
            bg="white", )
        label_1.place(x=120, y=50)

        self.now = datetime.datetime.now()
        month = str(self.now.month)
        day = self.now.day
        current_time = self.now.strftime("%I:%M %p")

        month_num = month
        datetime_object = datetime.datetime.strptime(month_num, "%m")

        month_name = datetime_object.strftime("%b")

        date_time_label = Label(self.root,
                                text=f'Today {day} {month_name} {current_time}',
                                bg='white',
                                fg="#cd745b",
                                font=("Bauhaus 93", 19)
                                )
        date_time_label.place(x=160, y=125)

    @staticmethod
    def login_page(self):
        root.destroy()
        import login_page_4

    def assigning_emoji_values(self):
        if self.x == 1:
            self.emoji_entry = self.emoji_dictionary.get(self.new_great_emoji)
        if self.x == 2:
            self.emoji_entry = self.emoji_dictionary.get(self.new_happy_emoji)
        if self.x == 3:
            self.emoji_entry = self.emoji_dictionary.get(self.new_meh_emoji)
        if self.x == 4:
            self.emoji_entry = self.emoji_dictionary.get(self.new_sad_emoji)
        if self.x == 5:
            self.emoji_entry = self.emoji_dictionary.get(self.new_awful_emoji)

    def fetching_login_info(self):
        try:
            con = pymysql.connect(
                host="localhost",
                user="root",
                password="Ajith@05",
                database="pythongui",
            )

            cur = con.cursor()
            cur_2 = con.cursor()
            cur.execute(
                "select * from user_logins "
            )
            rows = cur.fetchall()
            self.username = rows[len(rows) - 1]

            cur_2.execute(
                "SELECT `UserId` FROM master_register WHERE `username`=%s",
                (self.username),
            )
            self.user_id = cur_2.fetchone()
            con.commit()
            con.close()

        except Exception as es:

            messagebox.showerror(

                "Error", f"Error due to:{str(es)}", parent=self.root

            )

    def user_log(self):
        root.destroy()
        import user_log3

    def entering_info_into_entry_table(self):
        try:
            con = pymysql.connect(
                host="localhost",
                user="root",
                password="Ajith@05",
                database="pythongui",
            )

            cur = con.cursor()
            cur.execute(
                "insert into  entry_info (emoji_id,entry_date,entry_time,UserId,username) values (%s,%s,%s,%s,%s)",
                (self.emoji_entry, self.now.date(), self.now.strftime("%H:%M:%S"), self.user_id,self.username),
            )
            con.commit()
            con.close()

        except Exception as es:

            messagebox.showerror(

                "Error", f"Error due to:{str(es)}", parent=self.root

            )


root = Tk()
ob = Appscreen(root)
root.mainloop()
