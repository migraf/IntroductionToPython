__author__ = "Julian Petruck"

import Tkinter as tk
import tkFileDialog


class Gui:

    __languages = (
      "german",
      "english",
      "swedish",
      "french")

    __calculated_answer =("Here we will show\n"
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


    def __init__(self, master):

        __master = master

        __input_frame = tk.Frame(master)
        __input_frame.grid()

        self.label = tk.Label(__input_frame, text="Select two languages to compare")
        self.label.grid(row=0, column=0)

        self.__left_language = tk.StringVar(master)
        self.__left_language.set("")
        self.__right_language = tk.StringVar(master)
        self.__right_language.set("")

        self.__dropdown_frame = tk.Frame(__input_frame)
        self.__dropdown_frame.grid(row=1, column=0)

        self.__dropdown_left = tk.OptionMenu(self.__dropdown_frame, self.__left_language, *self.__languages)
        self.__dropdown_left.grid(row=0, column=0)

        self.__dropdown_right = tk.OptionMenu(self.__dropdown_frame, self.__right_language, *self.__languages)
        self.__dropdown_right.grid(row=0, column=1)

        self.calculate_button = tk.Button(self.__dropdown_frame, text="calculate", command=self.__calculate)
        self.calculate_button.grid(row=0, column=2)

        output_variations = ("output below",
                             "output in txt-file",
                             "output below and in txt-file")

        self.__selected_output = tk.StringVar(master)
        self.__selected_output.set(output_variations[0])

        self.__dropdown_output = tk.OptionMenu(__input_frame, self.__selected_output, *output_variations)
        self.__dropdown_output.grid(row=2, column=0)

        self.__textbox = tk.Text(__input_frame, height=6, width=50)
        self.__textbox.grid(row=3, column=0)
        self.__textbox.insert(tk.END, self.__calculated_answer)


    def set_languages(self, new_languages):

        self.__languages = new_languages

        self.__dropdown_left['menu'].delete(0, 'end')
        self.__dropdown_right['menu'].delete(0, 'end')

        for choice in self.__languages:
            self.__dropdown_left['menu'].add_command(label=choice, command=tk._setit(self.__left_language, choice))
            self.__dropdown_right['menu'].add_command(label=choice, command=tk._setit(self.__right_language, choice))


    def set_answer(self, new_answer):

        self.__calculated_answer = new_answer
        self.__textbox.delete("1.0", tk.END)
        self.__textbox.insert(tk.END, self.__calculated_answer)


    def __calculate(self):

        language_one = self.__left_language.get()
        language_two = self.__right_language.get()

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
