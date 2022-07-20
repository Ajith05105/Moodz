import requests
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("900x600")
root.title("Quiz")


def getquiz():
    url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=easy&type=multiple"
    quiz = requests.get(url).json()

    results = quiz["results"]

    questions = []
    my_questions = ""
    options = []
    my_options = ""
    correct_ans = []


    for result in results:
        questions.append(result["question"])
        options.append(result["incorrect_answers"])
        correct_ans.append(result["correct_answer"])



    for i in range(1):
        my_questions = my_questions + questions[i] + "\n"




    print(my_options)
    label.config(text= my_questions)
    button2.config(text= correct_ans[0])
    button3.config(text= options[0][0])
    button4.config(text=options[0][1])
    button5.config(text=options[0][2])







label = tk.Label(root, font = 18, justify = "left")
label.pack(pady= 20)
button2 = tk.Button(root, font='24', )
button2.pack(pady= 20)
button3 = tk.Button(root, font='24', )
button3.pack(pady= 20)
button4 = tk.Button(root, font='24', )
button4.pack(pady= 20)
button5 = tk.Button(root, font='24', )
button5.pack(pady= 20)
button1 = tk.Button(root, text="Play", font='24', command= getquiz)
button1.pack(pady= 20)



getquiz()
root.mainloop()

