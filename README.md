# Python Music Player

A command-line music player developed in Python using Pygame. The application allows users to manage and play local MP3 files with playback controls, playlist navigation, shuffle functionality, volume adjustment, and playback history tracking.

## Overview

This project was created to explore audio playback programming in Python and to gain hands-on experience with file handling, user input management, and application flow control.

## Features

* Play MP3 audio files from a local music directory
* Pause and resume playback
* Stop the currently playing track
* Navigate to the next or previous track
* Shuffle songs randomly
* Adjust playback volume
* View recently played tracks
* Automatic loading of available MP3 files
* Command-line based user interface
* Basic error handling and input validation

## Technologies Used

* Python 3
* Pygame
* OS Module
* Random Module

## Project Structure

```text
MusicPlayer/
│
├── Music/
│   ├── song1.mp3
│   ├── song2.mp3
│   └── ...
│
├── main.py
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd MusicPlayer
```

3. Install dependencies:

```bash
pip install pygame
```

4. Create a `Music` folder and add your MP3 files.

5. Run the application:

```bash
python main.py
```

## Available Commands

| Command | Description                    |
| ------- | ------------------------------ |
| P       | Pause playback                 |
| R       | Resume playback                |
| S       | Stop playback                  |
| N       | Play next track                |
| B       | Play previous track            |
| H       | Shuffle playlist               |
| +       | Increase volume                |
| -       | Decrease volume                |
| L       | Display recently played tracks |

## Recent Updates

### Playback History

Implemented a playback history feature that stores recently played tracks during the current session. Users can review the latest tracks using the `L` command.

## Future Improvements

* Favorites playlist support
* Persistent playback history
* Track duration display
* Automatic next-track playback
* Search functionality
* Graphical user interface (GUI)

## Learning Outcomes

This project helped strengthen understanding of:

* Python programming fundamentals
* Working with external libraries
* Audio playback management using Pygame
* File system operations
* User input handling
* Command-line application development

## License

This project is available for learning and educational purposes.
