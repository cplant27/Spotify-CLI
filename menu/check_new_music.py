from datetime import datetime, timedelta


def run(spotify):
    print(
        "\nNew Releases from Your Top Artists (Last 30 Days):\n---------------------------------------------------"
    )
    top_artists = spotify.current_user_top_artists(limit=25)["items"]
    now = datetime.now()
    one_month_ago = now - timedelta(days=30)
    found_any = False
    song_uris = []
    releases = []

    def time_ago(date):
        delta = now - date
        days = delta.days
        if days < 1:
            return "Today"
        elif days == 1:
            return "1 day ago"
        elif days < 7:
            return f"{days} days ago"
        elif days < 30:
            weeks = days // 7
            return f"{weeks} week{'s' if weeks > 1 else ''} ago"
        else:
            return "Over a month ago"

    for artist in top_artists:
        artist_name = artist["name"][:20].ljust(20)
        artist_id = artist["id"]
        albums = spotify.artist_albums(artist_id, album_type="album,single")["items"]

        for album in albums:
            release_date = album["release_date"]
            precision = album["release_date_precision"]
            album_type = album["album_type"].capitalize()
            album_name = album["name"][:35]

            try:
                if precision == "day":
                    release_datetime = datetime.strptime(release_date, "%Y-%m-%d")
                elif precision == "month":
                    release_datetime = datetime.strptime(release_date, "%Y-%m")
                else:
                    continue

                if release_datetime >= one_month_ago:
                    releases.append(
                        {
                            "artist": artist_name,
                            "type": album_type,
                            "name": album_name,
                            "date": release_datetime,
                            "album_id": album["id"],
                        }
                    )
                    found_any = True
            except:
                continue

    if not found_any:
        print("[!] No recent releases found.")
    else:
        releases.sort(key=lambda x: x["date"])  # sort by date
        for r in releases:
            print(
                f"{r['artist']} | {r['type']:<7} | {r['name']} ({time_ago(r['date'])})"
            )
            tracks = spotify.album_tracks(r["album_id"])["items"]
            for track in tracks:
                song_uris.append(track["uri"])

        print("\n----------------------------------------------")
        make_playlist = (
            input("\nWould you like to create a playlist of these songs? (y/n): ")
            .strip()
            .lower()
        )
        if make_playlist == "y":
            playlist_name = f"New Songs - {now.strftime('%b %d, %Y')}"
            user_id = spotify.current_user()["id"]
            playlist = spotify.user_playlist_create(
                user_id, playlist_name, public=False
            )
            spotify.playlist_add_items(playlist["id"], song_uris)
            print(
                f"\n[*] Playlist '{playlist_name}' created with {len(song_uris)} songs."
            )
