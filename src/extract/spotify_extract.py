from src.extract.spotify_client import SpotifyClient
import os
from dotenv import load_dotenv

load_dotenv()

def search_tracks(query):
    spotify = SpotifyClient(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"), client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
    spotify.authenticate()
    data = spotify.get("search", params={
        "q": query,
        "type": "track"
    })

    return data

search_tracks("nirvana")