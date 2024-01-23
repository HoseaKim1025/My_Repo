import json
from pprint import pprint

def get_popular(artists):
    new_data = []
    for artist in artists:
        id = artist['id']
        artist_data_open = open(f"data/artists/{id}.json", encoding="utf-8")
        artist_data = json.load(artist_data_open)
        if (artist_data['followers']['total'] > 5000000 and 
            artist_data['followers']['total'] < 10000000):
            new_data.append({'name' : artist['name'], 'followers' : artist_data['followers']['total']})
    return new_data

if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    pprint(get_popular(artists_list))