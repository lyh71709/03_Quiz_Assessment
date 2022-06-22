# Get hard difficulty working
# Blur images and set lives to 1

from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import Image, ImageTk, ImageFilter
import os
import random

lives = 3
score = 0
question_num = 0

correct_list = []
incorrect_list = []

def game_over():

    raise_frame(gameover_frame)

    #region Gameover Frame

    gameover_label = Label(gameover_frame, text="Game Over", font=Karmatic_Arcade_heading, bg="white", fg="red", width=100)
    gameover_label.grid(row=0, column=0, pady=15)

    stats_frame = Label(gameover_frame, bg="white")
    stats_frame.grid(row=1, pady=20)
    
    correct_listbox_label = Label(stats_frame, text="Pokemon you got", font=Karmatic_Arcade_big_text, fg="green", bg="white")
    correct_listbox_label.grid(row=0, column=0)

    gameover_stats_label = Label(stats_frame, text="Score - {} \nQuestions - {}".format(score, question_num), font=Karmatic_Arcade_big_text, bg="white")
    gameover_stats_label.grid(row=0, column=1, padx=40)

    incorrect_listbox_label = Label(stats_frame, text="Pokemon you forgot", font=Karmatic_Arcade_big_text, fg="orange", bg="white")
    incorrect_listbox_label.grid(row=0, column=2)

    correct_list_var = StringVar(value=correct_list)
    correct_listbox = Listbox(stats_frame, listvariable=correct_list_var, font=Karmatic_Arcade_small_text, height=20, borderwidth=0, highlightthickness=0.5)
    correct_listbox.grid(row=1, column=0, pady=10)

    sad_pikachu_label = Label(stats_frame, image=sad_pikachu, bg="black")
    sad_pikachu_label.grid(row=1, column=1)

    incorrect_list_var = StringVar(value=incorrect_list)
    incorrect_listbox = Listbox(stats_frame, listvariable=incorrect_list_var, font=Karmatic_Arcade_small_text, height=20, borderwidth=0, highlightthickness=0.5)
    incorrect_listbox.grid(row=1, column=2)

    export_button = Button(stats_frame, text="Export", font=Karmatic_Arcade_button)
    export_button.grid(row=2, column=0, pady=10)

    play_again_button = Button(stats_frame, text="Play Again", font=Karmatic_Arcade_button, command=restart)
    play_again_button.grid(row=2, column=1)

    quit_button = Button(stats_frame, text="Quit", font=Karmatic_Arcade_button, command=quit_game)
    quit_button.grid(row=2, column=2)
    #endregion


# Actual Game
def setup_game(difficulty):
    global lives

    # Generate the question and alters the answers
    def generate_question():
        global question_num
        
        for i in buttons:
            i.config(state=NORMAL)

        question_num = question_num + 1
        question_num_label.config(text="Question {}".format(question_num))

        # Randomly select pokemon
        question = random.choice(pokemon_list)
        # Finds the image of pokemon
        question_picture = Image.open("images/{}.png".format(question))
        # Resize the image using resize() method so it fits in frame
        resized_image = question_picture.resize((400, 400))
        # Blurs Image if user is on Master difficulty
        if difficulty == "master":
            resized_image = resized_image.filter(ImageFilter.GaussianBlur(radius=15))
        question_picture = ImageTk.PhotoImage(resized_image)
        

        question_label.config(image=question_picture)
        question_label.image = question_picture

        # Removes the pokemon from list so we won't have duplicates
        pokemon_list.remove(question)

        # Change the buttons back to default
        for i in buttons:
            i.config(text="{}".format(random.choice(pokemon_list)).title(), bg="SystemButtonFace")

        # Selects one button to be the actual answer
        answer_button = random.choice(buttons)
        answer_button.config(text=question.title())
        raise_frame(quiz_frame)
        # Gets rid of continue_button
        continue_button.grid_forget()

        # Bind all buttons for answer function
        answer_a_button.config(command= lambda: answer_question(answer_a_button, answer_button))
        answer_b_button.config(command= lambda: answer_question(answer_b_button, answer_button))
        answer_c_button.config(command= lambda: answer_question(answer_c_button, answer_button))
        answer_d_button.config(command= lambda: answer_question(answer_d_button, answer_button))

    # When user answers question
    def answer_question(chosen_button, correct_button):
        global lives, score

        for i in buttons:
            i.config(state=DISABLED)
    
        # Checks if user got question right or wrong
        if chosen_button == correct_button:
            print("correct")
            chosen_button.config(bg="green")
            correct_list.append(correct_button.cget('text'))
            score += 1
        else:
            print("incorrect")
            chosen_button.config(bg="red")
            correct_button.config(bg="green")
            incorrect_list.append(correct_button.cget('text'))
            lives -= 1

        game_stats_label.config(text="Lives - {}\nScore - {}".format(lives, score))

        if lives <= 0:
            game_over()


        # Makes continue button reappear
        continue_button.grid(row=2, column=1)
        continue_button.config(command=generate_question)
    
    # Use CSV to make a list
    with open('pokemon.csv') as file:
        content = file.readlines()

    pokemon_list = []
    # Strip unwanted characters from data
    for i in content:
        pokemon_list.append(i.strip())

    # Difficulty condition (set lives to 1)
    if difficulty == "master":
        lives = lives - 2

    #region Quiz Frame

    question_num_label = Label(quiz_frame, text="Question {}".format(question_num), font=Karmatic_Arcade_subheading, bg="white")
    question_num_label.grid(row=0, column=0)

    game_stats_label = Label(quiz_frame, text="Lives - {}\nScore - {}".format(lives, score), font=Karmatic_Arcade_subheading, bg="white")
    game_stats_label.grid(row=0, column=1, padx=5)

    question_label = Label(quiz_frame, background="white")
    question_label.grid(row=1, column=0, padx=20)

    answer_button_frame = Frame(quiz_frame, bg="white")
    answer_button_frame.grid(row=1, column=1, padx=40)

    answer_a_button = Button(answer_button_frame, text="A", font=Karmatic_Arcade_button, width=20, height=5)
    answer_a_button.grid(row=0, column=0, pady=20, padx=20)

    answer_b_button = Button(answer_button_frame, text="B", font=Karmatic_Arcade_button, width=20, height=5)
    answer_b_button.grid(row=0, column=1, pady=20, padx=20)

    answer_c_button = Button(answer_button_frame, text="C", font=Karmatic_Arcade_button, width=20, height=5)
    answer_c_button.grid(row=1, column=0, pady=20, padx=20)

    answer_d_button = Button(answer_button_frame, text="D", font=Karmatic_Arcade_button, width=20, height=5)
    answer_d_button.grid(row=1, column=1, pady=20, padx=20)

    continue_button = Button(quiz_frame, text="Continue", font=Karmatic_Arcade_button, width=20, height=2)
    continue_button.grid(row=2, column=1)

    quit_button = Button(quiz_frame, text="Leave Game", font=Karmatic_Arcade_button, width=20, height=2, command=game_over)
    quit_button.grid(row=2, column=0)
    #endregion

    buttons = [answer_a_button, answer_b_button, answer_c_button, answer_d_button]
    generate_question()


