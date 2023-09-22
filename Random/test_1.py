import tkinter as tk
from tkinter import filedialog
import pygame
from threading import Thread
import time

time.sleep(2)
class AudioPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")

        self.label = tk.Label(root, text="Select an audio file and press Play")
        self.label.pack(padx=20, pady=20)

        self.play_button = tk.Button(root, text="Play", command=self.play_audio)
        self.play_button.pack(padx=20, pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_audio)
        self.pause_button.pack(padx=20, pady=5)

        self.text_box = tk.Text(root, height=10, width=40)
        self.text_box.pack(padx=20, pady=10)

        self.playing = False

    def play_audio(self):
        if not self.playing:
            self.file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
            if self.file_path:
                self.playing = True
                self.play_button.config(state="disabled")
                self.pause_button.config(state="normal")
                pygame.mixer.init()
                pygame.mixer.music.load(self.file_path)
                pygame.mixer.music.play()
                self.text_box.insert(tk.END, "Playing: " + self.file_path + "\n")
                self.update_text_box()

    def pause_audio(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False
            self.play_button.config(state="normal")
            self.pause_button.config(state="disabled")
            self.text_box.insert(tk.END, "Paused\n")
            self.update_text_box()

    def update_text_box(self):
        def worker():
            while self.playing:
                self.text_box.see(tk.END)
                self.root.update_idletasks()
        
        thread = Thread(target=worker)
        thread.start()

if __name__ == "__main__":
    app = tk.Tk()
    AudioPlayerApp(app)
    app.mainloop()
