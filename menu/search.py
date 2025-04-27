def run(spotify):
    def prompt_continue():
        return (
            input(
                "\n[Enter # to view | press Enter to go back | type 'more' for more results]\n» "
            )
            .strip()
            .lower()
        )

    def end_program():
        print("\n----------------------------------------------")
        print("[Enter] Return to Menu")
        input("» ")

    def show_artist_details(artist_id):
        print("\nTop Songs:")
        top_tracks = spotify.artist_top_tracks(artist_id)["tracks"]
        for track in top_tracks[:5]:
            print(f"- {track['name']}")

        print("\nRecent Releases:")
        albums = spotify.artist_albums(artist_id, album_type="album,single")["items"]
        seen = set()
        for album in albums:
            if album["name"] not in seen:
                print(f"- {album['name']}")
                seen.add(album["name"])
            if len(seen) == 5:
                break

        print(f"\nArtist ID: {artist_id}")

    def show_track_details(track):
        print(f"\nTrack: {track['name']}")
        print(f"Artist: {track['artists'][0]['name']}")
        print(f"ID: {track['id']}")
        print("\nRelated Tracks:")

    try:
        recs = spotify.recommendations(
            seed_tracks=[track["id"]], limit=10, market="US"
        )["tracks"]

        if not recs:
            print("[!] No related tracks found.")
            return
        for rec in recs:
            print(f"- {rec['name']} by {rec['artists'][0]['name']}")
    except Exception as e:
        print("[!] Could not fetch related tracks.")

    def show_album_details(album_id):
        album = spotify.album(album_id)
        print(f"\nAlbum: {album['name']}")
        print(f"Artist: {album['artists'][0]['name']}")
        print("\nTracklist:")
        for track in album["tracks"]["items"]:
            print(f"- {track['name']}")

    print("What would you like to search?")
    print("1. Track")
    print("2. Album")
    print("3. Artist")

    choice_map = {
        "1": ("track", "Track"),
        "track": ("track", "Track"),
        "2": ("album", "Album"),
        "album": ("album", "Album"),
        "3": ("artist", "Artist"),
        "artist": ("artist", "Artist"),
    }

    choice_input = input("» ").strip()
    selection = choice_map.get(choice_input)
    if not selection:
        print("\n[!] Invalid choice.")
        end_program()
        return

    search_type, display_type = selection
    query = input(f"\nEnter {search_type} name:\n» ").strip()
    if not query:
        print("\n[!] Canceled.")
        end_program()
        return

    offset = 0
    limit = 5 if search_type == "artist" else 10

    while True:
        try:
            results = spotify.search(
                query, limit=limit, offset=offset, type=search_type
            )[f"{search_type}s"]["items"]
        except Exception as e:
            print(f"[!] Search failed: {e}")
            end_program()
            return

        if not results:
            print("[!] No results found.")
            end_program()
            return

        print(f"\n{display_type} Results:")
        print("--------------------")
        for i, item in enumerate(results, start=offset + 1):
            if search_type == "track":
                ex = " [E]" if item["explicit"] else ""
                print(f"{i:2}. {item['name']} by {item['artists'][0]['name']}{ex}")
            elif search_type == "artist":
                genres = ", ".join(item["genres"]) if item["genres"] else "N/A"
                print(f"{i:2}. {item['name']} (Genres: {genres})")
            elif search_type == "album":
                print(f"{i:2}. {item['name']} by {item['artists'][0]['name']}")

        user_input = prompt_continue()

        if user_input == "":
            print("\n[*] Returning to menu.")
            return
        elif user_input == "more":
            offset += limit
        elif user_input.isdigit():
            index = int(user_input) - 1
            if 0 <= index - offset < len(results):
                item = results[index - offset]
                if search_type == "track":
                    show_track_details(item)
                elif search_type == "artist":
                    show_artist_details(item["id"])
                elif search_type == "album":
                    show_album_details(item["id"])
                print("\n----------------------------------------------")
                print("[Enter] Return to Search")
                input("» ")
            else:
                print("[!] Invalid selection.")
        else:
            print("\n[!] Invalid input.")
