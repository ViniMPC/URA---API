import customtkinter as ctk
from PIL import Image, ImageDraw
import io

class App:
    def __init__(self):
        ctk.set_appearance_mode("dark")

        self.root = ctk.CTk()
        self.root.title("My Application")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.recording = False
        self.recorder = None

    def setup_gui(self):
        # Título
        title = ctk.CTkLabel(
            self.root, 
            text="Gravador de Áudio", 
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        # Frame de status
        status_frame = ctk.CTkFrame(self.root, fg_color="gray20")
        status_frame.pack(pady=15, padx=20, fill="x")
        
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="⚫ Pronto",
            font=("Arial", 16),
            text_color="gray"
        )
        self.status_label.pack(pady=15)

        # Frame de botões
        button_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        button_frame.pack(pady=20)

        # Botão Gravar
        self.record_btn = ctk.CTkButton(
            button_frame,
            text="⏺️  Gravar",
            command=self.start_recording,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            width=120,
            height=50,
            font=("Arial", 14, "bold")
        )
        self.record_btn.grid(row=0, column=0, padx=10)

        # Botão Parar
        self.stop_btn = ctk.CTkButton(
            button_frame,
            text="⏹️  Parar",
            command=self.stop_recording,
            fg_color="gray30",
            hover_color="gray40",
            width=120,
            height=50,
            font=("Arial", 14, "bold"),
            state="disabled"
        )
        self.stop_btn.grid(row=0, column=1, padx=10)

        # Botão Configurações
        config_btn = ctk.CTkButton(
            button_frame,
            text="⚙️  Configurações",
            fg_color="gray40",
            hover_color="gray50",
            width=120,
            height=50,
            font=("Arial", 14, "bold")
        )
        config_btn.grid(row=0, column=2, padx=10)

        # Info frame
        info_frame = ctk.CTkFrame(self.root, fg_color="gray20", corner_radius=10)
        info_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        info_label = ctk.CTkLabel(
            info_frame,
            text="✓ Gravação salva em: output.wav",
            font=("Arial", 12),
            text_color="green"
        )
        info_label.pack(pady=15)

    def start_recording(self):
        from utils.audio.audio_speaker import recorder
        
        self.recording = True
        self.recorder = recorder(temp=5, freq=44100, channels=2)
        
        self.record_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.status_label.configure(text="🔴 Gravando...", text_color="red")

    def stop_recording(self):
        if self.recording and self.recorder:
            self.recorder.record_audio("output.wav")
            self.recording = False
            
            self.record_btn.configure(state="normal")
            self.stop_btn.configure(state="disabled")
            self.status_label.configure(text="✅ Gravação concluída!", text_color="green")

    def run(self):
        self.setup_gui()
        self.root.mainloop()