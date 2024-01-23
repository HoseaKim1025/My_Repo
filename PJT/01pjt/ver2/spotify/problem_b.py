import json
from pprint import pprint

def artist_info(artist, genres):
    for genre in genres:
        for i in range(len(artist['genres_ids'])):
            if artist['genres_ids'][i] == genre['id']:
                artist['genres_ids'][i] = genre['name']
    new_data = {
        'id' : artist['id'],
        'name' : artist['name'],
        'genres_names' : artist['genres_ids'],
        'images' : artist['images'],
        'type' : artist['type']
    }
    return new_data

if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
