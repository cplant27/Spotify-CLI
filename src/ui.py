import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import os
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import tkinter

print('\n')

# Get username from terminal
username = os.getlogin()

# User ID: wpia9ov4me8c4k0jd1mqsydf0?si=160319f9c8154fce

# Erase Cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope=["user-library-read", 'playlist-modify', 'user-read-private','user-top-read','user-read-recently-played','user-read-currently-playing'])
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope=["user-library-read", 'playlist-modify', 'user-read-private','user-top-read','user-read-recently-played','user-read-currently-playing'])

# Create spotify object
spotifyObject = spotipy.Spotify(auth = token)

user = spotifyObject.current_user()

displayName = user['display_name']
followers = user['followers']['total']


###################################################################################################

#Menu

GUI = tkinter.Tk()
GUI.title('spotify helper')
GUI.geometry('300x400')

top_frame = tkinter.Frame(GUI).pack()
bottom_frame = tkinter.Frame(GUI).pack(side='bottom')




def clear_menu():
    pass


def currently_playing():
    clear_menu()
    currentlyPlaying = spotifyObject.currently_playing()['item']

    l1 = tkinter.Label(GUI,text='NAME: {}'.format(currentlyPlaying['name'])).pack()
    l2 = tkinter.Label(GUI,text='ARTIST: {}'.format(currentlyPlaying['artists'][0]['name'])).pack()
    l3 = tkinter.Label(GUI,text='ALBUM: {}'.format(currentlyPlaying['album']['name'])).pack()
    l4 = tkinter.Label(GUI,text='RELEASED: {}'.format(currentlyPlaying['album']['release_date'])).pack()
    l5 = tkinter.Label(GUI,text='EXPLICIT: {}'.format(currentlyPlaying['explicit'])).pack()
    l6 = tkinter.Label(GUI,text='ID: {}'.format(currentlyPlaying['id'])).pack()
    
def search_button_pressed():
    pass



def search_song():
    clear_menu()

    inpt1 = tkinter.Entry(GUI, width = 25)
    inpt1.grid(column=1,row=4)

    searchQuery = inpt1.get()

        
    selectedSong = 'MORE'
    limit = 5
    while selectedSong.upper() == 'MORE':
        for i in range(limit-5, limit):
            searchResults = spotifyObject.search(searchQuery, limit, 0, 'track')['tracks']['items']
            
            if searchResults[i]['explicit'] == True:
                EX = "[E]"    
            else:
                EX = ""

            num = i + 1
            print( '{}. {} by {} {}'.format(num,searchResults[i]['name'],searchResults[i]['artists'][0]['name'], EX) )
            print( '   ALBUM: {}'.format(searchResults[i]['album']['name']))
            print( '   RELEASED: {}'.format(searchResults[i]['album']['release_date']))
            print( '   ID: {}'.format(searchResults[i]['id']))
            print( )           
            print('\n')





while True:

    l1 = tkinter.Label(top_frame,text = 'Welcome to Spotify Helper ' + displayName + '!').pack()


    l2 = tkinter.Label(top_frame,text = 'You have ' + str(followers) + ' followers.').pack()

    bt1 = tkinter.Button(top_frame,text = '1 - Currently Playing',command=currently_playing).pack()

    search_bar = tkinter.Entry(top_frame,width = 25).pack()



    search_button = tkinter.Button(top_frame, text = 'Search', command = search_button_pressed).pack()

    bt5 = tkinter.Button(bottom_frame,text = '5 - List Favorite Songs').pack()

    bt6 = tkinter.Button(bottom_frame,text = '6 - List Favorite Artists').pack()

    bt7 = tkinter.Button(bottom_frame,text = '7 - Create a Playlist with Selected Artists').pack()

    bt8 = tkinter.Button(bottom_frame,text = '8 - Create a Playlist from Favorite Songs').pack()

    bt9 = tkinter.Button(bottom_frame,text = '9 - Combine a List of Playlists').pack()

    bt10 = tkinter.Button(bottom_frame,text = "Copy another user's Playlist (COMING SOON)").pack()

    bt11 = tkinter.Button(bottom_frame,text = '0 - Exit').pack()

    

###################################################################################################
    
    #format


    choice=input()
###################################################################################################

    #Search for a song





###################################################################################################

    #Search for the artist

    if choice == '3':
        searchQuery = input("What artist are you looking for?: ")

        searchResults = spotifyObject.search(searchQuery, 1, 0, 'artist')
        artist = searchResults['artists']['items'][0]

        print( '\n')
        print( 'NAME: {}'.format(artist['name']) )
        print( 'GENRES: {}'.format(artist['genres']) )
        print( 'ID: {}'.format(artist['id']))
        print()
        print('TOP 10 SONGS:')
        for i in range(len(spotifyObject.artist_top_tracks(artist['id'])['tracks'])):
            print( spotifyObject.artist_top_tracks(artist['id'])['tracks'][i]['name'])

        print('\nRELATED ARTISTS:')
        for i in range(5):
            print(spotifyObject.artist_related_artists(artist['id'])['artists'][i]['name'])


