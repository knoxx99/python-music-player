import tkinter as tk
from tkinter import filedialog
import pygame
import os
import random

pygame.mixer.init()

MUSIC_FOLDER = "Music"

root = tk.Tk()
root.title("🎵 Python Music Player")
root.geometry("1000x700")
root.configure(bg="#1E1E1E")
root.resizable(False, False)



# Current song label
current_song = tk.StringVar()
current_song.set("🎵 No song selected")

song_label = tk.Label(
    root,
    textvariable=current_song,
    font=("Arial",12),
    bg="#1E1E1E",
    fg="white"
)
song_label.pack(pady=10)

search_frame = tk.Frame(root, bg="#1E1E1E")
search_frame.pack(pady=5)

search_label = tk.Label(
    search_frame,
    text="🔍 Search:",
    bg="#1E1E1E",
    fg="white"
)
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(
    search_frame,
    width=40,
    font=("Arial", 11)
)
search_entry.pack(side=tk.LEFT)

# Song list
song_list = tk.Listbox(
    root,
    width=60,
    height=15,
    font=("Arial", 11),
    bg="#2D2D2D",
    fg="white",
    selectbackground="#007ACC",
    selectforeground="white",
    relief="flat",
    borderwidth=0
)

songs = []

if os.path.exists(MUSIC_FOLDER):
    songs = [
        file for file in os.listdir(MUSIC_FOLDER)
        if file.endswith(".mp3")
    ]

for song in songs:
    song_list.insert(tk.END, song)

total_label = tk.Label(
    root,
    text=f"Total Songs: {len(songs)}",
    bg="#1E1E1E",
    fg="white",
    font=("Arial", 10)
)
total_label.pack()

song_list.pack(pady=10)
if songs:
    song_list.selection_set(0)
    song_list.activate(0)

def play_song():
    if not song_list.curselection():
        return

    selected_index = song_list.curselection()[0]
    selected_song = song_list.get(selected_index)

    file_path = os.path.join(MUSIC_FOLDER, selected_song)

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    current_song.set(f"Now Playing: {selected_song}")


def pause_song():
    pygame.mixer.music.pause()


def resume_song():
    pygame.mixer.music.unpause()


def stop_song():
    pygame.mixer.music.stop()
    current_song.set("Playback Stopped")


def change_volume(value):
    pygame.mixer.music.set_volume(float(value) / 100)

def previous_song():

    if not songs:
        return

    if not song_list.curselection():
        index = 0
    else:
        index = song_list.curselection()[0]

    index = (index - 1) % len(songs)

    song_list.selection_clear(0, tk.END)
    song_list.selection_set(index)
    song_list.activate(index)

    play_song()

def next_song():

    if not songs:
        return

    if not song_list.curselection():
        index = 0
    else:
        index = song_list.curselection()[0]

    index = (index + 1) % len(songs)

    song_list.selection_clear(0, tk.END)
    song_list.selection_set(index)
    song_list.activate(index)

    play_song()

def shuffle_song():

    if len(songs) <= 1:
        return

    current = song_list.curselection()[0] if song_list.curselection() else -1

    index = random.randint(0, len(songs) - 1)

    while index == current:
        index = random.randint(0, len(songs) - 1)

    song_list.selection_clear(0, tk.END)
    song_list.selection_set(index)
    song_list.activate(index)

    play_song()

def search_song(event=None):
    keyword = search_entry.get().strip().lower()

    song_list.delete(0, tk.END)

    if keyword == "":
        for song in songs:
            song_list.insert(tk.END, song)
        return

    for song in songs:
        if keyword in song.lower():
            song_list.insert(tk.END, song)
search_entry.bind("<KeyRelease>", search_song)

def open_folder():
    global MUSIC_FOLDER, songs

    folder = filedialog.askdirectory(title="Select Music Folder")

    if not folder:
        return

    MUSIC_FOLDER = folder

    songs = [
        file for file in os.listdir(MUSIC_FOLDER)
        if file.endswith(".mp3")
    ]

    song_list.delete(0, tk.END)

    for song in songs:
        song_list.insert(tk.END, song)

    total_label.config(text=f"Total Songs: {len(songs)}")

    if songs:
        current_song.set("🎵 Folder Loaded Successfully")
        song_list.selection_set(0)
        song_list.activate(0)
    else:
        current_song.set("❌ No MP3 files found")

    if songs:
        song_list.selection_set(0)
        song_list.activate(0)

folder_btn = tk.Button(
    root,
    text="📂 Open Folder",
    command=open_folder,
    bg="#2D2D2D",
    fg="white",
    activebackground="#3C3C3C",
    activeforeground="white",
    width=20
)

folder_btn.pack(pady=5)
song_list.bind("<Double-Button-1>", lambda event: play_song())

# Buttons Frame
button_frame = tk.Frame(root, bg="#1E1E1E")
button_frame.pack(pady=10)

play_btn = tk.Button(
    button_frame,
    text="▶ Play",
    command=play_song,
    bg="#2D2D2D",
    fg="white",
    activebackground="#3C3C3C"
)
play_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(
    button_frame,
    text="Pause",
    width=10,
    command=pause_song,
    bg = "#2D2D2D",
    fg = "white",
    activebackground = "#3C3C3C",
    activeforeground = "white"
)
pause_btn.grid(row=0, column=1, padx=5)

resume_btn = tk.Button(
    button_frame,
    text="Resume",
    width=10,
    command=resume_song,
    bg = "#2D2D2D",
    fg = "white",
    activebackground = "#3C3C3C",
    activeforeground = "white"
)
resume_btn.grid(row=0, column=2, padx=5)

stop_btn = tk.Button(
    button_frame,
    text="Stop",
    width=10,
    command=stop_song,
    bg = "#2D2D2D",
    fg = "white",
    activebackground = "#3C3C3C",
    activeforeground = "white"
)
stop_btn.grid(row=0, column=3, padx=5)

previous_btn = tk.Button(
    button_frame,
    text="⏮ Previous",
    command=previous_song,
    bg = "#2D2D2D",
    fg = "white",
    activebackground = "#3C3C3C",
    activeforeground = "white"
)
previous_btn.grid(row=0, column=4, padx=5)

next_btn = tk.Button(
    button_frame,
    text="⏭ Next",
    command=next_song,
    bg = "#2D2D2D",
    fg = "white",
    activebackground = "#3C3C3C",
    activeforeground = "white"
)
next_btn.grid(row=0, column=5, padx=5)

shuffle_btn = tk.Button(
    root,
    text="🔀 Shuffle",
    command=shuffle_song,
    bg = "#2D2D2D",
    fg = "white",
    activebackground = "#3C3C3C",
    activeforeground = "white"
)
shuffle_btn.pack(pady=10)

# Volume Control
volume_label = tk.Label(
    root,
    text="🔊 Volume",
    bg="#1E1E1E",
    fg="white"
)
volume_label.pack()

volume_slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    command=change_volume,
    bg="#1E1E1E",
    fg="white",
    troughcolor="#2D2D2D",
    highlightthickness=0
)
volume_slider.set(50)
pygame.mixer.music.set_volume(0.5)
volume_slider.pack()

root.mainloop()