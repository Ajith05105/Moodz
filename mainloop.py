import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import Page_1
import Page_2
import main_page


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family = 'Helvetica', size = 18, weight = 'bold', slant = "italic")

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (main_page.StartPage, Page_1.Page1, Page_2.Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main_page.StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



# first window frame startpage


# second window frame page1


# third window frame page2


# Driver Code
app = tkinterApp()
app.mainloop()
