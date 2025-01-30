import requests
import json

# Base URL for the Last.fm API
lastfm_service = 'http://ws.audioscrobbler.com/2.0'

# Last.fm API key
API_KEY = '4f047a94b06c296c789f9571bd6e065f'

# Function to get top tracks for an artist from Last.fm and save to a JSON file
def get_and_save_lastfm_tracks(artist_name):
    # URL for making a request to the Last.fm API to retrieve top tracks data by a given artist.
    url = f'{lastfm_service}/?method=artist.gettoptracks&artist={artist_name}&api_key={API_KEY}&format=json'
    response = requests.get(url)
    data = response.json()
    file_name = f'resources/{artist_name}_lastfm_tracks.json'

    # Check for the existence of key 'toptracks' in data and key 'track' in data['toptracks']
    if data.get('toptracks') and data['toptracks'].get('track'):

        # Write and save data from the "track" key to a JSON formatted file
        with open(file_name, "w") as lastfm_file:
            json.dump(data['toptracks']['track'],lastfm_file, indent=4)

        print(f'Last.fm data saved to {file_name}')
    else:
        print('No data on Last.fm.')