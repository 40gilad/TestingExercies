import pytest
import source.spotify_downloader as sd
import unittest.mock as mock
import json
import os


def load_json(sub_path):
    f = fr"C:\Users\40gil\Desktop\not_work\my_scipts\TestingExercies\SpotifyToMp3\SpotifyToMp3\tests\data\{sub_path}.json"
    if os.path.getsize(f) == 0:  # Check if the file is empty
        return None
    with open(f) as file:
        return json.load(file)


def get_parmeterize_pairs_for_test_get_songs_from_playlist():
    playlists_names = ["Moz17_3", "Movies", "Drock"]
    return [(p, load_json(fr"expected_jsons\playlists\{p}")["id"], load_json(fr"expected_jsons\songs\{p}")) for p in
            playlists_names]


def get_parmeterize_pairs_for_test_get_playlist():
    playlists_names = ["Moz17_3", "Movies", "Drock"]
    return [(p, load_json(fr"expected_jsons\playlists\{p}")) for p in playlists_names]


@pytest.fixture
def spotify_class():
    instance = sd.GiladSpotifyClass()
    yield instance
    instance.sp = None


@pytest.fixture
def mocked_sp_playlists():
    with mock.patch('source.spotify_downloader.spotipy.Spotify.current_user_playlists') as m:
        return m


@pytest.fixture
def mocked_sp_tracks():
    with mock.patch('source.spotify_downloader.spotipy.Spotify.playlist_tracks') as m:
        return m


@pytest.mark.parametrize("playlist_name, expected_output", get_parmeterize_pairs_for_test_get_playlist())
def test_get_playlist(mocked_sp_playlists, spotify_class, playlist_name, expected_output):
    # Arrange
    mocked_sp_playlists.return_value = load_json(r"mocked_jsons\playlists\AllPlaylists")

    # Act
    actual_result = spotify_class.get_playlist(playlist_name)

    # Assert
    assert actual_result == expected_output, f"Expected {expected_output}\n got {actual_result}"


@pytest.mark.parametrize("playlist_name, expected_output", [("A playlist that's not exist", None)])
def test_get_playlist_invalid_playlist(mocked_sp_playlists, spotify_class, playlist_name, expected_output):
    # Arrange
    mocked_sp_playlists.return_value = None

    # Act
    actual_result = spotify_class.get_playlist(playlist_name)

    # Assert
    assert actual_result == expected_output, f"Expected {expected_output}\n got {actual_result}"


@pytest.mark.parametrize("playlist_name,playlist_id, expected_output",
                         get_parmeterize_pairs_for_test_get_songs_from_playlist())
def test_get_songs_from_playlist(mocked_sp_tracks, spotify_class, playlist_name, playlist_id, expected_output):
    # arrange
    mocked_sp_tracks.return_value = load_json(fr"mocked_jsons\songs\{playlist_name}")

    # act
    actual_result = spotify_class.get_songs_from_playlist(playlist_id)

    # assert
    assert actual_result == expected_output, f"Expected {expected_output}\n got {actual_result}"


def test_get_songs_from_playlist_invalid_id(mocked_sp_tracks, spotify_class):
    # arrange
    mocked_sp_tracks.side_effect = ValueError

    # act & assert
    with pytest.raises(ValueError):
        spotify_class.get_songs_from_playlist("invalid_id")


#
# def test_create_folder():
#     assert True


#
# def test_get_video_url():
#     assert True
#
#
# def test_download_url_from_ytdll():
#     assert True
#
#
# def test_change_metadata():
#     assert True

if __name__ == "__main__":
    # test_get_playlist()
    kaki = test_get_playlist()
    a = 1
