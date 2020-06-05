import lyricsgenius
import spotipy
import constants
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

if __name__ == "__main__":
    genius = lyricsgenius.Genius(constants.GENIUS_ACCESS_TOKEN)

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
