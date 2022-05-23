import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.geometry('200x100')
root.resizable(False, False)
root.title('Listbox')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create a list box

# Use CSV to make a list
with open('pokemon.csv') as file:
    content = file.readlines()

pokemon_list = []
for i in content:
    pokemon_list.append(i.strip())

langs_var = tk.StringVar(value=pokemon_list)

listbox = tk.Listbox(
    root,
    listvariable=langs_var)

listbox.grid(
    column=0,
    row=0,
    sticky='nwes'
)

# handle event
def items_selected(event):
    """ handle item selected event
    """
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = 'You selected: {}'.format(selected_langs)

    showinfo(
        title='Information',
        message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()