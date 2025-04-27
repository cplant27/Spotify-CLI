import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import spotipy.util as util

# Get username from terminal
username = os.getlogin()

# Erase Cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope=["user-library-read", 'playlist-modify', 'user-read-private','streaming'])
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope=["user-library-read", 'playlist-modify', 'user-read-private','streaming'])

# Create spotify object
s = spotipy.Spotify(auth = token)
user = s.current_user()

#get input from user
rawInput = input('\n\nEnter a list of artists separated by commas: ')


Input = rawInput.split(',')     #list of inputted artist names
inputID = []     #list of inputted artists' IDs
songs = []     #list of inputted artists' top 10 songs


#create list of inputted artists' IDs
for artist in Input:
    inputID.append( s.search(artist,1,0,'artist')['artists']['items'][0]['id'] )


#create a list of inputted artists' top 10 songs
for ID in inputID:
    for i in range( len( s.artist_top_tracks(s.artist(ID)['id'])['tracks'] ) ):
        songs.append( s.artist_top_tracks(s.artist(ID)['id'])['tracks'][i]['id'] )


#create playlist
s.user_playlist_create(user['id'],rawInput)

#find created playlist and assign to plylst
for i in range(len(s.current_user_playlists()['items'])):
    if s.current_user_playlists()['items'][i]['name'] == rawInput:
        plylst = s.current_user_playlists()['items'][i]
        break

#add songs to playlist
s.playlist_add_items(plylst['id'],songs)

in2 = input('\n\nYour playlist has been crated!\n\nWould you like to listen now? (Y/N):')

if in2.upper() == 'Y':
    s.start_playback(None,plylst['uri'])
    s.shuffle(True)
else:
    print('\n\nhave a great day\n')



