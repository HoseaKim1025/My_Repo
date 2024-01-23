import json

def max_polularity(artists):
    pop = []
    for artist in artists:
        id = artist['id']
        artist_data_open = open(f"data/artists/{id}.json", encoding="utf-8")
        artist_data = json.load(artist_data_open)
        pop.append(artist_data['popularity'])
    most_pop_artist = artists[pop.index(max(pop))]
    return most_pop_artist['name']

if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)
    print(max_polularity(artists_list))