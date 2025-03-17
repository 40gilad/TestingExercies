import pytest
import source.spotify_downloader as sd
import unittest.mock as mock
from tests.helpers.helpers import HelperTestSpotifyDownloader as HTSD
import os
import shutil


# region Fixtures
@pytest.fixture
def test_helper():
    """Fixture to provide a single instance of the helper class for all tests."""
    return HTSD()


@pytest.fixture
def spotify_class():
    instance = sd.GiladSpotifyClass()
    yield instance
    instance.sp = None


@pytest.fixture
def mocked_sp_playlists():
    with mock.patch('source.spotify_downloader.spotipy.Spotify.current_user_playlists') as m:
        yield m


@pytest.fixture
def mocked_sp_tracks():
    with (mock.patch('source.spotify_downloader.spotipy.Spotify.playlist_tracks') as m):
        yield m


@pytest.fixture
def mocked_get_video_url_get():
    with mock.patch('source.spotify_downloader.requests.get') as m:
        yield m


# endregion

# region Test Playlists
@pytest.mark.parametrize("playlist_name, expected_output", HTSD().get_parmeterize_pairs_for_test_get_playlist())
def test_get_playlist(mocked_sp_playlists, spotify_class, test_helper, playlist_name, expected_output):
    # Arrange
    mocked_sp_playlists.return_value = test_helper.load_json(r"mocked_jsons\playlists\AllPlaylists")

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


# endregion

# region Test Songs
@pytest.mark.parametrize("playlist_name,playlist_id, expected_output",
                         HTSD().get_parmeterize_pairs_for_test_get_songs_from_playlist())
def test_get_songs_from_playlist(mocked_sp_tracks, spotify_class, test_helper, playlist_name, playlist_id,
                                 expected_output):
    # arrange
    mocked_sp_tracks.return_value = test_helper.load_json(fr"mocked_jsons\songs\{playlist_name}")

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


@pytest.mark.parametrize("song,expected_output", [(HTSD().get_parmeterize_pairs_for_test_get_video_url())])
def test_get_video_url(mocked_get_video_url_get, spotify_class, song, expected_output):
    # arrange
    mock_file_path = r"C:\Users\40gil\Desktop\not_work\my_scipts\TestingExercies\SpotifyToMp3\SpotifyToMp3\tests\data\mocked_htmls\fortunate_son.html"
    with open(mock_file_path, "r", encoding="utf-8") as f:
        mock_html_content = f.read()
    mocked_get_video_url_get.return_value = mock.Mock(
        status_code=200, text=mock_html_content
    )

    # act
    actual_result = spotify_class.get_video_url(song)

    # assert
    assert actual_result == expected_output, f"Expected {expected_output}\n got {actual_result}"

# endregion
# def test_download_url_from_ytdll():
#     assert True
#
#
# def test_change_metadata():
#     assert True
