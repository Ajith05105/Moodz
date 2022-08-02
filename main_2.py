import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import login_page_6
import register_page_7


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title('Moodz')
        self.controller.resizable(False, False)
        self.controller.geometry('550x700+500+0')

        self.bg = Image.open('img/bg.png')
        self.resized = self.bg.resize((550, 700))
        self.new_bg = ImageTk.PhotoImage(self.resized)
        self.img_bg = Label(self, image=self.new_bg)
        self.img_bg.place(x='0', y=0)

        self.sign_up = Image.open('img/sign_up.png')
        self.sign_up_resized = self.sign_up.resize((300, 125))
        self.new_sign_up = ImageTk.PhotoImage(self.sign_up_resized)
        self.sign_up_button = Button(self, image=self.new_sign_up,
                                     cursor='hand2', bg='white', borderwidth='0',
                                     command=lambda: controller.show_frame(register_page_7.Register_page))
        self.sign_up_button.place(x='130', y='415')

        # login button

        self.login = Image.open('img/login.png')
        self.login_resized = self.login.resize((410, 140))
        self.new_login = ImageTk.PhotoImage(self.login_resized)
        self.login_button = Button(self, image=self.new_login, cursor='hand2'
                                   , bg='white', borderwidth='0',
                                   command=lambda: controller.show_frame(login_page_6.Login)
                                   )
        self.login_button.place(x='85', y='535')

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=controller.title_font)

        # putting the grid in its place by using
        # grid
