def run(spotify):
    try:
        track = spotify.currently_playing()["item"]
        print("NOW PLAYING")
        print("-----------")
        print(f"Name     : {track['name']}")
        print(f"Artist   : {track['artists'][0]['name']}")
        print(f"Album    : {track['album']['name']}")
        print(f"Released : {track['album']['release_date']}")
        print(f"Explicit : {track['explicit']}")
        print(f"Track ID : {track['id']}")
    except:
        print("[!] There is no song currently playing.")

    print("\n----------------------------------------------")
    print("[Enter] Return to Menu")
    input("» ")
