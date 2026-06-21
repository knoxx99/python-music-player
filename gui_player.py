import tkinter as tk
import pygame
import os
import random

pygame.mixer.init()

MUSIC_FOLDER = "Music"

root = tk.Tk()
root.title("🎵 Python Music Player")
root.geometry("700x550")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

# Current song label
current_song = tk.StringVar()
current_song.set("No song selected")

song_label = tk.Label(
    root,
    textvariable=current_song,
    font=("Arial",12),
    bg="#1E1E1E",
    fg="white"
)
song_label.pack(pady=10)



# Song list
# Song list
song_list = tk.Listbox(
    root,
    width=60,
    height=15,
    bg="#2D2D2D",
    fg="white",
    selectbackground="#007ACC",
    selectforeground="white"
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

    if not songs:
        return

    index = random.randint(0, len(songs)-1)

    song_list.selection_clear(0, tk.END)
    song_list.selection_set(index)
    song_list.activate(index)

    play_song()
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