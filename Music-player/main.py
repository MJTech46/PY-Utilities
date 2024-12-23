import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Buttons
        tk.Button(self.root, text="Load Music", command=self.load_music).pack(pady=10)
        tk.Button(self.root, text="Play", command=self.play_music).pack(pady=10)
        tk.Button(self.root, text="Pause", command=self.pause_music).pack(pady=10)
        tk.Button(self.root, text="Resume", command=self.resume_music).pack(pady=10)
        tk.Button(self.root, text="Stop", command=self.stop_music).pack(pady=10)

        self.file_path = None
        self.is_paused = False

    def load_music(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]
        )
        if self.file_path:
            pygame.mixer.music.load(self.file_path)
            print(f"Loaded: {self.file_path}")

    def play_music(self):
        if self.file_path:
            pygame.mixer.music.play()
            print("Playing music")

    def pause_music(self):
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            print("Music paused")

    def resume_music(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            print("Music resumed")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_paused = False
        print("Music stopped")


if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
  
