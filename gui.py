__author__ = "Julian Petruck"

#This file specifies the GUI class for our project
# "Distance Methods on ASJP-Corpus".

# all necessary inputs
import Tkinter as tk
from random import randint
import tkFileDialog
#from calculate_output import *

class GUI:

    # Creates the member variable for the list containing the languages.
    # The default content of this list should never be shown in the GUI,
    # but if so, there must be some error with the analysis of the
    # .txt file containing the languages.
    __languages = ("not",
                   "scanned",
                   "yet")

    # Creates the member variable for the output shown in the GUI.
    # The default content should be shown in the GUI until any other
    # output was calculated.
    __calculated_answer = ("Here we will show the result our program will calculate.")

    # Creates all the private member variables we need to use not only
    # in the __init__ method but also in other methods the GUI class uses.
    __textbox = 0
    __selected_output = 0
    __listbox_left = 0
    __listbox_right = 0
    __text_left = 0
    __text_right = 0

    # The initialization method for the GUI.
    def __init__(self, master):

        # Creates and places the main frame which takes place in the master frame
        self.__input_frame = tk.Frame(master)
        self.__input_frame.grid()

        # Creates and places a label at the top of the main frame (__input_frame)
        self.label = tk.Label(self.__input_frame,
                              text="\nSelect two languages to compare them with levensthein and n-gram:\n")
        self.label.grid(row=0, column=0)

        # Creates and places a frame for the listboxes containing the existing languages
        self.__listbox_frame = tk.Frame(self.__input_frame)
        self.__listbox_frame.grid(row=1, column=0)

        # Creates and places two frames, one for each listbox and its associated scrollbars
        self.__listbox_frame_left = tk.Frame(self.__listbox_frame)
        self.__listbox_frame_left.grid(row=0, column=0)
        self.__listbox_frame_right = tk.Frame(self.__listbox_frame)
        self.__listbox_frame_right.grid(row=0, column=1)

        # Creates 4 scrollbars, 2 for each listbox (below and on one side)
        self.scrollbar_left = tk.Scrollbar(self.__listbox_frame_left, orient=tk.VERTICAL)
        self.scrollbar_below_left = tk.Scrollbar(self.__listbox_frame_left, orient=tk.HORIZONTAL)
        self.scrollbar_right = tk.Scrollbar(self.__listbox_frame_right, orient=tk.VERTICAL)
        self.scrollbar_below_right = tk.Scrollbar(self.__listbox_frame_right, orient=tk.HORIZONTAL)

        # Creates 2 listboxes in the associated frames and with the associated scrollbars attached
        self.__listbox_left = tk.Listbox(self.__listbox_frame_left,
                                         yscrollcommand=self.scrollbar_left.set,
                                         xscrollcommand=self.scrollbar_below_left.set,
                                         selectmode='browse', width=25)
        self.__listbox_right = tk.Listbox(self.__listbox_frame_right,
                                          yscrollcommand=self.scrollbar_right.set,
                                          xscrollcommand=self.scrollbar_below_right.set,
                                          selectmode='browse', width=25)

        # Configures the scrollbars to set the associated part of the listboxes
        self.scrollbar_left.config(command=self.__listbox_left.yview)
        self.scrollbar_below_left.config(command=self.__listbox_left.xview)
        self.scrollbar_right.config(command=self.__listbox_right.yview)
        self.scrollbar_below_right.config(command=self.__listbox_right.xview)

        # Places the 4 scrollbars
        self.scrollbar_left.grid(row=0, column=0, sticky=tk.N+tk.S)
        self.scrollbar_below_left.grid(row=1, column=1, sticky=tk.E+tk.W)
        self.scrollbar_right.grid(row=0, column=1, sticky=tk.N+tk.S)
        self.scrollbar_below_right.grid(row=1, column=0, sticky=tk.E+tk.W)

        # Places the 2 listboxes
        self.__listbox_left.grid(row = 0, column = 1)
        self.__listbox_right.grid(row = 0, column = 0)

        # Creates and places a frame for showing the selected languages
        self.selected_frame = tk.Frame(self.__input_frame)
        self.selected_frame.grid(row=2, column=0)

        # Creates and places to labels as "captions" for the selected languages
        self.caption_left = tk.Label(self.selected_frame, text="first language: ")
        self.caption_right = tk.Label(self.selected_frame, text="second language: ")
        self.caption_left.grid(row=0, column=0)
        self.caption_right.grid(row=1, column=0)

        # Creates and places two labels for showing the selected languages
        self.__text_left = tk.Label(self.selected_frame)
        self.__text_right = tk.Label(self.selected_frame)
        self.__text_left.grid(row=0, column=1)
        self.__text_right.grid(row=1, column=1)

        # The two methods are defined for updating the labels specified above if
        # one selectes a languages in one of the 2 listboxes
        def selected_left(event):

            selected = self.__listbox_left.curselection()
            item = selected[0]
            language = self.__listbox_left.get(item)
            self.__text_left.config(text=language)

        def selected_right(event):

            selected = self.__listbox_right.curselection()
            item = selected[0]
            language = self.__listbox_right.get(item)
            self.__text_right.config(text=language)

        # Set the listbox to call the methods specified above if a language
        # is selected
        self.__listbox_left.bind('<<ListboxSelect>>', selected_left)
        self.__listbox_right.bind('<<ListboxSelect>>', selected_right)

        # The languages shown in the listbox should be sorted for easier
        # navigation
        self.__languages = sorted(self.__languages)

        # Inserts all the languages into the listboxes
        for choice in self.__languages:
            self.__listbox_left.insert(tk.END, choice)
            self.__listbox_right.insert(tk.END, choice)

        # Creates and places a frame for the "random languages" button and the
        # "output options" menu
        self.options_frame = tk.Frame(self.__input_frame)
        self.options_frame.grid(row=3, column=0)

        # Creates the list containing the ouput options
        output_variations = ("output below",
                             "output in txt-file",
                             "output below and in txt-file")

        # Creates a variable for getting the selected output option and
        # sets its default value to "output below"
        self.__selected_output = tk.StringVar(master)
        self.__selected_output.set(output_variations[0])

        # Creates and places the button for selecting two random languages.
        # The button calls the method "__random_languages".
        self.random_button = tk.Button(self.options_frame, text="set random languages", command=self.__random_languages)
        self.random_button.grid(row=0, column=0)

        # Creates and places the option menu for selecting an ouput type
        self.__output_type = tk.OptionMenu(self.options_frame, self.__selected_output, *output_variations)
        self.__output_type.grid(row=0, column=1)

        # Creates and places a frame for the 2 calculation buttons
        self.button_frame = tk.Frame(self.__input_frame)
        self.button_frame.grid(row=4, column=0)

        # Creates and places a button for comparing the 2 selected languages.
        # The button calls the method "__calculate".
        self.calculate_button = tk.Button(self.button_frame, text="calculate", command=self.__calculate)
        self.calculate_button.grid(row=0, column=0)

        # Creates and places a button for comparing the first language to all other languages.
        # The button calls the method "__compare_all".
        self.compare_all_button = tk.Button(self.button_frame,
                                       text="compare first language to all languages",
                                       command=self.__compare_all)
        self.compare_all_button.grid(row=0, column=1)

        # Creates and places a frame for the textbox containing the output and its
        # associated scrollbars.
        self.__textbox_frame = tk.Frame(self.__input_frame)
        self.__textbox_frame.grid(row=6, column=0)

        # Creates a scrollbar and a textbox for the output
        self.scrollbar_text = tk.Scrollbar(self.__textbox_frame, orient=tk.VERTICAL)
        self.__textbox = tk.Text(self.__textbox_frame, height=15, width=60, yscrollcommand=self.scrollbar_text.set)

        # configures the scrollbar to the textbox
        self.scrollbar_text.config(command=self.__textbox.yview)

        # Places scrollbar and textbox and inserts the default answer into the textbox.
        self.scrollbar_text.grid(row=0, column=1, sticky=tk.N+tk.S)
        self.__textbox.grid(row=0, column=0)
        self.__textbox.insert(tk.END, self.__calculated_answer)

    # Method for updating the list containing the languages and the listboxes.
    def set_languages(self, new_languages):

        # Updates the language list
        self.__languages = sorted(new_languages)

        # Deletes the old  content of the listboxes.
        self.__listbox_left.delete(0, tk.END)
        self.__listbox_right.delete(0, tk.END)

        # Writes the new languages into the listboxes
        for choice in self.__languages:
            self.__listbox_left.insert(tk.END, choice)
            self.__listbox_right.insert(tk.END, choice)


    # Method for setting the answer shown in the textbox
    def set_answer(self, new_answer):

        # Updates the member variable, deleltes the old content of the textbox
        # and inserts the new content.
        self.__calculated_answer = new_answer
        self.__textbox.delete("1.0", tk.END)
        self.__textbox.insert(tk.END, self.__calculated_answer)


    # Method for selecting two random languages
    def __random_languages(self):

        # Sets the boundary to the size of the language list
        boundary = len(self.__languages) - 1

        # Calculates a random number between 0 and the boundary
        random_one = randint(0, boundary)
        random_two = random_one

        # Calculates the second number until its not the same as
        # the first number
        while random_one == random_two:

            random_two = randint(0, boundary)

        # Gets the two calculated languages
        language_one = self.__languages[random_one]
        language_two = self.__languages[random_two]

        # Sets the labels to the languages
        self.__text_left.config(text=language_one)
        self.__text_right.config(text=language_two)


    # Compares two languages.
    def __calculate(self):

        # Gets the selected languages.
        language_one = self.__text_left.cget("text")
        language_two = self.__text_right.cget("text")

        # Catches empty languages or same languages
        if language_one == "":

            self.set_answer("You need to select two languages to calculate a result!")

        elif language_two == "":

            self.set_answer("You need to select two languages to calculate a result!")

        elif language_one == language_two:

            self.set_answer("You should select two different languages!")

        else:
            output = "..."

            self.__write_output(output)


    # Compares one language to all other languages.
    def __compare_all(self):
        #language_dict = split_file("listss16.txt")
        # Gets the language.
        language = self.__text_left.cget("text")

        # Catches empty languages
        if language == "":

             self.set_answer("You need to select a language to calculate a result!")

        else:
            output = "..."
                #compare_one_language_output(language_dict, language)

            self.__write_output(output)


    # Looks up the output type and writes them into the GUI or a new file
    def __write_output(self, output):

        # Gets the selected output type.
        output_type = self.__selected_output.get()

        if output_type == "output below":

            # Sets the output to the GUI.
            self.set_answer(output)

        elif output_type == "output in txt-file":

            # Saves the output to a file and catches, if a file was created or not.
            datei = tkFileDialog.asksaveasfile()
            if datei:
                datei.write(output)
                self.set_answer("Your file was saved to " + datei.name + " .")
                datei.close()

            else:
                self.set_answer("For some instance, there was no file created...")

        elif output_type == "output below and in txt-file":

            # Saves the output to a file and catches, if a file was created or not.
            datei = tkFileDialog.asksaveasfile()
            if datei:
                datei.write(self.__textbox.get('1.0', 'end'))
                temp_string = "Your file was saved to " + datei.name + " .\n"
                temp_string += "Those are your results: \n\n"
                datei.close()
            else:
                temp_string = "For some instance, there was no file created...\n"
                temp_string += "Those are your results: \n\n"

            # Sets the output to the GUI.
            output = temp_string + output
            self.set_answer(output)
