def run(spotify):
    def end_program():
        print("\n----------------------------------------------")
        print("[Enter] Return to Menu")
        input("» ")

    limit_input = input("How many artists? (max 50):\n» ").strip()
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
        print("\n[*] -_- Nice Try. Showing top 50 artists.")
        limit = 50

    artists = spotify.current_user_top_artists(limit)["items"]
    print("\nTop Artists:\n-------------")
    for i, artist in enumerate(artists):
        print(f"{i+1:2}. {artist['name']}")

    end_program()
