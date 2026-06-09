import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import pygame

def play_music(folder,song_num):
    file_path = os.path.join(folder,song_num)

    if not os.path.exists(file_path):
        print("File not found!")
        return
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"Now playing {song_num}")
    print("commands: [P]ause, [R]esume, [S]top")

    while True:
        command = input ("> ").upper()
        if command == "P":
            pygame.mixer.music.pause()
            print("paused")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("unpaused")
        elif command == "S":
            pygame.mixer.music.stop()
            print("stopped")
            return
        else :
            print("Invalid command!")

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
      print("Audio initialization failed! ",e)
      return
    folder = "Music"
    if not os.path.isdir(folder):
        print(f"Folder {folder} not found.")
        return
    mp3_files =sorted(
        [file for file in os.listdir(folder) if file.endswith(".mp3")]
    )
    print(mp3_files)
    if not mp3_files:
        print("No mp3 files found.")
        return

    while True:
        print("****** Music Player ******")
        print("My Song List :")

        for index, song in enumerate(mp3_files , start=1):
            print(f"{index}.{song}")

        choice_input = input("\n Enter song to play or 'Q' to exit :")
        if choice_input.upper() == "Q":
            print("BYE!")
            break
        if not choice_input.isdigit():
            print("INVALID INPUT!")
            continue
        choice = int(choice_input) - 1
        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice!")

if __name__=="__main__":
    main()
