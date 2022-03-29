from tkinter import *
import tkinter.font
from PIL import ImageTk,Image,ImageFilter


class Start:
    def __init__(self, parent):

        # Setup my karmatic arcade font
        Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 30, weight = "bold")
        Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 18, weight = "normal")

        logo = ImageTk.PhotoImage(Image.open("pokeball_icon.png"))
        
        self.starting_frame = Frame(padx=600, pady=20, background="white")
        self.starting_frame.grid()

        self.heading_label = Label(self.starting_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", justify=CENTER)
        self.heading_label.grid(row=0)
        
        self.pokemon_logo = Label(self.starting_frame, width = 500, height=500, image=logo)
        self.pokemon_logo.logo = logo
        self.pokemon_logo.grid(row=1, pady=50)

        


        self.starting_button_frame = Frame(self.starting_frame, pady=50)
        self.starting_button_frame.grid(row=2)

        self.help_button = Button(self.starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10)
        self.help_button.grid(row=0, column=0, padx=10)

        self.play_button = Button(self.starting_button_frame, text="Play", font=Karmatic_Arcade_button, width=10)
        self.play_button.grid(row=0, column=1, padx=10)

        self.quit_button = Button(self.starting_button_frame, text="Quit", font=Karmatic_Arcade_button, width=10)
        self.quit_button.grid(row=0, column=2, padx=10)
        


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()
