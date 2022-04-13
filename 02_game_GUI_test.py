from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import Image, ImageTk,  ImageFilter
import csv
import time
import random
from functools import partial

def raise_frame(frame):
    frame.tkraise()

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    
    return("finished")

class Game:
    def __init__(self, parent):

        # Setup my karmatic arcade font
        Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 60, weight = "bold")
        Karmatic_Arcade_subheading = tkinter.font.Font(family = "Karmatic Arcade", size = 40, weight = "bold")
        Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 18, weight = "normal")
        Karmatic_Arcade_text = tkinter.font.Font(family = "Karmatic Arcade", size = 12, weight = "normal")

        pokeball_icon = PhotoImage(file="pokeball_icon.gif")
        normal_icon = PhotoImage(file="pokeball.gif")
        master_icon = PhotoImage(file="masterball.gif")
        self.question_picture = ""
        # Resize the image using resize() method

        self.pokemon_list = []
        dataset = open("pokemon.csv")
        csvreader = csv.reader(dataset)
        for row in csvreader:
            self.pokemon_list.append(row)
            

        dataset.close()

        # Setup Frames
        self.heading_frame = Frame(bg="white")
        self.heading_frame.grid(row=0, pady=10, sticky="news")
        self.heading_frame.place(anchor="c", relx=.5, rely=0.1)

        self.starting_frame = Frame(pady=80, bg="white")
        self.starting_frame.grid(row=1, column=0, sticky="news")
        self.starting_frame.place(anchor="c", relx=.5, rely=0.6)

        self.quiz_frame = Frame(pady=30, bg="white")
        self.quiz_frame.grid(row=1, column=0, sticky="news")
        self.quiz_frame.place(anchor="c", relx=.5, rely=0.6)

        raise_frame(self.heading_frame)
        raise_frame(self.quiz_frame)

        #region Heading Frame
        self.heading_label = Label(self.heading_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", background="white", justify=CENTER)
        self.heading_label.grid(row=0)
        #endregion

        #region Starting Frame
        self.pokemon_logo = Label(self.starting_frame, width = 500, height=500, image=pokeball_icon, background="white")
        self.pokemon_logo.grid(row=0, pady=50)

        self.starting_button_frame = Frame(self.starting_frame, pady=50, background="white")
        self.starting_button_frame.grid(row=1)

        self.help_button = Button(self.starting_button_frame, text="Help", font=Karmatic_Arcade_button, width=10)
        self.help_button.grid(row=0, column=0, padx=10)

        self.play_button = Button(self.starting_button_frame, text="Play", font=Karmatic_Arcade_button, width=10, command=lambda: self.generate_question)
        self.play_button.grid(row=0, column=1, padx=10)

        self.quit_button = Button(self.starting_button_frame, text="Quit", font=Karmatic_Arcade_button, width=10, command=lambda: self.quit_game)
        self.quit_button.grid(row=0, column=2, padx=10)
        #endregion

        #region Quiz Frame
        self.question_num_label = Label(self.quiz_frame, text="Question X", font=Karmatic_Arcade_subheading, bg="white")
        self.question_num_label.grid(row=0, column=0, pady=10)

        self.stats_label = Label(self.quiz_frame, text="Lives - X\nScore - X", font=Karmatic_Arcade_subheading, bg="white")
        self.stats_label.grid(row=0, column=1, padx=10, pady=10)

        self.question = Label(self.quiz_frame, width=600, height=600, background="white")
        self.question.grid(row=1, column=0, pady=50, padx=30)

        self.answer_button_frame = Frame(self.quiz_frame)
        self.answer_button_frame.grid(row=1, column=1, pady=30, padx=50)

        self.answer_a_button = Button(self.answer_button_frame, text="A", font=Karmatic_Arcade_button, width=20, height=5)
        self.answer_a_button.grid(row=0, column=0, pady=20, padx=20)

        self.answer_b_button = Button(self.answer_button_frame, text="B", font=Karmatic_Arcade_button, width=20, height=5)
        self.answer_b_button.grid(row=0, column=1, pady=20, padx=20)

        self.answer_c_button = Button(self.answer_button_frame, text="C", font=Karmatic_Arcade_button, width=20, height=5)
        self.answer_c_button.grid(row=1, column=0, pady=20, padx=20)

        self.answer_d_button = Button(self.answer_button_frame, text="D", font=Karmatic_Arcade_button, width=20, height=5)
        self.answer_d_button.grid(row=1, column=1, pady=20, padx=20)

        self.answer_a_button.config(command=lambda: self.answer_question(self.answer_a_button, self.answer_a_button))
        self.answer_b_button.config(command=lambda: self.answer_question(self.answer_b_button, self.answer_a_button))
        self.answer_c_button.config(command=lambda: self.answer_question(self.answer_c_button, self.answer_a_button))
        self.answer_d_button.config(command=lambda: self.answer_question(self.answer_d_button, self.answer_a_button))

        #endregion

    def generate_question(self):
            buttons = [self.answer_a_button,self.answer_b_button,self.answer_c_button,self.answer_d_button]
            question = random.choice(self.pokemon_list)
            question_picture = Image.open("images/{}.png".format(question))
            resized_image = question_picture.resize((600, 600))
            question_picture = ImageTk.PhotoImage(resized_image)

            for i in buttons:
                i.config(text="{}".format(random.choice(self.pokemon_list)).title())

            correct_button = random.choice(buttons)
            correct_button.config(text="question".title())

            self.question.config(image=question_picture)


    def answer_question(self, button_pressed, correct_button):

        if button_pressed == correct_button:
            print("correct")
            button_pressed.config(bg="green")
        else:
            print("incorrect")
            button_pressed.config(bg="red")
            correct_button.config(bg="green")

        pre_question = countdown(5)
        if pre_question == "finished":
            print("hi")
    
    def quit_game(self):
        root.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Who's That Pokemon?")
    root.geometry("1920x1080")
    root.config(background="white")
    root.state('zoomed')
    something = Game(root)
    root.mainloop()
