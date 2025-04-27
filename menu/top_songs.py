def run(spotify):
    def end_program():
        print("\n----------------------------------------------")
        print("[Enter] Return to Menu")
        input("» ")

    limit_input = input("How many songs? (max 50):\n» ").strip()
    if not limit_input:
        print("\n[!] Canceled.")
        end_program()
        return

    if not limit_input.isdigit():
        print("\n[!] Invalid number.")
        end_program()
        return

    limit = int(limit_input)
    if limit <= 0:
        print("\n[!] Number must be greater than 0.")
        end_program()
        return
    if limit > 50:
        print("\n[*] -_- Nice Try. Showing top 50 songs.")
        limit = 50

    songs = spotify.current_user_top_tracks(limit)["items"]
    print("\nTop Songs:\n-----------")
    for i, song in enumerate(songs):
        print(f"{i+1:2}. {song['name']} by {song['artists'][0]['name']}")

    end_program()
