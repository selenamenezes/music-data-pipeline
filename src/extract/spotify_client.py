import requests

class SpotifyClient:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self.access_token = None

    def authenticate(self):
        url = "https://accounts.spotify.com/api/token"

        data = {
            "grant_type": "client_credentials"
        }

        response = requests.post(
            url,
            data=data,
            auth=(self.client_id, self.client_secret)
        )

        token_data = response.json()
        self.access_token = token_data["access_token"]

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}"
        }