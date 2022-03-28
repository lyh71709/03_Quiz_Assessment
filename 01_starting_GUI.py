from tkinter import *


class Start:
    def __init__(self, parent):
        
        self.starting_frame = Frame(padx=10, pady=10)
        self.starting_frame.grid()

        


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()
