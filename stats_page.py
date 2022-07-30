from login_page_4 import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import pymysql
import datetime


# creating a class
class stats_page:

    def __init__(self, root):  # initialise method
        self.root = root
        self.root.title("Moodz")  # title of the window
        self.root.geometry('550x700+500+0')  # geometry of the window
        self.root['bg'] = 'white'  # background colour of the window
        self.images_list = []
        self.root.resizable = (False, False)
        self.y = 0


    def fetching_info(self):
        pass
