# import requests   #modulo que te permite hacer llamadas a apis
#clienID = ""
#clientSecret = ""
# print(requests.get("https://www.google.com"))

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Ingresa tu Client ID y Client Secret obtenidos del panel de desarrolladores de Spotify
client_id = ""
client_secret = ""

# Configura las credenciales del cliente
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Crea un objeto de la API de Spotify
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Ahora puedes hacer solicitudes a la API de Spotify utilizando 'sp'

#results = sp.search(q='artist:Queen', type='artist')
#print(results)

# Busca un artista por nombre
artist_name = "Bad Gyal"
results = sp.search(q='artist:' + artist_name, type='artist')

# Extrae la URI del primer resultado (puede haber varios resultados)
if len(results['artists']['items']) > 0:
    artist_uri = results['artists']['items'][0]['uri']
    print(f'URI del artista "{artist_name}": {artist_uri}')
else:
    print(f'No se encontraron resultados para el artista "{artist_name}"')

results = sp.artist_albums(artist_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