###################################################################################################
    
    #Search for album

    if choice == '4':
        searchQuery = input("What album are you looking for?: ")

        searchResults = spotifyObject.search(searchQuery, 1, 0, 'album')
        album = searchResults['albums']['items'][0]

        print( '\n')
        print( 'NAME: {}'.format(album['name']) )
        print( 'ARTIST: {}'.format(album['artists'][0]['name']) )
        print( 'RELEASED: {}'.format(album['release_date']))
        print( 'TYPE: {}'.format(album['type']))
        print( 'ID: {}'.format(album['id']))
        print( )
        print( 'SONGS:')
        for i in range(len(spotifyObject.album_tracks(album['id'])['items'])):
            num = i + 1
            print('{}. {}'.format(num,spotifyObject.album_tracks(album['id'])['items'][i]['name']))


###################################################################################################

    #Display top songs

    if choice == '5':
        limit = int(input("How many songs would you like to show? (50 max):\n\n>"))
        print()

        if limit > 50:
            limit = 50
        
        for i in range(limit):
            num = i + 1
            print('{}. {} by {}'.format(num,spotifyObject.current_user_top_tracks(limit)['items'][i]['name'], spotifyObject.current_user_top_tracks(limit)['items'][i]['artists'][0]['name']) )


###################################################################################################

    #Display top artists

    if choice == '6':
        limit = int(input("How many artists would you like to show? (50 max):\n\n>"))
        print()
        
        if limit > 50:
            limit = 50

        for i in range(limit):
            num = i + 1
            print('{}. {}'.format(num,spotifyObject.current_user_top_artists(limit)['items'][i]['name']) )


###################################################################################################

    #Create playlist with inputted artists

    if choice == '7':
        #get input from user
        rawInput = input('Enter a list of artists separated by commas: ')


        Input = rawInput.split(',')     #list of inputted artist names
        inputID = []     #list of inputted artists' IDs
        songs = []     #list of inputted artists' top 10 songs


        #create list of inputted artists' IDs
        for artist in Input:
            inputID.append( spotifyObject.search(artist,1,0,'artist')['artists']['items'][0]['id'] )


        #create a list of inputted artists' top 10 songs
        for ID in inputID:
            for i in range( len( spotifyObject.artist_top_tracks(spotifyObject.artist(ID)['id'])['tracks'] ) ):
              songs.append( spotifyObject.artist_top_tracks(spotifyObject.artist(ID)['id'])['tracks'][i]['id'] )


        #create playlist
        spotifyObject.user_playlist_create(user['id'],rawInput)

        #find created playlist and assign to plylst
        for i in range(len(spotifyObject.current_user_playlists()['items'])):
            if spotifyObject.current_user_playlists()['items'][i]['name'] == rawInput:
                plylst = spotifyObject.current_user_playlists()['items'][i]
                break

        #add songs to playlist
        spotifyObject.playlist_add_items(plylst['id'],songs)

        in2 = input('\n\nYour playlist has been created!\n\nWould you like to listen now? (Y/N):')

        if in2.upper() == 'Y':
            spotifyObject.start_playback(None,plylst['uri'])
            spotifyObject.shuffle(True)


###################################################################################################

    #create playlist from top songs
    if choice == '8':
        limit = int(input("How many songs would you like to add? (50 max): "))
        print()

        if limit > 50:
            limit = 50

        playlistName = input('What would you like to call your playlist?\n\n>')

        favoriteSongIDs = []
        for i in range(limit):
            favoriteSongIDs.append( spotifyObject.current_user_top_tracks(limit)['items'][i]['id'] )
        
        spotifyObject.user_playlist_create(user['id'],playlistName)

        #find created playlist and assign to plylst
        for i in range(len(spotifyObject.current_user_playlists()['items'])):
            if spotifyObject.current_user_playlists()['items'][i]['name'] == playlistName:
                favoritesPlaylist = spotifyObject.current_user_playlists()['items'][i]
                break

        #add songs to playlist
        spotifyObject.playlist_add_items(favoritesPlaylist['id'],favoriteSongIDs)

        in2 = input('\n\nYour playlist has been created!\n\nWould you like to listen now? (Y/N):')

        if in2.upper() == 'Y':
            spotifyObject.start_playback(None,favoritesPlaylist['uri'])
            spotifyObject.shuffle(True)
            

###################################################################################################

    #formatting

    print('\n')
    print('-'*75)
    quit = input('Press "Enter" to return to the menu or enter "Q" to quit.\n')
    
    if quit.upper() == 'Q':
        break