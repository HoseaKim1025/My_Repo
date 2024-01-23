import json
from pprint import pprint

def artist_info(artist):
    new_data = {
        'id' : artist['id'],
        'name' : artist['name'],
        'genres_ids' : artist['genres_ids'],
        'images' : artist['images'],
        'type' : artist['type']
    }
    return new_data

if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))