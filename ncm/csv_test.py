import requests
import json
import pandas as pd

url = "http://localhost:3000/playlist/track/all?id=902732851&limit=50"

response = requests.get(url)
data = response.json()

songs_data = []
for song in data["songs"]:
    name = song["name"]
    song_id = song["id"]

    artists = []
    for artist in song["ar"]:
        artist_name = artist["name"]
        artist_id = artist["id"]
        artists.append({'name': artist_name, 'id': artist_id})
    album_id = song["al"]["id"]
    album_name = song["al"]["name"]
    
    song_data = {
        "Song Name": name,
        "Song ID": song_id,
        "Artists": artists,
        "Album Name": album_name,
        "Album ID": album_id
    }
    songs_data.append(song_data)

df = pd.DataFrame(songs_data)
df.to_csv("songs_data.csv", index=False, encoding='utf-8-sig')
