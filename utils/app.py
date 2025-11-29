from tkinter import Tk, Label, Button

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("My Application")
        self.root.geometry("400x300")


    def setup_gui(self):
        title_label = Label(self.root, text="Welcome to My Application", font=("Helvetica", 16))
        title_label.pack(pady=20)

    def run(self):
        self.setup_gui()
        self.root.mainloop()


