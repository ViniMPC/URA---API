import customtkinter as ctk

class App:
    def __init__(self):
        ctk.set_appearance_mode("dark")        # dark, light, system

        self.root = ctk.CTk()
        self.root.title("My Application")
        self.root.geometry("400x300")

    def setup_gui(self):
        ctk.CTkLabel(
            self.root, 
            text="Bem-vindo!", 
            font=("Arial", 22)
        ).pack(pady=20)

        ctk.CTkButton(
            self.root, 
            text="Entrar"
        ).pack(pady=10)

        ctk.CTkButton(
            self.root, 
            text="Configurações", 
            fg_color="gray30"
        ).pack()

    def run(self):
        self.setup_gui()
        self.root.mainloop()
