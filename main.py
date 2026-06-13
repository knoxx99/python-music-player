import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import random
def load_music(folder,song_name):
    file_path = os.path.join(folder,song_name)
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def play_music(folder,song_name,song_list,song_num):
    file_path = os.path.join(folder,song_name)
    current_volume = 0.5
    history = [song_name]
    pygame.mixer.music.set_volume(current_volume)
    if not os.path.exists(file_path):
        print("File not found!")
        return
    load_music(folder, song_name)
    print(f"Now playing {song_name}")
    print("commands: [P]ause, [R]esume, [S]top, [N]ext, [B]ack, [+]Volume, [-]Volume, [H]suffle, [L] List Recently Played Songs")

    while True:
        command = input ("> ").strip().upper()
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
        elif command == "N":
            song_num = (song_num + 1) % len(song_list)
            history.append(song_list[song_num])
            load_music(folder,song_list[song_num])
            print(f"Now playing {song_list[song_num]}")
        elif command == "B":
            song_num = (song_num - 1) % len(song_list)
            history.append(song_list[song_num])
            load_music(folder, song_list[song_num])
            print(f"Now playing {song_list[song_num]}")
        elif command == "+":
            current_volume = min(1.0, current_volume + 0.2)
            pygame.mixer.music.set_volume(current_volume)
            print(f"Volume: {current_volume:.1f}")
        elif command == "-":
            current_volume = max(0.0, current_volume - 0.2)
            pygame.mixer.music.set_volume(current_volume)
            print(f"Volume: {current_volume:.1f}")
        elif command == "H":
            if len(song_list) == 1:
                print("Only one song available")
                continue
            new_song = random.randint(0, len(song_list) - 1)

            while new_song == song_num:
                new_song = random.randint(0, len(song_list) - 1)

            song_num = new_song
            history.append(song_list[song_num])
            load_music(folder, song_list[song_num])

            print(f"Now playing {song_list[song_num]}")
        elif command == "L":
            print("\nRecently Played:")
            for i, song in enumerate(history[-5:], start=1):
                print(f"{i}. {song}")
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
            play_music(folder, mp3_files[choice],mp3_files,choice)
        else:
            print("Invalid choice!")

if __name__=="__main__":
    main()
