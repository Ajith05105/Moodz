import tkinter as tk
from tkinter import ttk
import main_page
import Page_2

class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'red')
        label = ttk.Label(self, text="Page 1", font = controller.title_font)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(main_page.StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page_2.Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)
