import tkinter as tk
import pygame
import os

pygame.mixer.init()

root = tk.Tk()
root.title("Music Player")
root.geometry("500x400")

song_list = tk.Listbox(root, width=50, height=15)
song_list.pack(pady=20)

songs = [f for f in os.listdir("Music") if f.endswith(".mp3")]

for song in songs:
    song_list.insert(tk.END, song)

def play_song():
    selected = song_list.get(song_list.curselection())

    file_path = os.path.join("Music", selected)

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

play_btn = tk.Button(
    root,
    text="Play",
    command=play_song
)

play_btn.pack()

root.mainloop()