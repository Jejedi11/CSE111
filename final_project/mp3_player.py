import random
import os
import vlc
import time

def play_song(song):
    player = vlc.MediaPlayer(song)
    player.play()
    time.sleep(10)

def list_folder(folder):
    index = 1
    song_list = os.listdir(folder)
    for i in song_list:
        print(f"{index}: {i}")
        index += 1
    return song_list

def load_playlist(playlist_file):
    pass

def make_playlist():
    pass

def main():
    while True:
        print("Welcome to the mp3 player")
        print("1. Load playlist")
        print("2. Make playlist")
        print("3. Quit")
        player_mode = input("Choose an option: ")

        if player_mode == "1":
            pass
        elif player_mode == "2":
            make_playlist()
        elif player_mode == "3":
            break

if __name__ == "__main__":
    main()