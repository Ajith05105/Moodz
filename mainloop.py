import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import font as tkfont
import main_2
import login_page_6
import register_page_7
import index_4
import user_log_5
import pymysql



class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family = 'Helvetica', size = 18, weight = 'bold', slant = "italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (main_2.StartPage,
                  login_page_6.Login,
                  register_page_7.Register_page,
                  index_4.home_page,
                  user_log_5.Log
                  ):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main_2.StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



# first window frame startpage


# second window frame page1


# third window frame page2

if __name__ == "__main__":
# Driver Code
    app = tkinterApp()
    app.mainloop()
