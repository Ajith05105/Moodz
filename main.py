
from tkinter import *
from PIL import Image, ImageTk


def login_page():
    root.destroy()
    import login_page_5


def sign_up():
    root.destroy()
    import register_page_5


class main_page:

    def __init__(self, root):
        self.root = root
        self.root.title('Moodz')
        self.root.geometry('550x700+500+0')

        # bg image

        self.bg = Image.open('img/bg.png')
        self.resized = self.bg.resize((550, 700))
        self.new_bg = ImageTk.PhotoImage(self.resized)
        self.img_bg = Label(root, image=self.new_bg)
        self.img_bg.place(x='0', y=0)

        # sign up button

        self.sign_up = Image.open('img/sign_up.png')
        self.sign_up_resized = self.sign_up.resize((300, 125))
        self.new_sign_up = ImageTk.PhotoImage(self.sign_up_resized)
        self.sign_up_button = Button(image=self.new_sign_up,
                                     cursor='hand2', bg='white', borderwidth='0',
                                     command=sign_up)
        self.sign_up_button.place(x='130', y='415')

        # login buttonf

        self.login = Image.open('img/login.png')
        self.login_resized = self.login.resize((410, 140))
        self.new_login = ImageTk.PhotoImage(self.login_resized)
        self.login_button = Button(image=self.new_login, cursor='hand2'
                                   , bg='white', borderwidth='0',
                                   command=login_page)
        self.login_button.place(x='85', y='535')


class sign_up_page:

    def __init__(self, root):
        self.root = root
        self.root.title('Moodz')


root = Tk()
obj = main_page(root)
root.mainloop()
