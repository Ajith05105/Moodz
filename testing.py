from tkinter import *
import tkinter as tk
from PIL import ImageTk
import pymysql


bg_colour = "#3d6466"


def fetch_db():
    global emoji_id, user_id, entry_time, entry_date,rows
    try:
        con = pymysql.connect(
            host="localhost",
            user="root",
            password="Ajith@05",
            database="pythongui",
        )

        cur = con.cursor()
        cur.execute(
            "SELECT * FROM entry_info"
        )

        rows = cur.fetchall()
        for i in rows:
            emoji_id = i[0]
            entry_date = str(i[1])
            entry_time = str(i[2])
            user_id = i[3]
            print(
                f'( emoji_id = {emoji_id}, entry_date = {entry_date}, entry_time = {entry_time}, UserId = {user_id} )')
        con.close()
        return emoji_id, entry_date, entry_time, user_id,rows





    except Exception as es:

        print(

            f"Error due to:{str(es)}"

        )


def load_frame2():
    frame2.tkraise()
    emoji_id, entry_date, entry_time, user_id,rows = fetch_db()

    logo_img = ImageTk.PhotoImage(file='img/sad_emoji.png')
    logo_widget = tk.Label(frame2, image=logo_img)
    logo_widget.img = logo_img
    logo_widget.pack()

    tk.Label(
        frame2,
        text="no",
        bg=bg_colour,
        fg="White",
        font=("TkMenuFont", 14)).pack()

    for i in rows:
        tk.Label(
            frame2,
            text=entry_time,
            bg=bg_colour,
            fg="White",
            font=("TkMenuFont", 14)).pack()



def load_frame1():
    frame1.tkraise()
    frame1.pack_propagate(False)
    # frame 1 widgets
    logo_img = ImageTk.PhotoImage(file='img/great_emoji.png')
    logo_widget = tk.Label(frame1, image=logo_img)
    logo_widget.img = logo_img
    logo_widget.pack()

    tk.Label(
        frame1,
        text="ready for your random recipe",
        bg=bg_colour,
        fg="White",
        font=("TkMenuFont", 14)).pack()

    tk.Button(
        frame1,
        text="shuffle",
        bg="#28393a",
        fg='white',
        cursor='hand2',
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame2()).pack()


root = Tk()
root.title = "testing"
root.geometry("500x500+500+0")

frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()

root.mainloop()
