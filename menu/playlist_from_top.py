def run(spotify, user):
    def end_program():
        print("\n----------------------------------------------")
        print("[Enter] Return to Menu")
        input("» ")

    limit_input = input("How many top songs? (max 50):\n» ").strip()
    if not limit_input:
        print("\n[!] Canceled.")
        end_program()
        return

    try:
        limit = int(limit_input)
    except ValueError:
        print("\n[!] Invalid number.")
        end_program()
        return

    if limit > 50:
        print("\n[*] -_- Nice Try.")
        limit = 50

    playlist_name = input("\nPlaylist name:\n» ").strip()
    if not playlist_name:
        print("\n[!] Canceled.")
        end_program()
        return

    songs = spotify.current_user_top_tracks(limit)["items"]
    song_ids = [song["id"] for song in songs]
    song_info = [f"{song['name']} by {song['artists'][0]['name']}" for song in songs]

    print("\nSongs to be added:")
    print("------------------")
    for i, song in enumerate(song_info, start=1):
        print(f"{i:2}. {song}")

    confirm = input("\nCreate playlist with these songs? (y/n): ").strip().lower()
    if confirm != "y":
        print("\n[!] Canceled.")
        end_program()
        return

    playlist = spotify.user_playlist_create(user["id"], playlist_name)
    spotify.playlist_add_items(playlist["id"], song_ids)
    print("\n[*] Playlist created from your top songs.")
    end_program()
