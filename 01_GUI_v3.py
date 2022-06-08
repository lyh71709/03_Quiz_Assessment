# V3
# Add in custom font

from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import ImageTk,Image,ImageFilter

def raise_frame(frame):
    frame.tkraise()

class Game:
    def __init__(self, parent):

        # Setup my karmatic arcade font
        Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 30, weight = "bold")
        Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 18, weight = "normal")

        pokeball_icon = ImageTk.PhotoImage(Image.open("pokeball_icon.gif"))

        # Setup Frames
        self.starting_frame = Frame(width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="blue")
        self.starting_frame.grid(row=0, column=0)

        self.difficulty_frame = Frame(width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="red")
        self.difficulty_frame.grid(row=0, column=0)

        raise_frame(self.starting_frame)

        # Starting Frame
        self.heading_label = Label(self.starting_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", background="white", justify=CENTER)
        self.heading_label.grid(row=0)
        
        self.pokemon_logo = Label(self.starting_frame, width = 500, height=500, image=pokeball_icon, background="white")
        self.pokemon_logo.logo = pokeball_icon
        self.pokemon_logo.grid(row=1, pady=50)

        self.starting_button_frame = Frame(self.starting_frame, pady=50, background="white")
        self.starting_button_frame.grid(row=2)

        self.help_button = Button(self.starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10)
        self.help_button.grid(row=0, column=0, padx=10)

        self.play_button = Button(self.starting_button_frame, text="Play", font=Karmatic_Arcade_button, width=10, command=lambda:raise_frame(self.difficulty_frame))
        self.play_button.grid(row=0, column=1, padx=10)

        self.quit_button = Button(self.starting_button_frame, text="Quit", font=Karmatic_Arcade_button, width=10, command=self.quit_game)
        self.quit_button.grid(row=0, column=2, padx=10)

        # Difficulty Frame
        self.heading_label = Label(self.difficulty_frame, font=Karmatic_Arcade_heading, text="Select your difficulty", background="white", justify=CENTER)
        self.heading_label.grid(row=0)

    def quit_game(self):
        # Destroy window
        root.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Who's That Pokemon?")
    root.state("zoomed")
    root.config(background="white")
    game = Game(root)
    root.mainloop()
