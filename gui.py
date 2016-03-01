__author__ = "Julian Petruck"

import Tkinter as tk
from random import randint
import tkFileDialog


class Gui:
    __languages = (
        "german",
        "english",
        "swedish",
        "french")

    __calculated_answer = ("Here we will show\n"
                           "the answer\n"
                           "Our methods will\n"
                           "calculate.")

    __master = 0
    __input_frame = 0
    __textbox = 0
    __dropdown_frame = 0
    __dropdown_left = 0
    __dropdown_right = 0
    __left_language = 0
    __right_language = 0
    __dropdown_output = 0
    __selected_output = 0
    __listbox_left = 0
    __listbox_right = 0
    __listbox_frame_left = 0
    __listbox_frame_right = 0
    __textbox_frame = 0
    __text_left = 0
    __text_right = 0

    def __init__(self, master):


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

        __master = master

        self.__input_frame = tk.Frame(master)
        self.__input_frame.grid()

        self.label = tk.Label(self.__input_frame, text="Select two languages to compare")
        self.label.grid(row=0, column=0)

        self.__dropdown_frame = tk.Frame(self.__input_frame)
        self.__dropdown_frame.grid(row=1, column=0)

        self.__listbox_frame_left = tk.Frame(self.__dropdown_frame)
        self.__listbox_frame_left.grid(row=0, column=0)
        self.__listbox_frame_right = tk.Frame(self.__dropdown_frame)
        self.__listbox_frame_right.grid(row=0, column=1)

        scrollbar_left = tk.Scrollbar(self.__listbox_frame_left, orient=tk.VERTICAL)
        scrollbar_below_left = tk.Scrollbar(self.__listbox_frame_left, orient=tk.HORIZONTAL)
        scrollbar_right = tk.Scrollbar(self.__listbox_frame_right, orient=tk.VERTICAL)
        scrollbar_below_right = tk.Scrollbar(self.__listbox_frame_right, orient=tk.HORIZONTAL)

        self.__listbox_left = tk.Listbox(self.__listbox_frame_left,
                                         yscrollcommand=scrollbar_left.set,
                                         xscrollcommand=scrollbar_below_left.set,
                                         selectmode='browse')
        self.__listbox_right = tk.Listbox(self.__listbox_frame_right,
                                          yscrollcommand=scrollbar_right.set,
                                          xscrollcommand=scrollbar_below_right.set,
                                          selectmode='browse')

        scrollbar_left.config(command=self.__listbox_left.yview)
        scrollbar_below_left.config(command=self.__listbox_left.xview)
        scrollbar_right.config(command=self.__listbox_right.yview)
        scrollbar_below_right.config(command=self.__listbox_right.xview)

        scrollbar_left.grid(row=0, column=0, sticky=tk.N+tk.S)
        scrollbar_below_left.grid(row=1, column=1, sticky=tk.E+tk.W)
        scrollbar_right.grid(row=0, column=1, sticky=tk.N+tk.S)
        scrollbar_below_right.grid(row=1, column=0, sticky=tk.E+tk.W)
        self.__listbox_left.grid(row = 0, column = 1)
        self.__listbox_right.grid(row = 0, column = 0)

        selected_frame = tk.Frame(self.__input_frame)
        selected_frame.grid(row=2, column=0)

        self.__text_left = tk.Label(selected_frame)
        self.__text_right = tk.Label(selected_frame)
        caption_left = tk.Label(selected_frame, text="first language: ")
        caption_right = tk.Label(selected_frame, text="second language: ")
        caption_left.grid(row=0, column=0)
        caption_right.grid(row=1, column=0)
        self.__text_left.grid(row=0, column=1)
        self.__text_right.grid(row=1, column=1)

        self.__listbox_left.bind('<<ListboxSelect>>', selected_left)
        self.__listbox_right.bind('<<ListboxSelect>>', selected_right)

        self.__languages = sorted(self.__languages)

        for choice in self.__languages:
            self.__listbox_left.insert(tk.END, choice)
            self.__listbox_right.insert(tk.END, choice)

        button_frame = tk.Frame(self.__input_frame)
        button_frame.grid(row=3, column=0)

        calculate_button = tk.Button(button_frame, text="calculate", command=self.__calculate)
        calculate_button.grid(row=0, column=0)

        random_button = tk.Button(button_frame, text="calculate random", command=self.__random_calculation)
        random_button.grid(row=0, column=1)

        output_variations = ("output below",
                             "output in txt-file",
                             "output below and in txt-file")

        self.__selected_output = tk.StringVar(master)
        self.__selected_output.set(output_variations[0])

        self.__dropdown_output = tk.OptionMenu(self.__input_frame, self.__selected_output, *output_variations)
        self.__dropdown_output.grid(row=4, column=0)

        self.__textbox_frame = tk.Frame(self.__input_frame)
        self.__textbox_frame.grid(row=5, column=0)

        scrollbar_text = tk.Scrollbar(self.__textbox_frame, orient=tk.VERTICAL)
        self.__textbox = tk.Text(self.__textbox_frame, height=6, width=50, yscrollcommand=scrollbar_text.set)

        scrollbar_text.config(command=self.__textbox.yview)

        scrollbar_text.grid(row=0, column=1, sticky=tk.N+tk.S)
        self.__textbox.grid(row=0, column=0)
        self.__textbox.insert(tk.END, self.__calculated_answer)


    def set_languages(self, new_languages):

        self.__languages = sorted(new_languages)

        self.__listbox_left.delete(0, tk.END)
        self.__listbox_right.delete(0, tk.END)

        for choice in self.__languages:
            self.__listbox_left.insert(tk.END, choice)
            self.__listbox_right.insert(tk.END, choice)


    def set_answer(self, new_answer):

        self.__calculated_answer = new_answer
        self.__textbox.delete("1.0", tk.END)
        self.__textbox.insert(tk.END, self.__calculated_answer)


    def __calculate(self):

        language_one = self.__text_left.cget("text")
        language_two = self.__text_right.cget("text")

        if language_one == "":

            self.set_answer("You need to select two languages to calculate a result!")

        elif language_two == "":

            self.set_answer("You need to select two languages to calculate a result!")

        elif language_one == language_two:

            self.set_answer("You should select two different languages!")

        else:

            output_type = self.__selected_output.get()

            # hier sollte die methode ausgefuehrt werden, die die berechnung durchfuehrt und die Antwort zurueckgibt

            if output_type == "output below":

                self.set_answer("goodbye\ngoodbye\ngoodbye\n...")

            elif output_type == "output in txt-file":

                self.set_answer("The result was saved to a file...")

                datei = tkFileDialog.asksaveasfile()
                if datei:
                    datei.write("goodbye\ngoodbye\ngoodbye\n...")
                    datei.close()

            elif output_type == "output below and in txt-file":

                self.set_answer("goodbye\ngoodbye\ngoodbye\n...")

                datei = tkFileDialog.asksaveasfile()
                if datei:
                    datei.write(self.__textbox.get('1.0', 'end'))
                    datei.close()


    def __random_calculation(self):

        boundary = len(self.__languages) - 1

        random_one = randint(0, boundary)
        random_two = random_one

        while random_one == random_two:

            random_two = randint(0, boundary)

        language_one = self.__languages[random_one]
        language_two = self.__languages[random_two]

        self.__text_left.config(text=language_one)
        self.__text_right.config(text=language_two)

        output_type = self.__selected_output.get()

        # hier sollte die methode ausgefuehrt werden, die die berechnung durchfuehrt und die Antwort zurueckgibt

        if output_type == "output below":

            self.set_answer("goodbye\ngoodbye\ngoodbye\n...")

        elif output_type == "output in txt-file":

            self.set_answer("The result was saved to a file...")

            datei = tkFileDialog.asksaveasfile()
            if datei:
                datei.write("goodbye\ngoodbye\ngoodbye\n...")
                datei.close()

        elif output_type == "output below and in txt-file":

            self.set_answer("goodbye\ngoodbye\ngoodbye\n...")

            datei = tkFileDialog.asksaveasfile()
            if datei:
                datei.write(self.__textbox.get('1.0', 'end'))
                datei.close()

