import base64
import requests
from urllib.parse import urlencode
import os
from collections import Counter

# Spotify API URLs and configuration
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_SCOPE = 'user-top-read user-read-private user-read-email'

def get_auth_url(client_id, redirect_uri):
    """Generate Spotify authorization URL"""

    auth_query = {
        'response_type': 'code',
        'client_id': client_id,
        'scope': SPOTIFY_SCOPE,
        'redirect_uri': redirect_uri,
        'show_dialog': 'true'
    }
    return f"{SPOTIFY_AUTH_URL}?{urlencode(auth_query)}"

def exchange_code_for_token(code, client_id, client_secret, redirect_uri):
    """Exchange authorization code for access token"""
    auth_str = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }

    response = requests.post(SPOTIFY_TOKEN_URL, headers=headers, data=data)
    return response.json()

def get_user_profile(access_token):
    """Get user profile information from Spotify API"""

    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get("https://api.spotify.com/v1/me", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def refresh_access_token(refresh_token, client_id, client_secret):
    """Refresh access token using refresh token"""
    if not refresh_token:
        return None
        
    auth_str = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }

    try:
        response = requests.post(SPOTIFY_TOKEN_URL, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        return None
    

def get_top_artists(access_token, time_range='medium_term', limit=3):
    """Get user's top artists from Spotify API"""
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "limit": limit,
        "time_range": time_range
    }

    response = requests.get("https://api.spotify.com/v1/me/top/artists", headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        return None
    

def get_top_genres(access_token, limit=10, time_range='medium_term', genre_limit=6):
    
    """Get user's top genres from Spotify API"""

    top_artists = get_top_artists(access_token, time_range=time_range, limit=limit)
    if not top_artists:
        return None

    genre_counts = Counter()
    
    for artist in top_artists:
        genres = artist.get('genres', [])
        for genre in genres:
            genre_counts[genre] += 1

    most_common = genre_counts.most_common(genre_limit)
    if not most_common:
        return None

    return [(genre, count) for genre, count in most_common]


def get_top_tracks(access_token, time_range='medium_term', limit=5):
    """Get user's top tracks from Spotify API"""
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "limit": limit,
        "time_range": time_range
    }

    response = requests.get("https://api.spotify.com/v1/me/top/tracks", headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        return None
