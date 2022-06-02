from tkinter import *
import tkinter.font


class Start:
    def __init__(self, parent):

        # Setup my karmatic arcade font
        Karmatic_Arcade = tkinter.font.Font(family = "Karmatic Arcade", size = 30, weight = "bold")
        photo = PhotoImage(file="pokeball_icon.gif")
        
        self.starting_frame = Frame(padx=600, pady=20)
        self.starting_frame.grid()

        self.heading_label = Label(self.starting_frame, font=Karmatic_Arcade, text="Who's That Pokemon?", justify=CENTER, bg="red", width=10)
        self.heading_label.grid(row=0)
        # self.heading_label.grid_propagate(0)
        
        self.logo_label = Label(self.starting_frame, padx=10, pady=10, image=photo)
        self.logo_label.photo = photo
        self.logo_label.grid(row=1)
        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()
