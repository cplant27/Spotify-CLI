# Spotify Helper

A streamlined Python application that provides a command-line interface to your Spotify account, allowing you to manage your music, create playlists, and more.

## Features

- View currently playing track
- Search for songs, artists, and albums
- View your top songs and artists
- Create playlists based on your favorite artists
- Generate playlists from your top tracks
- Check for new music from your followed artists
- Add songs to your playlists

## Requirements

- Python 3.6+
- Spotify Premium account
- Spotify Developer credentials

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/cplant27/spotify-helper.git
   cd spotify-helper
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Set up your Spotify API credentials as environment variables:

   ```
   # Windows
   set SPOTIPY_CLIENT_ID=your_client_id
   set SPOTIPY_CLIENT_SECRET=your_client_secret
   set SPOTIPY_REDIRECT_URI=http://localhost:8888/callback

   # Mac/Linux
   export SPOTIPY_CLIENT_ID=your_client_id
   export SPOTIPY_CLIENT_SECRET=your_client_secret
   export SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
   ```

## Usage

Run the application:

```
python main.py
```

Follow the on-screen menu to navigate through the different features.

## Project Structure

```
spotify-helper/
│
├── main.py               # Main application entry point
├── auth.py               # Spotify authentication
├── menu/                 # Menu modules
│   ├── __init__.py
│   ├── add_to_playlist.py
│   ├── check_new_music.py
│   ├── currently_playing.py
│   ├── playlist_from_artists.py
│   ├── playlist_from_top.py
│   ├── search.py
│   ├── top_artists.py
│   └── top_songs.py
│
└── src/                  # Additional source files
    ├── playlist_creator.py
    └── ui.py
```

## Acknowledgements

- [Spotipy](https://spotipy.readthedocs.io/) - Lightweight Python library for the Spotify API
