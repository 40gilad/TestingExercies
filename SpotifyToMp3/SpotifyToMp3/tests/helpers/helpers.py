import json
import os


class HelperTestSpotifyDownloader():
    def load_json(self, sub_path):
        f = fr"C:\Users\40gil\Desktop\not_work\my_scipts\TestingExercies\SpotifyToMp3\SpotifyToMp3\tests\data\{sub_path}.json"
        if os.path.getsize(f) == 0:  # Check if the file is empty
            return None
        with open(f) as file:
            return json.load(file)

    def get_parmeterize_pairs_for_test_get_songs_from_playlist(self):
        playlists_names = ["Moz17_3", "Movies", "Drock"]
        return [
            (p, self.load_json(fr"expected_jsons\playlists\{p}")["id"], self.load_json(fr"expected_jsons\songs\{p}"))
            for p in
            playlists_names]

    def get_parmeterize_pairs_for_test_get_playlist(self):
        playlists_names = ["Moz17_3", "Movies", "Drock"]
        return [(p, self.load_json(fr"expected_jsons\playlists\{p}")) for p in playlists_names]
