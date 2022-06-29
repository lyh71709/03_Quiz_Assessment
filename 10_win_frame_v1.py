# Add a win screen
# Allow the game to finish no matter how rare

from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import Image, ImageTk, ImageFilter
import os
import random
import re

# Game Over screen
def game_over(win_or_loss):
    # Removes any pre exising widgets
    for widgets in gameover_frame.winfo_children():
        widgets.destroy()

    raise_frame(gameover_frame)

    #region Gameover Frame
    gameover_label = Label(gameover_frame, text="Game Over", font=Karmatic_Arcade_subheading, bg="white", fg="red", width=100)
    gameover_label.grid(row=0, column=0, pady=15)
    if win_or_loss == "win":
        gameover_label.config(text="Congratulations!", fg="blue")

    stats_frame = Label(gameover_frame, bg="white")
    stats_frame.grid(row=1, pady=20)

    correct_listbox_label = Label(stats_frame, text="   Pokemon you got    ", font=Karmatic_Arcade_big_text, fg="green", bg="white")
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
    if win_or_loss == "win":
        sad_pikachu_label.config(image=happy_pikachu)

    incorrect_list_var = StringVar(value=incorrect_list)
    incorrect_listbox = Listbox(stats_frame, listvariable=incorrect_list_var, font=Karmatic_Arcade_small_text, height=20, borderwidth=0, highlightthickness=0.5)
    incorrect_listbox.grid(row=1, column=2)

    export_button = Button(stats_frame, text="Export", font=Karmatic_Arcade_button, command=export)
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

        # Checks if possible_questions is empty
        if not possible_questions:
            game_over("win")

        else:
            # Randomly select pokemon
            question = random.choice(possible_questions)
            # Finds the image of pokemon
            question_picture = Image.open("images/{}.png".format(question))
            # Resize the image using resize() method so it fits in frame
            resized_image = question_picture.resize((400, 400))
       
            # Blurs Image if user is on Master difficulty
            if difficulty == "master":
                resized_image = resized_image.filter(ImageFilter.GaussianBlur(radius=15))
            question_picture = ImageTk.PhotoImage(resized_image)
        
            # Update picture with the picture of chosen pokemon
            question_label.config(image=question_picture)
            question_label.image = question_picture

            # Removes the pokemon from the possible questions list so we won't have duplicate questions
            possible_questions.remove(question)

            # Removes the question from pokemon list to remove the possibility of a non correct button to have the chosen pokemon's name on it
            pokemon_list.remove(question)
            # Selects 4 random pokemon without repeats
            possible_button_names = random.sample(pokemon_list, 4)
            # Re adds the chosen pokemon's name to the list
            pokemon_list.append(question)

            # Bg set to "SystemButtonFace" to restore default and replace the text on button with randomly generated name
            answer_a_button.config(text="{}".format(possible_button_names[0]).title(), bg="SystemButtonFace")
            answer_b_button.config(text="{}".format(possible_button_names[1]).title(), bg="SystemButtonFace")
            answer_c_button.config(text="{}".format(possible_button_names[2]).title(), bg="SystemButtonFace")
            answer_d_button.config(text="{}".format(possible_button_names[3]).title(), bg="SystemButtonFace")

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
            game_over("loss")

        # Makes continue button reappear
        continue_button.grid(row=2, column=1)
        continue_button.config(command=generate_question)
    
    # Use CSV to make a list
    with open('pokemon.csv') as file:
        content = file.readlines()

    # Make lists smaller for testing purposes
    pokemon_list = ["bulbasaur", "charmander", "squirtle", "charizard", "venusaur", "blastoise"]
    possible_questions = ["bulbasaur", "charmander", "squirtle", "charizard", "venusaur", "blastoise"]
    
    # pokemon_list = []
    # # Strip unwanted characters from data
    # for i in content:
    #     pokemon_list.append(i.strip())

    # Difficulty condition (set lives to 1)
    if difficulty == "master":
        lives = lives - 2

    #region Quiz Frame

    question_num_label = Label(quiz_frame, text="Question {}".format(question_num), font=Karmatic_Arcade_subheading, bg="white")
    question_num_label.grid(row=0, column=0)

    game_stats_label = Label(quiz_frame, text="Lives - {}\nScore - {}".format(lives, score), font=Karmatic_Arcade_big_text, bg="white")
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

    quit_button = Button(quiz_frame, text="Leave Game", font=Karmatic_Arcade_button, width=20, height=2, command=lambda: game_over("loss"))
    quit_button.grid(row=2, column=0)
    #endregion

    # Set up a list of buttons for later use
    buttons = [answer_a_button, answer_b_button, answer_c_button, answer_d_button]
    generate_question()

