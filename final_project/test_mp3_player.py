import pytest
from mp3_player import play_song, list_folder, load_playlist

def test_play_song():
    assert play_song("final_project/songs/track_10.mp3") == True
    assert play_song("final_project/songs/") == False

def test_list_folder():
    pass

def test_load_playlist():
    pass

pytest.main(["-v", "--tb=line", "-rN", "final_project/test_mp3_player.py"])