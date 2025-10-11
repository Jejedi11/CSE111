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
    #folder = list_folder("final_project/songs")
    #song = input("Select a song to play: ")
    #play_song(f"final_project/songs/{folder[int(song) - 1]}")

    while True:
        select = ""
        if select == "1":
            list_folder("final_project/songs")
        if select == "2":
            play_song()

if __name__ == "__main__":
    main()