import pytest
import os
from pathlib import Path
from mp3_player import list_folder, load_playlist, make_playlist

def test_make_playlist(tmp_path, monkeypatch):
    tracks = ["Track_1.mp3", "Track_2.mp3", "Track_3.mp3"]

    monkeypatch.chdir(tmp_path)
    make_playlist("1,2,3", "test_playlist_1", tracks)
    expected = Path("final_project/playlists") / "test_playlist_1.txt"

    assert expected.exists(), f"Expected Playlist file {expected} to be created"


def test_list_folder():
    assert list_folder("final_project/test_files") == ["mock_playlist_1.txt", "mock_playlist_2.txt", "mock_playlist_3.txt"]

def test_load_playlist():
    assert load_playlist("final_project/test_files/mock_playlist_1.txt") == ["Track_1.mp3", "Track_2.mp3", "Track_3.mp3"]
    assert load_playlist("final_project/test_files/mock_playlist_2.txt") == ["Track_2.mp3", "Track_3.mp3", "Track_1.mp3"]
    assert load_playlist("final_project/test_files/mock_playlist_3.txt") == ["Track_12.mp3", "Track_24.mp3", "Track_3.mp3", "Tabernacle_Choir.mp3"]


pytest.main(["-v", "--tb=line", "-rN", "final_project/test_mp3_player.py"])