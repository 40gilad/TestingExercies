import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv


def jsonify(s):
    import ast
    import json
    if not isinstance(s, str):
        s = str(s)
    return json.dumps(ast.literal_eval(s), indent=4)


class GiladSpotifyClass:
    def __init__(self, redirect_uri: str = "http://localhost:1234", scope: str = "playlist-modify-public"):
        REDIRECT_URI = redirect_uri
        SCOPE = scope
        load_dotenv(dotenv_path=r"C:\Users\40gil\Desktop\not_work\my_scipts\TestingExercies\SpotifyToMp3\SpotifyToMp3"
                                r"\source\key.env")
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                            client_secret=CLIENT_SECRET,
                                                            redirect_uri=REDIRECT_URI,
                                                            scope=SCOPE))

    def get_playlist(self, name):
        results = self.sp.current_user_playlists(limit=100)
        if results is None:
            return None

        for playlist in results['items']:
            if name == playlist['name']:
                return {"id": playlist["id"], "name": playlist['name']}

    def get_songs_from_playlist(self, playlist_id):
        try:
            playlist_tracks = self.sp.playlist_tracks(playlist_id)
        except spotipy.exceptions.SpotifyException:
            raise ValueError(f"Playlist id '{playlist_id}' not found or invalid")
        if not playlist_tracks:
            raise ValueError(f"Playlist id '{playlist_id}' not found or invalid")
        ret = [
            {
                "name": i['track']['name'],
                "artist": i['track']['artists'][0]['name'],
                "song_id": i['track']["id"]
            }
            for i in playlist_tracks['items']
        ]
        return None if ret == [] else ret


if __name__ == "__main__":
    kaki = GiladSpotifyClass()
    pipi = kaki.get_playlist("abc")
    b = 1
