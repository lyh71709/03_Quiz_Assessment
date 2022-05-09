from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import ImageFilter

root = Tk()

# Moves frame to the top
def raise_frame(frame):
    frame.tkraise()

# Exits game
def quit_game():
        root.destroy()

# Setup my karmatic arcade font
Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 60, weight = "bold")
Karmatic_Arcade_subheading = tkinter.font.Font(family = "Karmatic Arcade", size = 40, weight = "bold")
Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 18, weight = "normal")
Karmatic_Arcade_text = tkinter.font.Font(family = "Karmatic Arcade", size = 12, weight = "normal")

# Setting up images
pokeball_icon = PhotoImage(file="pokeball_icon.gif")
normal_icon = PhotoImage(file="pokeball.gif")
master_icon = PhotoImage(file="masterball.gif")

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

help_frame = Frame(pady=30, bg="white")
help_frame.grid(row=1, column=0, sticky="news")
help_frame.place(anchor="c", relx=.5, rely=0.6)

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

help_button = Button(starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(help_frame))
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

normal_button = Button(difficulty_button_frame, image=normal_icon, font=Karmatic_Arcade_button)
normal_button.grid(row=1, column=0, padx=25, pady=5)

master_button = Button(difficulty_button_frame, image=master_icon, font=Karmatic_Arcade_button, command=quit_game)
master_button.grid(row=1, column=1, padx=25, pady=5)
#endregion

#region Help Frame
frame_set_size = Label(help_frame, width=(root.winfo_screenwidth()), bg="white")
frame_set_size.grid(row=0)

sub_heading_label = Label(help_frame, font=Karmatic_Arcade_subheading, text="Help", fg="red" ,background="white", justify=CENTER)
sub_heading_label.grid(row=1)

help_1_label = Label(help_frame, text="Paragraph 1", font=Karmatic_Arcade_text, background="white",justify=CENTER)
help_1_label.grid(row=2, pady=100)

help_1_label = Label(help_frame, text="Paragraph 2", font=Karmatic_Arcade_text, background="white",justify=CENTER)
help_1_label.grid(row=3, pady=60)

back_button = Button(help_frame, text="Close", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(starting_frame))
back_button.grid(row=4, pady=50)
#endregion


# main routine
root.title("Who's That Pokemon?")
root.geometry("1920x1080")
root.config(background="white")
# Makes game fullscreen
root.state('zoomed')
root.mainloop()
