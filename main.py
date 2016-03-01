__author__ = "Julian Petruck"

from Tkinter import *
from gui import *


frame = Tk()
gui = Gui(frame)

gui.set_answer("hallo\n"
               "hallo\n"
               ".\n"
               ".\n"
               ".\n"
               ".\n"
               "tschuess.")

new_languages = ("1", "2", "3", "4", "5")

gui.set_languages(new_languages)

frame.title("Distance Methods on ASJP-Corpus")

frame.mainloop()

