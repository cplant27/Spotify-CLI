import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import os
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

print('\n')

# Get username from terminal
username = os.getlogin()

# wpia9ov4me8c4k0jd1mqsydf0?si=160319f9c8154fce

# Erase Cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope=["user-library-read", 'playlist-modify', 'user-read-private','user-top-read','user-read-recently-played','user-read-currently-playing'])
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope=["user-library-read", 'playlist-modify', 'user-read-private','user-top-read','user-read-recently-played','user-read-currently-playing'])

# Create spotify object
spotifyObject = spotipy.Spotify(auth = token)

#check current song
currentSongID = spotifyObject.currently_playing()['item']['id']

#check what playlists that song is in
suggestedPlaylists = spotifyObject.category_playlists('hiphop')['playlists']['items']
for i in range( len( suggestedPlaylists ) ):  #loop thru suggested playlists
    
    if currentSongID in spotifyObject.playlist_items( suggestedPlaylists[i]['id'] )['items']:  #loop thru songs in current suggested playlists
        print( spotifyObject.category_playlists('hiphop')['playlists']['items'][i]['name'] )
#        if spotifyObject.playlist_items( spotifyObject.category_playlists('hiphop')['playlists']['items'][i]['id'] )['items'][j]['track']['id'] == songID:   # if songID == current songID print playlist name
 #           print( spotifyObject.category_playlists('hiphop')['playlists']['items'][i]['name'] )
  #          break


#check what playlists contains most of the recently played songs
spotifyObject.current_user_recently_played()['items'][0]['track']['name']

#return playlist

