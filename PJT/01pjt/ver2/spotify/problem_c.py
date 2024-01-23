import json
from pprint import pprint

def artist_info(artists, genres):
    new_data_list = []
    for artist in artists:
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
        new_data_list.append(new_data)
    return new_data_list

if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))