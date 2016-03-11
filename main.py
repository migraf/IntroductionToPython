__author__ = "Julian Petruck"

from Tkinter import *
from gui import *
from input_reader import *


language_dict = split_file("listss16.txt")
languages = dict_keys_as_list(language_dict)

frame = Tk()
gui = GUI(frame)
frame.title("Distance Methods on ASJP-Corpus")

gui.set_languages(languages)

frame.mainloop()

