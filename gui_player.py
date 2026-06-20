import tkinter as tk
import pygame
import os

pygame.mixer.init()

MUSIC_FOLDER = "Music"

root = tk.Tk()
root.title("Python Music Player")
root.geometry("600x500")

# Current song label
current_song = tk.StringVar()
current_song.set("No song selected")

song_label = tk.Label(
    root,
    textvariable=current_song,
    font=("Arial", 12)
)
song_label.pack(pady=10)

# Song list
song_list = tk.Listbox(root, width=60, height=15)
song_list.pack(pady=10)

songs = []

if os.path.exists(MUSIC_FOLDER):
    songs = [
        file for file in os.listdir(MUSIC_FOLDER)
        if file.endswith(".mp3")
    ]

for song in songs:
    song_list.insert(tk.END, song)


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


# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

play_btn = tk.Button(
    button_frame,
    text="Play",
    width=10,
    command=play_song
)
play_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(
    button_frame,
    text="Pause",
    width=10,
    command=pause_song
)
pause_btn.grid(row=0, column=1, padx=5)

resume_btn = tk.Button(
    button_frame,
    text="Resume",
    width=10,
    command=resume_song
)
resume_btn.grid(row=0, column=2, padx=5)

stop_btn = tk.Button(
    button_frame,
    text="Stop",
    width=10,
    command=stop_song
)
stop_btn.grid(row=0, column=3, padx=5)

# Volume Control
volume_label = tk.Label(root, text="Volume")
volume_label.pack()

volume_slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    command=change_volume
)
volume_slider.set(50)
volume_slider.pack()

root.mainloop()