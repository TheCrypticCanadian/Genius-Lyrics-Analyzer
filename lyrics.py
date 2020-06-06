import lyricsgenius
import spotipy
import constants
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

if __name__ == "__main__":
    genius = lyricsgenius.Genius(constants.GENIUS_ACCESS_TOKEN)
    
    genius.remove_section_headers = True
    genius.verbose = False

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(constants.SPOTIPY_CLIENT_ID,constants.SPOTIPY_CLIENT_SECRET))

    search_string = str(input("Track name: "))
    print("")

    results = sp.search(q=search_string, type="track", limit=20)
    
    songList = []
    albumName = ""

    for idx, track in enumerate(results['tracks']['items']):
        #pprint(track)
        if int(idx) == 0:
            print(str(track['name'])+" - "+str(track['artists'][0]['name']))
            print()
            song = genius.search_song(str(track['name']),str(track['artists'][0]['name']))
            print(song.lyrics)


    """
    for idx, album in enumerate(results['albums']['items']):
        pprint(album)
        print(str(album['name'])+" - "+str(album['artists'][0]['name']))
        if int(idx) == 0:
            albumName = album['name']
    """        