# Export Screen
def export():

    # Reused from practice assessment
    def save_history():

        # Regular Expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        # Get filename from entry
        filename = export_entry.get()

        # Checks if there is an invalid character in user input
        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(No Spaces Allowed)"

            else:
                problem = "(No {}'s Allowed)".format(letter)
            has_error = "yes"
            break

        if filename == "":
            problem = "Can't Be Blank"
            has_error = "yes"
        
        if has_error == "yes":
            # Display error message
            export_error_label.config(text="Invalid filename - {}".format(problem), fg="red")
            # Change entry box background to pink
            export_entry.config(bg="#ffafaf")

        else:
            # If there are no errors, generate text file and then close dialogue
            # Add .txt suffix
            filename = filename + ".txt"

            # Create file to hold data
            f = open(filename, "w+") # Press to pay respects

            # Writes a title in the file
            f.write("GAME HISTORY:\n\n")

            # Writes the correct list
            f.write("Pokemon You Got RIGHT!\n\n")
            # Add new line at the end of each item
            for item in correct_list:
                f.write(item + "\n")

            # Writes the correct list
            f.write("Pokemon You Got WRONG!\n\n")
            # Add new line at the end of each item
            for item in incorrect_list:
                f.write(item + "\n")

            # Give feedback for user
            export_error_label.config(text="History Exported Successfully", fg="green")

    # Removes any pre exising widgets
    for widgets in export_frame.winfo_children():
      widgets.destroy()

    raise_frame(export_frame)
    
    #region Export Frame
    export_label = Label(export_frame, text="Export Your Results!", font=Karmatic_Arcade_subheading, bg="white", width=100)
    export_label.grid(row=0, pady=30)

    export_content_frame = Frame(export_frame, bg="white")
    export_content_frame.grid(row=1, pady=25)

    export_picture = Label(export_content_frame, image=surprised_pikachu)
    export_picture.grid(row=0, column=0, padx=15)

    export_instructions = Label(export_content_frame, text="Enter a filename in the box below and press the Save button to save your calculation history to a text file.", font=Karmatic_Arcade_button, justify=LEFT, bg="white", wrap=500)
    export_instructions.grid(row=0, column=1, padx=15, pady=25)
    
    export_error_label = Label(export_frame, bg="white", font=Karmatic_Arcade_small_text, text="")
    export_error_label.grid(row=2, pady=15)

    export_entry = Entry(export_frame, font=Karmatic_Arcade_big_text, width=30, justify=CENTER, relief=GROOVE, borderwidth=4)
    export_entry.grid(row=3, pady=25)

    export_button_frame = Frame(export_frame, bg="white")
    export_button_frame.grid(row=4, pady=25)

    export_button = Button(export_button_frame, text="Export", font=Karmatic_Arcade_button, command=save_history)
    export_button.grid(row=0, column=0, padx=50)

    back_button = Button(export_button_frame, text="Back", font=Karmatic_Arcade_button, command=lambda: raise_frame(gameover_frame))
    back_button.grid(row=0, column=2, padx=50)

    export_error_label.config(text="")
    
    #endregion

