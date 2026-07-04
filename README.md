# Python Music Player

A desktop music player developed using **Python**, **Tkinter**, and **Pygame**. The application provides a simple graphical interface for playing MP3 files, managing playlists, and controlling audio playback.

## Overview

This project was created to explore desktop application development in Python by combining graphical user interfaces with multimedia programming. The application automatically loads MP3 files from a selected folder and provides essential playback controls through an intuitive interface.

## Features

* Graphical user interface built with Tkinter
* Automatic detection of MP3 files
* Play, Pause, Resume, and Stop playback
* Previous and Next track navigation
* Shuffle playback
* Search songs in real time
* Open any local music folder
* Volume control with slider
* Display currently playing track
* Display total number of songs
* Double-click a song to start playback
* Dark-themed user interface

## Technologies

* Python 3
* Tkinter
* Pygame
* OS Module
* Random Module

## Project Structure

```text
python-music-player/
│
├── Music/
│   ├── song1.mp3
│   ├── song2.mp3
│   └── ...
│
├── gui_player.py
├── main.py
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/knoxx99/python-music-player.git
```

Move into the project directory:

```bash
cd python-music-player
```

Install the required dependency:

```bash
pip install pygame
```

Run the application:

```bash
python gui_player.py
```

## Usage

1. Launch the application.
2. Select a song from the playlist or open another folder containing MP3 files.
3. Double-click a song or press **Play**.
4. Use the playback controls to navigate through the playlist.
5. Search songs using the search box.
6. Adjust the volume using the slider.

## Implemented Features

| Feature               | Status |
| --------------------- | :----: |
| GUI Interface         |    ✅   |
| MP3 Playback          |    ✅   |
| Playlist              |    ✅   |
| Play / Pause / Resume |    ✅   |
| Stop Playback         |    ✅   |
| Previous / Next Track |    ✅   |
| Shuffle               |    ✅   |
| Search Songs          |    ✅   |
| Open Folder           |    ✅   |
| Volume Control        |    ✅   |
| Current Song Display  |    ✅   |
| Double-Click Playback |    ✅   |
| Dark Theme            |    ✅   |

## Future Improvements

* Playback progress bar
* Song duration display
* Repeat mode
* Favorites playlist
* Album artwork
* Music metadata (Artist, Album, Duration)
* Keyboard shortcuts
* Playlist import/export
* Recently played history

## Learning Outcomes

This project helped strengthen practical knowledge of:

* Python programming
* Tkinter GUI development
* Audio playback with Pygame
* Event-driven programming
* File handling
* Desktop application development
* User interface design

## Author

**Kaustubh Gedam**

## License

This project is open for educational and learning purposes.