root = Tk()

#region Variables
# Setup my karmatic arcade font
Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 50, weight = "bold")
Karmatic_Arcade_subheading = tkinter.font.Font(family = "Karmatic Arcade", size = 30, weight = "bold")
Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 16, weight = "normal")
Karmatic_Arcade_small_text = tkinter.font.Font(family = "Karmatic Arcade", size = 10, weight = "normal")
Karmatic_Arcade_big_text = tkinter.font.Font(family = "Karmatic Arcade", size = 20, weight = "normal")

# Set up images
pokeball_icon = PhotoImage(file="pokeball_icon(resized).gif")
normal_icon = PhotoImage(file="pokeball.gif")
master_icon = PhotoImage(file="masterball.gif")
sad_pikachu = PhotoImage(file="sad_pikachu.gif")


#endregion

# Restarts the Whole Window 
# only works if program file ends in .pyw
# That's why play again will only work on final program
def restart():
    root.destroy()
    os.startfile(".pyw")
# Bring frame to the top
def raise_frame(frame):
    frame.tkraise()
# Exit Game
def quit_game():
        root.destroy()

# Setup Frames
heading_frame = Frame(bg="white")
heading_frame.grid(row=0, sticky="news")
heading_frame.place(anchor="c", relx=.5, rely=0.1)

starting_frame = Frame(bg="white")
starting_frame.grid(row=1, column=0, sticky="news")
starting_frame.place(anchor="c", relx=.5, rely=0.55)

difficulty_frame = Frame(bg="white")
difficulty_frame.grid(row=1, column=0, sticky="news")
difficulty_frame.place(anchor="c", relx=.5, rely=0.6)

quiz_frame = Frame(bg="white")
quiz_frame.grid(row=1, column=0, sticky="news")
quiz_frame.place(anchor="c", relx=.5, rely=0.58)

gameover_frame = Frame(bg="white")
gameover_frame.grid(row=1, column=0, sticky="news")
gameover_frame.place(anchor="c", relx=.5, rely=0.6)

# Raises the inital frame
raise_frame(heading_frame)
raise_frame(starting_frame)

#region Heading Frame
heading_label = Label(heading_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", background="white", justify=CENTER)
heading_label.grid(row=0)
#endregion

#region Starting Frame
pokemon_logo = Label(starting_frame, image=pokeball_icon, background="white", width=1000)
pokemon_logo.grid(row=0, pady=20)

starting_button_frame = Frame(starting_frame, background="white")
starting_button_frame.grid(row=1, pady=10)

help_button = Button(starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10)
help_button.grid(row=0, column=0, padx=10)

play_button = Button(starting_button_frame, text="Play", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(difficulty_frame))
play_button.grid(row=0, column=1, padx=10)

quit_button = Button(starting_button_frame, text="Quit", font=Karmatic_Arcade_button, width=10, command=quit_game)
quit_button.grid(row=0, column=2, padx=10)
#endregion

#region Difficulty Frame
pokemon_logo = Label(difficulty_frame, font=Karmatic_Arcade_subheading, text="Select Your Difficulty", fg="blue",background="white")
pokemon_logo.grid(row=0, pady=50)

difficulty_button_frame = Frame(difficulty_frame, pady=50, background="white")
difficulty_button_frame.grid(row=1, pady=50)

normal_label = Label(difficulty_button_frame, font=Karmatic_Arcade_subheading, text="Normal", fg="red",background="white")
normal_label.grid(row=0, column=0, padx=20)

master_label = Label(difficulty_button_frame, font=Karmatic_Arcade_subheading, text="Master", fg="purple",background="white")
master_label.grid(row=0, column=1, padx=20)

normal_button = Button(difficulty_button_frame, image=normal_icon, command=lambda: setup_game("normal"))
normal_button.grid(row=1, column=0, padx=25, pady=5)

master_button = Button(difficulty_button_frame, image=master_icon, command=lambda: setup_game("master"))
master_button.grid(row=1, column=1, padx=25, pady=5)
#endregion

# main routine
root.title("Who's That Pokemon?")
root.geometry("1280x720")
root.config(background="white")
# Makes game fullscreen
# root.state('zoomed')
root.mainloop()
