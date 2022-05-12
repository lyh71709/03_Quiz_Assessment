from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import ImageTk,Image,ImageFilter


class Start:
    def __init__(self, parent):

        # Setup my karmatic arcade font
        Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 30, weight = "bold")
        Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 18, weight = "normal")

        # Starting Frame
        logo = ImageTk.PhotoImage(Image.open("pokeball_icon.gif"))

        self.canvas = Canvas(root)
        self.canvas.grid()

        myscrollbar=Scrollbar(root,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=myscrollbar.set)
        myscrollbar.grid(row=0, column=1, sticky="NS")

        self.starting_frame = Frame(self.canvas, padx=600, pady=80, background="white")
        self.starting_frame.grid()

        self.heading_label = Label(self.starting_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", background="white", justify=CENTER)
        self.heading_label.grid(row=0)
        
        self.pokemon_logo = Label(self.starting_frame, width = 500, height=500, image=logo, background="white")
        self.pokemon_logo.logo = logo
        self.pokemon_logo.grid(row=1, pady=50)

        self.starting_button_frame = Frame(self.starting_frame, pady=50, background="white")
        self.starting_button_frame.grid(row=2)

        self.help_button = Button(self.starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10)
        self.help_button.grid(row=0, column=0, padx=10)

        self.play_button = Button(self.starting_button_frame, text="Play", font=Karmatic_Arcade_button, width=10, command=self.to_difficuty_select)
        self.play_button.grid(row=0, column=1, padx=10)

        self.quit_button = Button(self.starting_button_frame, text="Quit", font=Karmatic_Arcade_button, width=10, command=self.quit_game)
        self.quit_button.grid(row=0, column=2, padx=10)

    def quit_game(self):
        # Destroy Window
        root.destroy()
    
        
    def to_difficuty_select(self):
        root.withdraw()
        Difficulty(self)

    def myfunction(self, event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=200,height=200)

class Difficulty:
    def __init__(self, partner):

        self.difficulty_box = Toplevel()
        # If users press cross at top, close program
        self.difficulty_box.protocol('WM_DELETE_WINDOW', partner.quit_game)
        self.difficulty_box.state("zoomed")

        self.difficulty_frame = Frame(self.difficulty_box, padx=600, pady=80, background="white")
        self.difficulty_frame.grid()

        self.heading_label = Label(self.difficulty_frame, font="arial 12 bold", text="Who's That Pokemon?", background="white", justify=CENTER)
        self.heading_label.grid(row=0)




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Who's That Pokemon?")
    root.state("zoomed")
    root.config(background="white")
    game = Start(root)
    root.mainloop()
