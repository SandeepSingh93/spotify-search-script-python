import requests
import base64
import sys


def get_spotify_access_token():
    client_id = "0d862453a8ec4546a3e7ccad48cf4039"
    client_secret = "c948033d62664c9ab134f899f892a8ff"

    auth_string = client_id + ':' + client_secret
    response = requests.post('https://accounts.spotify.com/api/token',\
                             headers = {'Authorization': f"Basic {base64.b64encode(auth_string.encode()).decode()}"},\
                             data = {'grant_type': 'client_credentials'})
    return response.json()['access_token']

def execute_request(http_method, api_endpoint, params):
    url = "https://api.spotify.com/v1" + api_endpoint
    token = get_spotify_access_token()
    headers = {'Authorization': f"Bearer {token}"}

    response = requests.request(http_method, url, headers=headers, params=params)
    return response.json()

def search_artist(artist_name):
    return execute_request('GET', '/search', {'q': artist_name, 'type': 'artist', 'limit': 3})

def get_artist_tracks(artist_id):
    return execute_request('GET', f"/artists/{artist_id}/top-tracks", {'market': 'IN'})


if __name__ == '__main__':
    print("####### Welcome to Spotify search. Search an artist and their top available tracks!! #######")

    while True:
        artist_name = input("Enter the artist name to search: ")
        if artist_name == '':
            print('Invalid Artist Name!! Type again.')
        else:
            break
    print()

    artist_results = search_artist(artist_name)
    artists = artist_results['artists']['items']
    if artists == []:
        print("Oh ho! No Artist found by this name.")
        print("Spotify Search will close now. Bbye!")
        sys.exit()

    print("==>Here are the top 3 search results: ")
    for serial,artist in enumerate(artists, start=1):
        print(str(serial) + '. ' + artist['name'])
    print()

    while True:
        artist_serial = input("Please select the artist (serial number): ")
        if artist_serial in ['1','2','3']:
            break
        else:
            print('Invalid Selection!! Type again.')
    print()

    track_results = get_artist_tracks(artists[int(artist_serial)-1]['id'])
    tracks = track_results["tracks"][:3]
    if tracks == []:
        print("Oh ho! This Artist does not have any tracks.")
        print("Spotify Search will close now. Bbye!")
        sys.exit()

    print(f"==>Here are the top 3 tracks of {artists[int(artist_serial)-1]['name']}: ")
    for serial, track in enumerate(tracks, start=1):
        print(str(serial) + '. ' + track['name'] + ': ' + track['external_urls']['spotify'])

    print()
    print("Hope you enjoy the tracks! :)")
    print("Closing Spotify search. Bbye!")