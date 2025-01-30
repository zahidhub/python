import spotify_api_miner
import lastfm_api_miner
import music_data_analyser
import os

def get_top_tracks():
    artist_name = get_artist_name()
    try:
        music_data_analyser.display_top_spotify_tracks(artist_name)
        music_data_analyser.display_top_lastfm_tracks(artist_name)
    except Exception:
        get_invalid_artist_text(artist_name)

def get_top_album():
    artist_name = get_artist_name()
    try:
        music_data_analyser.get_artist_top_albums(artist_name)
    except Exception:
        get_invalid_artist_text(artist_name)

def get_track_duration():
    artist_name = get_artist_name()
    try:
        music_data_analyser.get_track_duration(artist_name)
    except Exception:
        get_invalid_artist_text(artist_name)

def get_specific_year_tracks():
    artist_name = get_artist_name()
    try:
        music_data_analyser.get_tracks_of_particular_year(artist_name)
    except Exception:
        get_invalid_artist_text(artist_name)

def get_track_listeners():
    artist_name = get_artist_name()
    try:
        music_data_analyser.get_listener_count(artist_name)
    except Exception:
        get_invalid_artist_text(artist_name)

def retrieve_all_tracks():

    artist_name = input('\nEnter the name of an artist to retrieve all of their tracks: ').strip()
    file_name1 = f'resources/{artist_name}_spotify_tracks.json'
    file_name2 = f'resources/{artist_name}_lastfm_tracks.json'

    if os.path.exists(file_name1):
        print('"Artist already exists"')
        return
    if os.path.exists(file_name2):
        print('"Artist already exists"')
        return
    else:
        lastfm_api_miner.get_and_save_lastfm_tracks(artist_name)
        spotify_api_miner.get_and_save_spotify_tracks(artist_name)
        return artist_name

def plot_artist_popularity_overtime():
    artist_name = get_artist_name()
    music_data_analyser.plot_artist_popularity(artist_name)

def get_artist_name():
     return input('Enter the name of the artist: ').strip()

def get_invalid_artist_text(artist_name):
    return print(f'Artist \'{artist_name}\' not found. Please check the artist\'s name and try again.')

def main_menu():
    option = ''
    while option != '8':
        display_menu()
        option = input('Type your option: ')

        match option:
            case '1':
                get_top_tracks() # Retrieve top tracks of an artist
            case '2':
                get_top_album() # Find the top album from an artist
            case '3': 
                get_track_duration() # Check the duration of a specific track
            case '4': 
                get_specific_year_tracks() # Discover songs released in a specific year
            case '5':  
                get_track_listeners() # See how many listeners a song has
            case '6':
                plot_artist_popularity_overtime()  #Get and plot an artist's popularity
            case '7':
                retrieve_all_tracks()  #Register New Artist
            case '8':
                print('Thank you! See you next time!')
            case _:
                print('Error - Invalid option. Please input a number between en 1 and 8')

def display_menu():
  print("""
===================================================
           Welcome to Music Analytics   
===================================================
      Choose an option from the list below:

    1. Retrieve top tracks of an artist
    2. Find the top album from an artist
    3. Check the duration of a specific track
    4. Discover songs released in a specific year
    5. See how many listeners a song has
    6. See an artists popularity overtime
    7. Register New Artist
    8. Quit the program
===================================================
""")
  
if __name__ == '__main__':
    retrieve_all_tracks()
    main_menu()