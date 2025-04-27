"""
Authentication module for Spotify API interactions.

This module handles authentication with the Spotify Web API
using the Spotipy library. It manages user tokens and provides
authenticated Spotify API client objects.
"""

import os

import spotipy
import spotipy.util as util


def get_spotify_object():
    """
    Authenticate with Spotify API and return a Spotify client object.

    Uses environment variables for authentication credentials:
    - SPOTIPY_CLIENT_ID
    - SPOTIPY_CLIENT_SECRET
    - SPOTIPY_REDIRECT_URI

    Returns:
        tuple: (spotify_object, user_data)
            - spotify_object: Authenticated Spotipy client instance
            - user_data: Dictionary containing user profile information
    """
    username = os.getlogin()
    scope = [
        "user-library-read",
        "playlist-modify-public",
        "playlist-modify-private",
        "user-read-private",
        "user-top-read",
        "user-read-recently-played",
        "user-read-currently-playing",
        "user-follow-read",
    ]
    try:
        token = util.prompt_for_user_token(username, scope=scope)
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope=scope)
    spotify = spotipy.Spotify(auth=token)
    user = spotify.current_user()
    return spotify, user
