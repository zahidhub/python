import requests
import json

# Application URL for the Spotify API
spotify_service = 'https://dit009-spotify-assignment.vercel.app/api/v1'

# Function to get tracks for an artist from Spotify and save to a JSON file
def get_and_save_spotify_tracks(artist_name):
    # URL for making a request to the Spotify API to search for tracks data by a given artist.
    url = f'{spotify_service}/search?q={artist_name}&type=track&market=US&limit=50&offset=0'
    response = requests.get(url)
    data = response.json()
    file_name = f'resources/{artist_name}_spotify_tracks.json'
    # Check for the existence of key 'tracks' in data and key 'items' in data['tracks']
    if data.get('tracks') and data['tracks'].get('items'):
        # Write and save data from the "items" key to a JSON formatted file
        with open(file_name, "w") as spotify_file:
            json.dump(data['tracks']['items'],spotify_file, indent=4)

        print(f'Spotify data saved to {file_name}')
    else:
        print('No data on Spotify.')