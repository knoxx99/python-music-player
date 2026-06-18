import tkinter as tk
import os

root = tk.Tk()
root.title("Music Player")
root.geometry("500x400")

song_list = tk.Listbox(root, width=50, height=15)
song_list.pack(pady=20)

songs = [f for f in os.listdir("Music") if f.endswith(".mp3")]

for song in songs:
    song_list.insert(tk.END, song)

play_btn = tk.Button(root, text="Play")
play_btn.pack()

root.mainloop()