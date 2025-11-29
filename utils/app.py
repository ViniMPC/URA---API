from tkinter import Tk

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("My Application")
        self.root.geometry("400x300")

    

    def run(self):
        self.root.mainloop()


