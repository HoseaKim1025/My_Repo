import json
from pprint import pprint

def acoustic_artists(artists, genres):
    new_data = []
    for artist in artists:
        if genres[0]['id'] in artist['genres_ids']:
            new_data.append(artist['name'])
            
    return new_data

if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_dict = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(acoustic_artists(artists_dict, genres_list))