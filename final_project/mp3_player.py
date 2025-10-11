import random
import os
import vlc
import time

def play_song(song):
    player = vlc.MediaPlayer(song)
    player.play()
    time.sleep(10)

def load_playlist(playlist_file):
    pass

def make_playlist():
    pass

def main():
    index = 1
    print("Select a song to play.")
    song_list = os.listdir("final_project/songs")
    for i in song_list:
        print(f"{index}: {i}")
        index += 1
    song = input(":") 
    play_song(f"final_project/songs/{song_list[int(song) - 1]}")

if __name__ == "__main__":
    main()