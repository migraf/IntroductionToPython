__author__ = "Julian Petruck"

# Necessary input.
from Tkinter import *
from gui import *
from input_reader import *

# Creates the used language list.
language_dict = split_file("listss16.txt")
languages = dict_keys_as_list(language_dict)

# Creates the GUI frame and the GUI class and sets the title.
frame = Tk()
gui = GUI(frame)
frame.title("Distance Methods on ASJP-Corpus")

# Sets the language list of the GUI.
gui.set_languages(languages)

# Starts the mainloop of the GUI.
frame.mainloop()

