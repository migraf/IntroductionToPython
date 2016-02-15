from Tkinter import *

class App:

    def __init__(self, master):
        input_frame = Frame(master)
        input_frame.grid()

        self.button = Button(input_frame, text = "Analyze Textfile", )
        self.button.grid(row = 1, column = 3)

        self.label = Label(input_frame, text = "Give the name of the asjp style textfile you want to analyze")
        self.label.grid(row = 0, column = 1)

        self.entry = Entry(input_frame)
        self.entry.grid(row = 1, column = 1)

root = Tk()
app = App(root)
root.mainloop()