# Help Screen
def help_game():
    # Removes any pre exising widgets
    for widgets in help_frame.winfo_children():
      widgets.destroy()

    raise_frame(help_frame)
    
    #region Help Frame
    frame_set_size = Label(help_frame, width=(root.winfo_screenwidth()), bg="white")
    frame_set_size.grid(row=0)

    sub_heading_label = Label(help_frame, font=Karmatic_Arcade_subheading, text="Help", fg="red" ,background="white", justify=CENTER)
    sub_heading_label.grid(row=1)

    help_1_label = Label(help_frame, text="Paragraph 1", font=Karmatic_Arcade_big_text, background="white",justify=CENTER)
    help_1_label.grid(row=2, pady=80)

    help_2_label = Label(help_frame, text="Paragraph 2", font=Karmatic_Arcade_big_text, background="white",justify=CENTER)
    help_2_label.grid(row=3, pady=80)

    back_button = Button(help_frame, text="Close", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(starting_frame))
    back_button.grid(row=4, pady=25)
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


root = Tk()

#region Variables
# Setup my karmatic arcade font
Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 50, weight = "bold")
Karmatic_Arcade_subheading = tkinter.font.Font(family = "Karmatic Arcade", size = 35, weight = "bold")
Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 16, weight = "normal")
Karmatic_Arcade_small_text = tkinter.font.Font(family = "Karmatic Arcade", size = 10, weight = "normal")
Karmatic_Arcade_big_text = tkinter.font.Font(family = "Karmatic Arcade", size = 20, weight = "normal")

lives = 3
score = 0
question_num = 0

correct_list = []
incorrect_list = []

# Set up images
pokeball_icon = PhotoImage(file="pokeball_icon(resized).gif")
normal_icon = PhotoImage(file="pokeball.gif")
master_icon = PhotoImage(file="masterball.gif")
sad_pikachu = PhotoImage(file="sad_pikachu.gif")
surprised_pikachu = PhotoImage(file="surprised_pikachu.gif")
happy_pikachu = PhotoImage(file="happy_pikachu.gif")
#endregion


# Setup Frames
heading_frame = Frame(bg="white")
heading_frame.grid(row=0, sticky="news")
heading_frame.place(anchor="c", relx=.5, rely=0.1)

starting_frame = Frame(bg="white")
starting_frame.grid(row=1, column=0, sticky="news")
starting_frame.place(anchor="c", relx=.5, rely=0.6)

difficulty_frame = Frame(bg="white")
difficulty_frame.grid(row=1, column=0, sticky="news")
difficulty_frame.place(anchor="c", relx=.5, rely=0.6)

help_frame = Frame(bg="white")
help_frame.grid(row=1, column=0, sticky="news")
help_frame.place(anchor="c", relx=.5, rely=0.6)

quiz_frame = Frame(bg="white")
quiz_frame.grid(row=1, column=0, sticky="news")
quiz_frame.place(anchor="c", relx=.5, rely=0.6)

gameover_frame = Frame(bg="white")
gameover_frame.grid(row=1, column=0, sticky="news")
gameover_frame.place(anchor="c", relx=.5, rely=0.6)

export_frame = Frame(bg="white")
export_frame.grid(row=1, column=0, sticky="news")
export_frame.place(anchor="c", relx=.5, rely=0.6)

# Raises the inital frame
raise_frame(heading_frame)
raise_frame(starting_frame)

#region Heading Frame
heading_label = Label(heading_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", background="white", justify=CENTER)
heading_label.grid(row=0)
#endregion

#region Starting Frame
pokemon_logo = Label(starting_frame, image=pokeball_icon, background="white", width=2000)
pokemon_logo.grid(row=0, pady=20)

starting_button_frame = Frame(starting_frame, background="white")
starting_button_frame.grid(row=1, pady=20)

help_button = Button(starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10, height=2, command=help_game)
help_button.grid(row=0, column=0, padx=10)

play_button = Button(starting_button_frame, text="Play", font=Karmatic_Arcade_button, width=10, height=2, command=lambda:raise_frame(difficulty_frame))
play_button.grid(row=0, column=1, padx=10)

quit_button = Button(starting_button_frame, text="Quit", font=Karmatic_Arcade_button, width=10, height=2, command=quit_game)
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
