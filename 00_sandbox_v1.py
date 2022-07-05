from tkinter import *

def sel(e):
   selection = "Value = " + str(var.get())
   label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var, from_=0)
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel)
root.bind('<Return>', sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()