import json
import os
import matplotlib.pyplot as plt

# method to load the Spotify data from a JSON file
def load_spotify_data(artist_name):
    file_name = f'resources/{artist_name}_spotify_tracks.json'

    # check if file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError(f'File {file_name} does not exists.')
    # check if file is empty
    if os.path.getsize(file_name) == 0:
        raise ValueError(f'Error: The file {file_name} is empty.')

    # try loading the file's JSON content
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    # Catch any format issues
    except json.JSONDecodeError as e:
        raise ValueError(f'Error: JSON file {file_name} has the wrong format: {e}')
    # catch any other errors
    except Exception as error:
        print(error)

# method to load the Last.fm data from a JSON file
def load_lastfm_data(artist_name):
    file_name = f'resources/{artist_name}_lastfm_tracks.json'
    # check if file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError(f'File {file_name} does not exists.')
    # Check if file is empty
    if os.path.getsize(file_name) == 0:
        raise ValueError(f'Error: The file {file_name} is empty.')

    # try loading the file's JSON content
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    # catch any format issues
    except json.JSONDecodeError as e:
        raise ValueError(f'Error: JSON file {file_name} has the wrong format: {e}')
    # catch any other errors
    except Exception as error:
        print(error)

# method to get the popularity of a track (used for sorting)
def get_popularity_spotify(track):
    return int(track['popularity'])
# method to get the play count of a track (used for sorting)
def get_play_count_lastfm(track):
    return int(track['playcount'])

# method to display top 10 tracks sorted by popularity
def display_top_spotify_tracks(artist_name):
    spotify_tracks_data = load_spotify_data(artist_name)

    if spotify_tracks_data:
        popularity_list = []
        # Add 'name' and 'popularity' key values to popularity_list
        for track in spotify_tracks_data:
            popularity_list.append({'name': track['name'], 'popularity': track['popularity']})

        # sort by popularity in descending order
        sorted_list = sorted(popularity_list, key=get_popularity_spotify, reverse=True)

        # display Top tracks
        print(f'\nTop Tracks of \'{artist_name}\' on Spotify (sorted by popularity):')
        for track in sorted_list[:10]:
            print(f'"{track['name']}"  (popularity:{track['popularity']})')
        
        # getting the track names and the popularity scores for the plot
        track_names = [track['name'] for track in sorted_list[:10]]
        popularity_scores = [track['popularity'] for track in sorted_list[:10]]

        # plotting Spotify API's data as a horizontal bar chart
        plt.figure(figsize=(12, 8))  # Setting the plot size
        plt.barh(track_names, popularity_scores, color='#FF69B4', height=0.8)  # Pink chart
        plt.xlabel('Popularity Score (0-100)')  # X-axis label
        plt.title(f'Top 10 Spotify Tracks of {artist_name} by Popularity')  # Title
        plt.gca().invert_yaxis()  # Flipping the y-axis to show highest popularity at the top
        plt.tight_layout()  # Adjusting  thelayout to fit all of the labels
        plt.savefig(f'{artist_name}_top_spotify_tracks.png')  # Saving the plot as an image
        plt.show()  # Displaying the plot

# method to display top 10 tracks from Last.fm data
def display_top_lastfm_tracks(artist_name):
    lastfm_tracks_data = load_lastfm_data(artist_name)

    # Ccheck for availability of data
    if lastfm_tracks_data:
        tracks_list = []
        # Add 'name' and 'play count' key values to tracks_list
        for track in lastfm_tracks_data:
            tracks_list.append({'name': track['name'], 'playcount': track['playcount']})

        # sort by play count in descending order
        sorted_list = sorted(tracks_list, key=get_play_count_lastfm, reverse=True)

        # display Top tracks
        print(f'\nTop Tracks of \'{artist_name}\' on Last.fm (sorted by play count):')
        for track in sorted_list[:10]:
            print(f'"{track['name']}"  (play count:{track['playcount']})')

        # Getting the track names and play counts for graph
        track_names = [track['name'] for track in sorted_list[:10]]
        play_counts = [int(track['playcount']) for track in sorted_list[:10]]

        # plotting Last.fm API's data as a bar chart
        plt.figure(figsize=(12, 8))  # Setting the plot size
        plt.barh(track_names, play_counts, color='#87CEEB', height=0.8)  # Light blue chart
        plt.xlabel('Play Count')  # X-axis label
        plt.title(f'Top 10 Last.fm Tracks of {artist_name} by Play Count')
        plt.gca().invert_yaxis()  # Flipping the y-axis to show highest play count at the top
        plt.tight_layout()  # Fitting the layout
        plt.savefig(f'{artist_name}_top_lastfm_tracks.png')  # Saving the plot
        plt.show()  # Displaying the plot

    else:
        print(f"No data found for {artist_name} on Last.fm.")

