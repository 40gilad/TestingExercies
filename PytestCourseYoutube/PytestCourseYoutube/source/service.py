import requests


# -------------------------------- Requests API --------------------------------#
# in 1:05:07 in the video,
# were gonna requests api to make an actual request to an endpoint to get json of users

def get_users_from_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        data = response.json()

        modified_data = [
            {key + " kaki": val for key, val in user.items()}
            for user in data
        ]

        return modified_data  # Now the modified keys will be returned

    raise requests.HTTPError("Failed to fetch data")

