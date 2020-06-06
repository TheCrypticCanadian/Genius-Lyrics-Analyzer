import lyricsgenius
import spotipy
import constants
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

if __name__ == "__main__":
    genius = lyricsgenius.Genius(constants.GENIUS_ACCESS_TOKEN)

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(constants.SPOTIPY_CLIENT_ID,constants.SPOTIPY_CLIENT_SECRET))

    results = sp.search(q='Atrocity Exhibition', type="album", limit=20)
    
    for idx, album in enumerate(results['albums']['items']):
        #pprint(album)
        print(idx, album['name'], album['artists'][0]['name'])