# get top 5 album of specific artist
def get_artist_top_albums(artist_name):
    # reading spotify data of the specific artist
    spotify_albums_data = load_spotify_data(artist_name)

    # if artist found
    if spotify_albums_data:
        albums_list = []
        # add name and popularity values to albums_list
        for track in spotify_albums_data:
            album_name = track['album']['name']
            album_popularity = track['popularity']
            albums_list.append({'name': album_name, 'popularity': album_popularity})

        # sort by popularity in descending order
        sorted_album_list = sorted(albums_list, key=get_popularity_spotify, reverse=True)

        # display the first 5 albums
        print(f'\nTop 5 Albums of \'{artist_name}\' (sorted by popularity):')
        for album in sorted_album_list[:5]:
            print(f"\"{album['name']}\"  (popularity: {album['popularity']})")
    else:
        print(f'No albums found for {artist_name}.')

# get track duration of specific artist
def get_track_duration(artist_name):
    # reading spotify data of the specific artist
    spotify_tracks_data = load_spotify_data(artist_name)

    # ask the user for the track name
    track_name = input(f'Enter the name of the track by \'{artist_name}\': ').strip()

    # if artist found
    if spotify_tracks_data:
        # search for the track in the data
        for track in spotify_tracks_data:
        
            if track['name'].lower() == track_name.lower():
                # get the duration in milliseconds
                duration_ms = track['duration_ms']
                # convert duration to minutes
                # the time in minutes is equal to the time in milliseconds divided by 60000
                duration_minutes = duration_ms / 60000 
                print(f'The duration of \'{track['name']}\' by \'{artist_name}\' is {duration_minutes:.2f} minutes.')
                return
        else:
            # if track does not exist
            print(f'Track \'{track_name}\' not found for artist \'{artist_name}\'.')

# method to get all tracks of an artist based on year of release
def get_tracks_of_particular_year(artist_name):
    # reading spotify data of the specific artist
    spotify_tracks_data = load_spotify_data(artist_name)

    year = input('\nEnter the year: ')

    # if artist found
    if spotify_tracks_data :
        tracks = []

        for track in spotify_tracks_data:
            # get release date of the album the track belongs to, None if not available
            track_release_date = track['album'].get('release_date', None)
            # get track name
            track_name = track['name']
            # check if the track has release date and if it starts with the inputed year
            if track_release_date and track_release_date.startswith(year):
                # add track name and release date to the list
                tracks.append({'name': track_name, 'release_date': track_release_date})
        
        # if track found
        if tracks:
            print(f'\nTracks released the year {year} of \'{artist_name}\' are:')
            for track in tracks:
                print(f'{track['name']} (release date: {track['release_date']})')
        else:
            # if no tracks were found for the specified year
            print(f'\nNo tracks found for the year {year}.')


def get_listener_count(artist_name):
    lastfm_tracks_data = load_lastfm_data(artist_name)

    track_name = input(f'Type in the track name by \'{artist_name}\' to get its listeners: ').strip()

    for track in lastfm_tracks_data:
        if track['name'].lower().startswith(track_name) == track_name.lower().startswith(track_name):
            # If match found display the track name and listener count
            print(f'{track['name']} (listeners: {track["listeners"]})')
            return

    print(f"No track found for '{track_name}' by '{artist_name}'.")

#Method to plot an artist's popularity overtime
def plot_artist_popularity(artist_name):
    # loading the artist data
    spotify_data = load_spotify_data(artist_name)
    if not spotify_data:
        print(f"No data found for {artist_name}.")
        return  # exit if no data is found

    years = []  # list to store years
    popularity = []  # list to store popularity scores

    # Going through every track to get the release years and their popularity scores
    for track in spotify_data:
        release_date = track['album'].get('release_date')
        if release_date:
            year = release_date.split('-')[0]  # Getting the year from the date
            years.append(year)  # adding the year to the list
            popularity.append(track['popularity'])  # aadding the popularity score to the list

    # creating a dictionary to store popularity score by the year
    popularity_by_year = {}
    for year, pop in zip(years, popularity): # Combining the two lists to associate the popularity score with the corresponding year based on the positions in the lists
        # Adding the popularity score to the current year, if the year already exists (since there can multiple tracks in the same year)
        if year in popularity_by_year:
            popularity_by_year[year].append(pop)
        # if the year doesn't exist in the dictionary, create a new key for it
        else:
            popularity_by_year[year] = [pop]

    # calculating the average popularity for each year
    avg_popularity = {}
    for year, pops in popularity_by_year.items():
        avg_popularity[year] = sum(pops) / len(pops)

    # sorting the years and their popularity
    sorted_years = sorted(avg_popularity.keys())
    sorted_popularity = [avg_popularity[year] for year in sorted_years]

    # plotting the data
    plt.figure(figsize=(10, 5))  # Setting the figure's size
    plt.plot(sorted_years, sorted_popularity, marker='o', color='#FFC0CB') # pink graph
    plt.title(f'{artist_name} Average Popularity Over Time', fontsize=14)  # Title
    plt.xlabel('Year', fontsize=12)  # X-axis label
    plt.ylabel('Avg Popularity', fontsize=12)  # Y-axis label
    plt.xticks(rotation=45)  # rotating the year labels
    plt.grid(True)  # Showing grid lines
    plt.tight_layout()  # fitting the layout

    plt.savefig(f'{artist_name}_popularity_over_time.png')  # saving the plot
    plt.show()  # showing the plot


