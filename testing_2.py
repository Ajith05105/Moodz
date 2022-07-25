from tkinter import *
from tkinter import ttk

root = Tk()
root.title("scrolling bar")
root.geometry("500x500")
root.resizable(False,False)

wrapper1 = LabelFrame(root, highlightbackground='black')

wrapper2 = LabelFrame(root, highlightbackground='black')
wrapper3 = LabelFrame(root, highlightbackground='black')

mycanvas = Canvas(wrapper2)
mycanvas.pack(side = LEFT)

yscrollbar = ttk.Scrollbar(wrapper2, orient="vertical", command= mycanvas.yview)
yscrollbar.pack(side = RIGHT,fill = "y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e:mycanvas.configure(scrollregion=mycanvas.bbox("all")))

myframe = Frame(mycanvas)
mycanvas.create_window((200,0), window=myframe, anchor="nw")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)

y= 0
for i in range(20):
    y+=20
    Button(myframe,text= f"my button {i}").grid(row = y, column = 0,pady =10)

root.mainloop()
