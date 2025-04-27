def run(spotify):
    playlists = spotify.current_user_playlists()["items"]
    print("\nYour Playlists:\n----------------")
    for i, p in enumerate(playlists):
        print(f"{i+1:2}. {p['name']}")
    idx = int(input("Enter playlist number: ")) - 1
    playlist_id = playlists[idx]["id"]
    song_ids = input("Enter song IDs (comma-separated): ").split(",")
    spotify.playlist_add_items(playlist_id, [s.strip() for s in song_ids])
    print("\n[*] Songs successfully added to playlist.")
