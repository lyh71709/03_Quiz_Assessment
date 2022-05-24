import sys
import os
from tkinter import Tk, Label, Button

# def restart_program():
#     """Restarts the current program.
#     Note: this function does not return. Any cleanup action (like
#     saving data) must be done before calling this function."""
#     python = sys.executable
#     os.execl(python, python, * sys.argv)

root = Tk()

# # kills the whole application and starts a fresh one
# def restart():
#     root.destroy()
#     root = Tk()
#     root.mainloop()

# Restarts the Whole Window    
def restart():
    root.destroy()
    os.startfile("00_sandbox_v2.pyw")

Label(root, text="Hello World!").pack()
Button(root, text="Restart", command=restart).pack()

root.mainloop()