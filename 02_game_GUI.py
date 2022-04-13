from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import Image, ImageTk,  ImageFilter
import csv
import time
import random

root = Tk()

# Setup my karmatic arcade font
Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 60, weight = "bold")
Karmatic_Arcade_subheading = tkinter.font.Font(family = "Karmatic Arcade", size = 40, weight = "bold")
Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 18, weight = "normal")
Karmatic_Arcade_text = tkinter.font.Font(family = "Karmatic Arcade", size = 12, weight = "normal")

pokeball_icon = PhotoImage(file="pokeball_icon.gif")
normal_icon = PhotoImage(file="pokeball.gif")
master_icon = PhotoImage(file="masterball.gif")
# Resize the image using resize() method


pokemon_list = []
dataset = open("pokemon.csv")
csvreader = csv.reader(dataset)
for row in csvreader:
    pokemon_list.append(row)

dataset.close()

def raise_frame(frame):
    frame.tkraise()

def quit_game():
        root.destroy()

def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		time.sleep(1)
		t -= 1
	
	return("finished")

def generate_question(list, a, b, c, d):
    buttons = [a,b,c,d]
    question = random.choice(list)
    question_picture = Image.open("images/{}.png".format(question))
    resized_image = question_picture.resize((600, 600))
    question_picture = ImageTk.PhotoImage(resized_image)

    for i in buttons:
        i.config(text="{}".format(random.choice(list)).title())

    correct_button = random.choice(buttons)
    correct_button.config(text="question".title())


    return question_picture


def answer_question(button_pressed, correct_button):

    if button_pressed == correct_button:
        print("correct")
        button_pressed.config(bg="green")
    else:
        print("incorrect")
        button_pressed.config(bg="red")
        correct_button.config(bg="green")


# Setup Frames
heading_frame = Frame(bg="white")
heading_frame.grid(row=0, pady=10, sticky="news")
heading_frame.place(anchor="c", relx=.5, rely=0.1)

starting_frame = Frame(pady=80, bg="white")
starting_frame.grid(row=1, column=0, sticky="news")
starting_frame.place(anchor="c", relx=.5, rely=0.6)

quiz_frame = Frame(pady=30, bg="white")
quiz_frame.grid(row=1, column=0, sticky="news")
quiz_frame.place(anchor="c", relx=.5, rely=0.6)

raise_frame(heading_frame)
raise_frame(quiz_frame)

#region Heading Frame
heading_label = Label(heading_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", background="white", justify=CENTER)
heading_label.grid(row=0)
#endregion

#region Starting Frame
pokemon_logo = Label(starting_frame, width = 500, height=500, image=pokeball_icon, background="white")
pokemon_logo.grid(row=0, pady=50)

starting_button_frame = Frame(starting_frame, pady=50, background="white")
starting_button_frame.grid(row=1)

help_button = Button(starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10)
help_button.grid(row=0, column=0, padx=10)

play_button = Button(starting_button_frame, text="Play", font=Karmatic_Arcade_button, width=10, command=play_game)
play_button.grid(row=0, column=1, padx=10)

quit_button = Button(starting_button_frame, text="Quit", font=Karmatic_Arcade_button, width=10, command=quit_game)
quit_button.grid(row=0, column=2, padx=10)
#endregion

#region Quiz Frame
question_num_label = Label(quiz_frame, text="Question X", font=Karmatic_Arcade_subheading, bg="white")
question_num_label.grid(row=0, column=0, pady=10)

stats_label = Label(quiz_frame, text="Lives - X\nScore - X", font=Karmatic_Arcade_subheading, bg="white")
stats_label.grid(row=0, column=1, padx=10, pady=10)

question_label = Label(quiz_frame, width=600, height=600, background="black")
question_label.grid(row=1, column=0, pady=50, padx=30)

answer_button_frame = Frame(quiz_frame)
answer_button_frame.grid(row=1, column=1, pady=30, padx=50)

answer_a_button = Button(answer_button_frame, text="A", font=Karmatic_Arcade_button, width=20, height=5)
answer_a_button.grid(row=0, column=0, pady=20, padx=20)

answer_b_button = Button(answer_button_frame, text="B", font=Karmatic_Arcade_button, width=20, height=5)
answer_b_button.grid(row=0, column=1, pady=20, padx=20)

answer_c_button = Button(answer_button_frame, text="C", font=Karmatic_Arcade_button, width=20, height=5)
answer_c_button.grid(row=1, column=0, pady=20, padx=20)

answer_d_button = Button(answer_button_frame, text="D", font=Karmatic_Arcade_button, width=20, height=5)
answer_d_button.grid(row=1, column=1, pady=20, padx=20)

#endregion

# main routine
root.title("Who's That Pokemon?")
root.geometry("1920x1080")
root.config(background="white")
root.state('zoomed')
root.mainloop()
