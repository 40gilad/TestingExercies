import json
import ast


def correct_json():
    path = r"C:\Users\40gil\Desktop\not_work\my_scipts\TestingExercies\SpotifyToMp3\SpotifyToMp3\tests\data\mocked_jsons\songs\Movies.json"

    # Read file
    with open(path, "r") as fr:
        content = fr.read()

    # Convert from invalid JSON to valid JSON
    try:
        data = ast.literal_eval(content)  # Convert single-quote JSON to Python dict
        corrected_json = json.dumps(data, indent=4)  # Convert back to properly formatted JSON
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return

    # Write back corrected JSON
    with open(path, "w") as fw:
        fw.write(corrected_json)


if __name__ == "__main__":
    correct_json()
