from tkinter import *
import tkinter.font
from turtle import screensize
from PIL import Image, ImageTk,  ImageFilter

root = Tk()

def raise_frame(frame):
    frame.tkraise()

def quit_game():
        root.destroy()

# Setup my karmatic arcade font
Karmatic_Arcade_heading = tkinter.font.Font(family = "Karmatic Arcade", size = 60, weight = "bold")
Karmatic_Arcade_subheading = tkinter.font.Font(family = "Karmatic Arcade", size = 40, weight = "bold")
Karmatic_Arcade_button = tkinter.font.Font(family = "Karmatic Arcade", size = 18, weight = "normal")
Karmatic_Arcade_text = tkinter.font.Font(family = "Karmatic Arcade", size = 12, weight = "normal")

pokeball_icon = PhotoImage(file="pokeball_icon.gif")
normal_icon = PhotoImage(file="pokeball.gif")
master_icon = PhotoImage(file="masterball.gif")
question_picture = Image.open("images/charizard.gif")
# Resize the image using resize() method
resized_image = question_picture.resize((400, 400))
question_picture = ImageTk.PhotoImage(resized_image)

# Setup Frames
heading_frame = Frame(bg="white")
heading_frame.grid(row=0, pady=10, sticky="news")
heading_frame.place(anchor="c", relx=.5, rely=0.1)

quiz_frame = Frame(pady=30, bg="red")
quiz_frame.grid(row=1, column=0, sticky="news")
quiz_frame.place(anchor="c", relx=.5, rely=0.6)

raise_frame(heading_frame)
raise_frame(quiz_frame)

#region Heading Frame
heading_label = Label(heading_frame, font=Karmatic_Arcade_heading, text="Who's That Pokemon?", background="white", justify=CENTER)
heading_label.grid(row=0)
#endregion

#region Quiz Frame
stats_label = Label(quiz_frame, text="Score - 15 \n Lives - 3\n Question No. - 10", font=Karmatic_Arcade_text, bg="white")
stats_label.grid(row=0, pady=10)

question = Label(quiz_frame, width=400, height=400, image=question_picture, background="white")
question.grid(row=1, pady=50)


#endregion

# main routine
root.title("Who's That Pokemon?")
root.geometry("1920x1080")
root.config(background="white")
root.state('zoomed')
root.mainloop()
