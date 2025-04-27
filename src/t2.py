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
    token = util.prompt_for_user_token(username, scope=[
        "user-library-read", 
        'playlist-modify', 
        'user-read-private',
        'user-top-read',
        'user-read-recently-played',
        'user-read-currently-playing',
        'user-follow-read'
    ])
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope=[
        "user-library-read", 
        'playlist-modify', 
        'user-read-private',
        'user-top-read',
        'user-read-recently-played',
        'user-read-currently-playing',
        'user-follow-read'
        ])

# Create spotify object
spotifyObject = spotipy.Spotify(auth = token)

user = spotifyObject.current_user()

displayName = user['display_name']
followers = user['followers']['total']


###################################################################################################

#Menu

# combine playlists
# add songs to a playlist
# create playlist
# copy another user's playlist
# error handling

while True:

    print()
    print('>>> Welcome to Spotifyxx.py ' + displayName + '!')
    print('You have ' + str(followers) + ' followers.')
    print()
    print('1 - Currently Playing')
    print('2 - Search')
    print('3 - List Favorite Songs')
    print('4 - List Favorite Artists')
    print('5 - Create a Playlist with Selected Artists')
    print('6 - Create a Playlist from Favorite Songs')
    print('7 - Check for New Music (WIP)')
    print('8 - Add a Song to a Playlist')
    print()
    print('Q - Quit')
    print()
    menu_choice = input('Your choice: ')


###################################################################################################
    
    #End program or format
    
    if menu_choice.upper() == 'Q':
        break
    
    print('\n')
    print('-'*75)
    print('\n')


###################################################################################################

    #Give info about currently playing song
    
    if menu_choice == '1':
        
        try:
            currentlyPlaying = spotifyObject.currently_playing()['item']

            print( 'NAME: {}'.format(currentlyPlaying['name']))
            print( 'ARTIST: {}'.format(currentlyPlaying['artists'][0]['name']))
            print( 'ALBUM: {}'.format(currentlyPlaying['album']['name']))
            print( 'RELEASED: {}'.format(currentlyPlaying['album']['release_date']))
            print( 'EXPLICIT: {}'.format(currentlyPlaying['explicit']))
            print( 'ID: {}'.format(currentlyPlaying['id']))
        
        except:
            print("There is no song currently playing.")


###################################################################################################

    #Search

    elif menu_choice == '2':

        search_choice = input('Are you looking for a song, album, or artist?: ')
        

        if search_choice.upper() == 'SONG':
        
            searchQuery = input("\n\nWhat song are you looking for?: ")
            print('\n')

        
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
                selectedSong = input('Enter "more" to show more results or press "Enter" to quit the search: ')
                print('\n')

                if selectedSong.upper() == 'MORE':
                    limit += 5
                    if limit > 50:
                        limit = 50
            
                else: 
                    break


        
        if search_choice.upper() == 'ARTIST':
            searchQuery = input("\n\nWhat artist are you looking for?: ")

            searchResults = spotifyObject.search(searchQuery, 1, 0, 'artist')
            artist = searchResults['artists']['items'][0]

            print( '\n')
            print( 'NAME: {}'.format(artist['name']) )
            print( 'GENRES: {}'.format(artist['genres']) )
            print( 'ID: {}'.format(artist['id']))
            print()
            print('TOP 10 SONGS:')
        
            top10_TEMP = spotifyObject.artist_top_tracks(artist['id'])['tracks']
            for i in range(len(top10_TEMP)):
                print( top10_TEMP[i]['name'])

            related_artists_TEMP = spotifyObject.artist_related_artists(artist['id'])['artists']
            print('\nRELATED ARTISTS:')
            for i in range(5):
                print(related_artists_TEMP[i]['name'])

        

        if search_choice.upper() == 'ALBUM':
            searchQuery = input("\n\nWhat album are you looking for?: ")

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

            album_tracks_TEMP = spotifyObject.album_tracks(album['id'])['items']
            for i in range(len(album_tracks_TEMP)):
                num = i + 1
                print('{}. {}'.format(num,album_tracks_TEMP[i]['name']))


###################################################################################################

    #Display top songs

    elif menu_choice == '3':
        limit = int(input("How many songs would you like to show? (50 max):\n\n>"))
        print()

        if limit > 50:
            limit = 50

        top_songs = spotifyObject.current_user_top_tracks(limit)['items']
        
        for i in range(limit):
            num = i + 1
            print('{}. {} by {}'.format(num,top_songs[i]['name'], top_songs[i]['artists'][0]['name']) )


