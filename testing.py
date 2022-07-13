from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('550x750+500+0')
root['bg'] = 'white'

def make_something(value):
    global x
    x = value




great_emoji = Image.open('img/great_emoji.png')
great_emoji_resized = great_emoji.resize((75, 70))
new_great_emoji = ImageTk.PhotoImage(great_emoji_resized)
img_great_emoji = Button(root, image=new_great_emoji, bd=0, bg='white',command=lambda: make_something(1))
img_great_emoji.place(x=0, y=100)

# feeling happy emoji
happy_emoji = Image.open('img/happy_emoji.png')
happy_emoji_resized = happy_emoji.resize((75, 70))
new_happy_emoji = ImageTk.PhotoImage(happy_emoji_resized)
img_happy_emoji = Button(root, image=new_happy_emoji, bd=0, bg='white',command=lambda: make_something(2))
img_happy_emoji.place(x=80, y=100)

# feeling meh emoji
meh_emoji = Image.open('img/meh_emoji.png')
meh_emoji_resized = meh_emoji.resize((75, 70))
new_meh_emoji = ImageTk.PhotoImage(meh_emoji_resized)
img_meh_emoji = Button(root, image=new_meh_emoji, bd=0, bg='white',command=lambda: make_something(3))
img_meh_emoji.place(x=165, y=100)

# feeling sad emoji
sad_emoji = Image.open('img/sad_emoji.png')
sad_emoji_resized = sad_emoji.resize((75, 70))
new_sad_emoji = ImageTk.PhotoImage(sad_emoji_resized)
img_sad_emoji = Button(root, image=new_sad_emoji, bd=0, bg='white',command=lambda: make_something(4))
img_sad_emoji.place(x=250, y=100)

# feeling awful emoji
awful_emoji = Image.open('img/awful_emoji.png')
awful_emoji_resized = awful_emoji.resize((75, 70))
new_awful_emoji = ImageTk.PhotoImage(awful_emoji_resized)
img_awful_emoji = Button(root, image=new_awful_emoji, bd=0, bg='white', command=lambda: make_something(5))
img_awful_emoji.place(x=335, y=100)

emoi_dictionary = {new_great_emoji: 1,
                   new_happy_emoji: 2,
                   new_meh_emoji: 3,
                   new_sad_emoji: 4,
                   new_awful_emoji: 5}



def assigning_emoji_values():
    global emoji_input_number
    if x == 1:
        emoji_input_number = emoi_dictionary.get(new_great_emoji)

    elif x ==2:
        emoji_input_number = emoi_dictionary.get(new_happy_emoji)

    elif x == 3:
        emoji_input_number = emoi_dictionary.get(new_meh_emoji)

    elif x ==4:
        emoji_input_number = emoi_dictionary.get(new_sad_emoji)

    elif x ==4:
        emoji_input_number = emoi_dictionary.get(new_awful_emoji)

    print (emoji_input_number)

assigning_emoji_values()


root.mainloop()
