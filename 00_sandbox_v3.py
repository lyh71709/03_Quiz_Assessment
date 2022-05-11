from tkinter import *

root = Tk()

width, height = root.winfo_screenwidth(), root.winfo_screenheight()

root.geometry('%dx%d+0+0' % (width,height))

root.mainloop()