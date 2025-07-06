from flask import Flask, render_template, redirect, session, url_for, request
import os
from dotenv import load_dotenv
from spotify import *


# This project was developed with guidance from OpenAI's ChatGPT, which assisted
# in planning, designing, and implementing features including:
# - Formatting and simplification of the code structure of the spotify Auth
# - Secure access/refresh token management
# - Help in the planning for a roadmap of the project
# - Acceleration in the design of the frontend through the use of Tailwind CSS
# - Implementation of charting features using Chart.js
# - Cleaning up the code structure and enhancing error handling

# That respective code was duly understood, implemented, and customized by me.


load_dotenv()

# Spotify API credentials
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Load environment variables from .env file
load_dotenv()

@app.route('/')
def index():
    access_token = session.get("access_token")
    if access_token:
        return redirect("/dashboard")

    return render_template('index.html')

@app.route('/login')
def login():
    # Redirect to Spotify's authorization page
    auth_url = get_auth_url(SPOTIFY_CLIENT_ID, url_for('callback', _external=True))
    return redirect(auth_url)

@app.route('/logout')
def logout():
    # Clear the session and redirect to the index page
    session.clear()
    return redirect("/")

@app.route('/callback')
def callback():
    code = request.args.get("code")
    
    token_data = exchange_code_for_token(
        code, 
        SPOTIFY_CLIENT_ID, 
        SPOTIFY_CLIENT_SECRET, 
        url_for('callback', _external=True)
    )

    session["access_token"] = token_data.get("access_token")
    session["refresh_token"] = token_data.get("refresh_token")

    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    access_token = session.get("access_token")
    if not access_token:
        return redirect("/")

    user_data = get_user_profile(access_token)
    

    if not user_data:
        # Try to refresh the access token
        refresh_token = session.get("refresh_token")
        if refresh_token:
            try:
                new_token_data = refresh_access_token(refresh_token, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
                
                # Check if refresh was successful
                if new_token_data.get("access_token"):
                    session["access_token"] = new_token_data.get("access_token")
                    # Update refresh token if a new one is provided
                    if new_token_data.get("refresh_token"):
                        session["refresh_token"] = new_token_data.get("refresh_token")
                    return redirect("/dashboard")
                else:
                    # Refresh failed, redirect to login
                    session.clear()
                    return redirect("/")
            except Exception as e:
                # Error during refresh, clear session and redirect to login
                session.clear()
                return redirect("/")
        else:
            # No refresh token available, redirect to login
            session.clear()
            return redirect("/")
        
    top_artists = get_top_artists(access_token, time_range='medium_term', limit=3)

    top_genres = get_top_genres(access_token, limit=10, time_range='medium_term', genre_limit=6)

    top_tracks = get_top_tracks(access_token, time_range='medium_term', limit=5)

    return render_template("dashboard.html", user=user_data, top_artists=top_artists, top_genres=top_genres, top_tracks=top_tracks)


if __name__ == '__main__':
    app.run(debug=True)
