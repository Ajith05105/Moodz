import tkinter as tk
from tkinter import ttk
import Page_1
import main_page


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font = controller.title_font)
        label.grid(row=0, column=4, padx=10, pady=10)
