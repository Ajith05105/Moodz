import tkinter as tk
from tkinter import ttk
import Page_2
import Page_1


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller
        self.controller.title('moodz')
        self.controller.geometry('550x700+500+0')

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font = controller.title_font)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)
        ttk.Label(self, text="IDK").grid(row=4, column=5)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page_1.Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page_2.Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)
