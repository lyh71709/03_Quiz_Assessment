from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import ImageTk,Image,ImageFilter

root = Tk()

def raise_frame(frame):
    frame.tkraise()

def quit_game():
        root.destroy()

# Setup my karmatic arcade font
Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 40, weight = "bold")
Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 18, weight = "normal")
Karmatic_Arcade_text = tkinter.font.Font(family = "Karmatic Arcade", size = 12, weight = "normal")

logo = ImageTk.PhotoImage(Image.open("pokeball_icon.png"))

# Setup Frames
starting_frame = Frame(padx=600, pady=80, bg="white")
starting_frame.grid(row=0, column=0)

difficulty_frame = Frame(padx=600, pady=80, bg="white")
difficulty_frame.grid(row=0, column=0)

help_frame = Frame(padx=600, pady=80, bg="red", width=2020)
help_frame.grid(row=0, column=0)

raise_frame(starting_frame)

# region Starting Frame
heading_label = Label(starting_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", background="white", justify=CENTER)
heading_label.grid(row=0)

pokemon_logo = Label(starting_frame, width = 500, height=500, image=logo, background="white")
pokemon_logo.logo = logo
pokemon_logo.grid(row=1, pady=50)

starting_button_frame = Frame(starting_frame, pady=50, background="white")
starting_button_frame.grid(row=2)

help_button = Button(starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(help_frame))
help_button.grid(row=0, column=0, padx=10)

play_button = Button(starting_button_frame, text="Play", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(difficulty_frame))
play_button.grid(row=0, column=1, padx=10)

quit_button = Button(starting_button_frame, text="Quit", font=Karmatic_Arcade_button, width=10, command=quit_game)
quit_button.grid(row=0, column=2, padx=10)
# regionend

# Difficulty Frame
heading_label = Label(difficulty_frame, font=Karmatic_Arcade_heading, text="Select a Difficulty", background="white", justify=CENTER)
heading_label.grid(row=0)

pokemon_logo = Label(difficulty_frame, width = 500, height=500, image=logo, background="white")
pokemon_logo.logo = logo
pokemon_logo.grid(row=1, pady=50)

difficulty_button_frame = Frame(difficulty_frame, pady=50, background="white")
difficulty_button_frame.grid(row=2)

help_button = Button(difficulty_button_frame, text="Easy", font=Karmatic_Arcade_button, width=10)
help_button.grid(row=0, column=0, padx=10)

play_button = Button(difficulty_button_frame, text="Normal", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(difficulty_frame))
play_button.grid(row=0, column=1, padx=10)

quit_button = Button(difficulty_button_frame, text="Hard", font=Karmatic_Arcade_button, width=10, command=quit_game)
quit_button.grid(row=0, column=2, padx=10)

# Help Frame
heading_label = Label(help_frame, font=Karmatic_Arcade_heading, text="Help", background="white", justify=CENTER)
heading_label.grid(row=0)

help_1_label = Label(help_frame, text="Paragraph 1", font=Karmatic_Arcade_text, background="white",justify=CENTER)
help_1_label.grid(row=1, pady=20)

help_1_label = Label(help_frame, text="Paragraph 2", font=Karmatic_Arcade_text, background="white",justify=CENTER)
help_1_label.grid(row=2, pady=10)

back_button = Button(help_frame, text="Go Back", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(starting_frame))
back_button.grid(row=3, pady=20)


# main routine

root.title("Who's That Pokemon?")
root.geometry("1920x1080")
root.config(background="white")
root.mainloop()
