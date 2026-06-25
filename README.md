# Python Music Player

A desktop music player developed in **Python** using **Tkinter** for the graphical user interface and **Pygame** for audio playback. The application provides an intuitive interface for playing MP3 files stored on the local system while demonstrating event-driven programming and multimedia handling in Python.

---

## Features

* Modern graphical user interface (GUI) built with Tkinter
* Automatic loading of MP3 files from the `Music` directory
* Interactive playlist
* Double-click a song to start playback
* Play, Pause, Resume and Stop controls
* Previous and Next track navigation
* Shuffle playback
* Volume control using a slider
* Displays the currently playing track
* Displays the total number of songs available
* Dark theme user interface
* Basic input validation and error handling

---

## Technologies Used

* Python 3
* Tkinter
* Pygame
* OS Module
* Random Module

---

## Project Structure

```text
Python-Music-Player/
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

---

## Installation

Clone the repository:

```bash
git clone https://github.com/knoxx99/python-music-player.git
```

Navigate to the project directory:

```bash
cd python-music-player
```

Install the required package:

```bash
pip install pygame
```

Run the GUI application:

```bash
python gui_player.py
```

---

## Current Functionality

| Feature               | Status |
| --------------------- | :----: |
| GUI Interface         |    ✅   |
| MP3 Playback          |    ✅   |
| Playlist              |    ✅   |
| Play / Pause / Resume |    ✅   |
| Stop Playback         |    ✅   |
| Previous / Next Track |    ✅   |
| Shuffle               |    ✅   |
| Volume Control        |    ✅   |
| Current Song Display  |    ✅   |
| Double-Click to Play  |    ✅   |
| Song Counter          |    ✅   |
| Dark Theme            |    ✅   |

---

## Planned Enhancements

* Search songs
* Open music folder from the application
* Automatic playback of the next track
* Playback progress bar
* Track duration display
* Favorites playlist
* Repeat mode
* Album artwork support
* Music metadata (Artist, Album, Duration)
* Keyboard shortcuts
* Playlist export/import

---

## Learning Outcomes

This project demonstrates practical experience with:

* Python programming
* GUI development using Tkinter
* Audio playback using Pygame
* Event-driven programming
* File system operations
* Desktop application development
* Basic user interface design

---

## License

This project is intended for educational and learning purposes.
