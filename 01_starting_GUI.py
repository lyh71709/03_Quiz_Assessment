from tkinter import *
import tkinter.font
from PIL import ImageTk,Image


class Start:
    def __init__(self, parent):

        # Setup my karmatic arcade font
        Karmatic_Arcade = tkinter.font.Font(family = "Karmatic Arcade", size = 30, weight = "bold")
        
        self.starting_frame = Frame(padx=600, pady=20)
        self.starting_frame.grid()

        self.heading_label = Label(self.starting_frame, font=Karmatic_Arcade, text="Who's That Pokemon?", justify=CENTER)
        self.heading_label.grid(row=0)
        
        self.pokemon_logo_canvas = Canvas(self.starting_frame, width = 400, height=380, background="white")
        self.pokemon_logo_canvas.grid(row=1, pady=50)
        self.img = ImageTk.PhotoImage(Image.open("pokeball_icon.png"))     
        self.pokemon_logo_canvas.create_image(0,0,anchor=NW, image=self.img)  



        


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()
