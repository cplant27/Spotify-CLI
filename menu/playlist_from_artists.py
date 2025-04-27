# menu/playlist_from_artists.py
def run(spotify, user):
    raw_input = input("Enter artists separated by commas:\n» ")
    if not raw_input.strip():
        print("\n[!] Canceled.")
        return

    artist_names = raw_input.split(",")
    song_ids = []
    song_info = []

    for name in artist_names:
        artist_id = spotify.search(name.strip(), 1, 0, "artist")["artists"]["items"][0][
            "id"
        ]
        top_tracks = spotify.artist_top_tracks(artist_id)["tracks"]
        for track in top_tracks:
            song_ids.append(track["id"])
            song_info.append(f"{track['name']} by {track['artists'][0]['name']}")

    print("\nSongs to be added:")
    print("------------------")
    for i, song in enumerate(song_info, start=1):
        print(f"{i:2}. {song}")

    confirm = input("\nCreate playlist with these songs? (y/n): ").strip().lower()
    if confirm != "y":
        print("\n[!] Canceled.")
        return

    playlist = spotify.user_playlist_create(user["id"], raw_input.upper())
    spotify.playlist_add_items(playlist["id"], song_ids)
    print("\n[*] Playlist created successfully.")
