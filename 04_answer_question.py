from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import Image, ImageTk,  ImageFilter
import csv
import time
import datetime
import random

# Create class that acts as a countdown
def countdown(h, m, s):
 
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
 
    return("finished")

def setup_game():

    def generate_question():
        buttons = [answer_a_button, answer_b_button, answer_c_button, answer_d_button]
        question = random.choice(pokemon_list)
        question_picture = Image.open("images/{}.png".format(question))
        # Resize the image using resize() method so it fits in frame
        resized_image = question_picture.resize((475, 475))
        question_picture = ImageTk.PhotoImage(resized_image)

        question_label.config(image=question_picture)
        question_label.image = question_picture

        for i in buttons:
            i.config(text="{}".format(random.choice(pokemon_list)).title())

        answer_button = random.choice(buttons)
        answer_button.config(text=question.title())
        raise_frame(quiz_frame)
        return(answer_button)

    def answer_question(chosen_button, correct_button):
        if chosen_button == correct_button:
            print("correct")
            chosen_button.config(bg="green")
        else:
            print("incorrect")
            chosen_button.config(bg="red")

        countdown(10)
        
        answer = generate_question()
        answer_a_button.config(command= lambda: answer_question(answer_a_button, answer))
        answer_b_button.config(command= lambda: answer_question(answer_b_button, answer))
        answer_c_button.config(command= lambda: answer_question(answer_c_button, answer))
        answer_d_button.config(command= lambda: answer_question(answer_d_button, answer))
        


    with open('pokemon.csv') as file:
        content = file.readlines()

    pokemon_list = []
    for i in content:
        pokemon_list.append(i.strip())

    #region Quiz Frame
    question_num_label = Label(quiz_frame, text="Question X", font=Karmatic_Arcade_subheading, bg="white")
    question_num_label.grid(row=0, column=0, pady=10)

    stats_label = Label(quiz_frame, text="Lives - X\nScore - X", font=Karmatic_Arcade_subheading, bg="white")
    stats_label.grid(row=0, column=1, padx=10, pady=10)

    question_label = Label(quiz_frame, width=475, height=475, background="white")
    question_label.grid(row=1, column=0, pady=50, padx=30)

    answer_button_frame = Frame(quiz_frame, bg="white")
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

    answer = generate_question()

    answer_a_button.config(command= lambda: answer_question(answer_a_button, answer))
    answer_b_button.config(command= lambda: answer_question(answer_b_button, answer))
    answer_c_button.config(command= lambda: answer_question(answer_c_button, answer))
    answer_d_button.config(command= lambda: answer_question(answer_d_button, answer))
    
root = Tk()

#region Variables
# Setup my karmatic arcade font
Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 60, weight = "bold")
Karmatic_Arcade_subheading = tkinter.font.Font(family = "Karmatic Arcade", size = 40, weight = "bold")
Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 18, weight = "normal")
Karmatic_Arcade_text = tkinter.font.Font(family = "Karmatic Arcade", size = 12, weight = "normal")

pokeball_icon = PhotoImage(file="pokeball_icon.gif")
normal_icon = PhotoImage(file="pokeball.gif")
master_icon = PhotoImage(file="masterball.gif")

#endregion

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

# Setup Frames
heading_frame = Frame(bg="white")
heading_frame.grid(row=0, pady=10, sticky="news")
heading_frame.place(anchor="c", relx=.5, rely=0.1)

starting_frame = Frame(pady=80, bg="white")
starting_frame.grid(row=1, column=0, sticky="news")
starting_frame.place(anchor="c", relx=.5, rely=0.6)

difficulty_frame = Frame(pady=80, bg="white")
difficulty_frame.grid(row=1, column=0, sticky="news")
difficulty_frame.place(anchor="c", relx=.5, rely=0.6)

quiz_frame = Frame(bg="white")
quiz_frame.grid(row=1, column=0, sticky="news")
quiz_frame.place(anchor="c", relx=.5, rely=0.6)

raise_frame(heading_frame)
raise_frame(starting_frame)

#region Heading Frame
heading_label = Label(heading_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", background="white", justify=CENTER)
heading_label.grid(row=0)
#endregion

#region Starting Frame
frame_set_size = Label(starting_frame, width=(root.winfo_screenwidth()), bg="white")
frame_set_size.grid(row=0)

pokemon_logo = Label(starting_frame, width = 500, height=500, image=pokeball_icon, background="white")
pokemon_logo.grid(row=1, pady=50)

starting_button_frame = Frame(starting_frame, pady=50, background="white")
starting_button_frame.grid(row=2)

help_button = Button(starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10)
help_button.grid(row=0, column=0, padx=10)

play_button = Button(starting_button_frame, text="Play", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(difficulty_frame))
play_button.grid(row=0, column=1, padx=10)

quit_button = Button(starting_button_frame, text="Quit", font=Karmatic_Arcade_button, width=10, command=quit_game)
quit_button.grid(row=0, column=2, padx=10)
#endregion

#region Difficulty Frame
pokemon_logo = Label(difficulty_frame, font=Karmatic_Arcade_subheading, text="Select Your Difficulty", fg="blue",background="white")
pokemon_logo.grid(row=0, pady=15)

difficulty_button_frame = Frame(difficulty_frame, pady=50, background="white")
difficulty_button_frame.grid(row=1, pady=50)

normal_label = Label(difficulty_button_frame, font=Karmatic_Arcade_subheading, text="Normal", fg="red",background="white")
normal_label.grid(row=0, column=0, padx=20)

master_label = Label(difficulty_button_frame, font=Karmatic_Arcade_subheading, text="Master", fg="purple",background="white")
master_label.grid(row=0, column=1, padx=20)

normal_button = Button(difficulty_button_frame, image=normal_icon, font=Karmatic_Arcade_button, command=setup_game)
normal_button.grid(row=1, column=0, padx=25, pady=5)

master_button = Button(difficulty_button_frame, image=master_icon, font=Karmatic_Arcade_button, command=quit_game)
master_button.grid(row=1, column=1, padx=25, pady=5)
#endregion

# main routine
root.title("Who's That Pokemon?")
root.geometry("1920x1080")
root.config(background="white")
root.state('zoomed')
root.mainloop()