###################################################################################################

    #Display top artists

    elif menu_choice == '4':
        limit = int(input("How many artists would you like to show? (50 max):\n\n>"))
        print()
        
        if limit > 50:
            limit = 50

        top_artists = spotifyObject.current_user_top_artists(limit)['items']

        for i in range(limit):
            num = i + 1
            print('{}. {}'.format(num,top_artists[i]['name']) )


###################################################################################################

    #Create playlist with inputted artists

    elif menu_choice == '5':
        #get input from user
        rawInput = input('Enter a list of artists separated by commas: ')


        Input = rawInput.split(',')     #list of inputted artist names
        inputID = []     #list of inputted artists' IDs
        songs = []     #list of inputted artists' top 10 songs

        print('\none moment...\n\n')


        #print('creating list of inputted artists IDs...'.upper())
        for artist in Input:
            inputID.append( spotifyObject.search(artist,1,0,'artist')['artists']['items'][0]['id'] )


        #print('creating list of inputted artists top 10 songs...'.upper())
        for ID in inputID:
            artist_top10_TEMP = spotifyObject.artist_top_tracks(spotifyObject.artist(ID)['id'])['tracks']
            for i in range( len( artist_top10_TEMP ) ):
              songs.append( artist_top10_TEMP[i]['id'] )


        #print('creating playlist...'.upper())
        spotifyObject.user_playlist_create(user['id'],rawInput.upper())

        #print('locating created playlist...'.upper())
        for i in range(len(spotifyObject.current_user_playlists()['items'])):
            
            user_playlists = spotifyObject.current_user_playlists()['items']
            if user_playlists[i]['name'] == rawInput.upper():
                plylst = user_playlists[i]
                break

        #print('adding songs to playlist...'.upper())
        spotifyObject.playlist_add_items(plylst['id'],songs)

        in2 = input('\n\nYour playlist has been created!\n\nWould you like to listen now? (Y/N):')

        if in2.upper() == 'Y':
            spotifyObject.start_playback(None,plylst['uri'])
            spotifyObject.shuffle(True)


###################################################################################################

    #create playlist from top songs
    elif menu_choice == '6':
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
    
    #search new music friday

    # find a way to check features
    # fix index 40 error
    
    elif menu_choice == '7':
        followed_artists_RAW = spotifyObject.current_user_followed_artists(limit = 50)['artists']['items']
        followed_artists = []

        for i in range(len(followed_artists_RAW)):
            followed_artists.append(followed_artists_RAW[i]['id'])

        new_music_friday = spotifyObject.playlist('37i9dQZF1DX4JAvHpjipBk')['tracks']['items']
        ifnone = 0

        for i in range(len(new_music_friday)):
            print(i)
            ifnone += 1
            if new_music_friday[i]['track']['artists'][0]['id'] in followed_artists:
                ifnone += 1
                print( '   {} by {}'.format(new_music_friday[i]['track']['name'],new_music_friday[i]['track']['artists'][0]['name']) )
                print( '   ALBUM: {}'.format(new_music_friday[i]['track']['album']['name']))
                print( '   ID: {}'.format(new_music_friday[i]['track']['id']))
                print( )   

        if ifnone == 0:
            print('No new music was found for any of your followed artists.')

    elif menu_choice == 'test':
        for i in range(len(spotifyObject.playlist('37i9dQZF1DX4JAvHpjipBk')['tracks']['items'])):
            print(spotifyObject.playlist('37i9dQZF1DX4JAvHpjipBk')['tracks']['items'][i])
            print(i)

    elif menu_choice == 'test2':
        print(spotifyObject.artist_albums('5K4W6rqBFWDnAN6FQUkS6x')['items'][0]['name'])

###################################################################################################

    #add a song to a playlist

    elif menu_choice == '8':

        user_playlists_RAW = spotifyObject.current_user_playlists()['items']
        user_playlists_ids_LIST = []

        for i in range(len(user_playlists_RAW)):
            user_playlists_ids_LIST.append(user_playlists_RAW[i]['id'])
            print("{}. {}".format(i+1, user_playlists_RAW[i]['name']))

        playlist_selection = input("\n\nEnter the Number of the Playlist: ")
        playlist_selection = int(playlist_selection) + 1

        add2playlist_id = user_playlists_ids_LIST[playlist_selection]

        songs_to_add = input('\nEnter the IDs of the songs you would like to add separated by commas: ')
        songs_to_add = songs_to_add.split()
        spotifyObject.playlist_add_items(add2playlist_id,songs_to_add)

        print("\n\nDone.")


###################################################################################################

    else:
        print('Invalid Input. Try Again.')

    #formatting

    print('\n')
    print('-'*75)
    quit = input('Press "Enter" to return to the main menu\n')
    
    if quit.upper() == 'Q':
        break