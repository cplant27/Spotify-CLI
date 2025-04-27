from auth import get_spotify_object
from menu import (
    add_to_playlist,
    check_new_music,
    currently_playing,
    playlist_from_artists,
    playlist_from_top,
    search,
    top_artists,
    top_songs,
)


def print_menu():
    print("\n==============================================")
    print("|          SPOTIFY TERMINAL INTERFACE         |")
    print("==============================================")
    print("| 1 | Currently Playing                       |")
    print("| 2 | Search                                  |")
    print("| 3 | List Favorite Songs                     |")
    print("| 4 | List Favorite Artists                   |")
    print("| 5 | Create Playlist from Artists            |")
    print("| 6 | Create Playlist from Favorite Songs     |")
    print("| 7 | Check for New Music                     |")
    print("| 8 | Add Song to Playlist                    |")
    print("|   |                                         |")
    print("| Q | Quit                                    |")
    print("==============================================")


spotifyObject, user = get_spotify_object()

while True:
    print("\n" * 50)

    print_menu()
    choice = input("Select an option: ").strip().upper()

    print("\n" * 50)
    print("----------------------------------------------\n")

    if choice == "Q":
        print("Goodbye!")
        break
    elif choice == "1":
        currently_playing.run(spotifyObject)
    elif choice == "2":
        search.run(spotifyObject)
    elif choice == "3":
        top_songs.run(spotifyObject)
    elif choice == "4":
        top_artists.run(spotifyObject)
    elif choice == "5":
        playlist_from_artists.run(spotifyObject, user)
    elif choice == "6":
        playlist_from_top.run(spotifyObject, user)
    elif choice == "7":
        check_new_music.run(spotifyObject)
    elif choice == "8":
        add_to_playlist.run(spotifyObject)
    else:
        print("[!] Invalid Input.")
