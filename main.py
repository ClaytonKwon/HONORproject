import requests
import base64
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify tokens
id = '17e466af805745bf8a92dda2b32555c3'
secret = '61bec1966e0c4719aba667b20ca39ade'
redirect = 'http://127.0.0.1:5000/'

# Getting my access token
auth_header = base64.b64encode(f"{id}:{secret}".encode('utf-8')).decode('utf-8')

auth = requests.post("https://accounts.spotify.com/api/token", 
                     headers={"Authorization": f"Basic {auth_header}"},
                     data={"grant_type": "client_credentials"})
token = auth.json()['access_token']

# OAuth code
sp_oauth = SpotifyOAuth(client_id = id,
                        client_secret = secret,
                        redirect_uri = redirect,
                        scope='user-read-recently-played')

# made api
sp = spotipy.Spotify(auth_manager=sp_oauth)

# Get recent played tracks
try:
    results = sp.current_user_recently_played()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(f"{idx}: {track['artists'][0]['name']} – {track['name']}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# retrieve artist info
headers = {"Authorization": f"Bearer {token}"}
artist_name = "Taylor Swift"
response = requests.get(f"https://api.spotify.com/v1/search?q={artist_name}&type=artist", headers=headers)
artist_info = response.json()

# print info abt "The Weeknd"
try:
    artists = artist_info['artists']['items']
    for artist in artists:
        if artist['name'].lower() == artist_name.lower():
            print(f"Name: {artist['name']}")
            print(f"Genres: {', '.join(artist['genres'])}")
            print(f"Spotify URI: {artist['uri']}")
except KeyError:
    print("No artist information found.")
