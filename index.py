import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Ingresa tu Client ID y Client Secret obtenidos del panel de desarrolladores de Spotify
client_id = ""
client_secret = ""

# Configura las credenciales del cliente
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Crea un objeto de la API de Spotify
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# playlist de this is bad gyal -> segundos
playlist_name = "This is Bad Gyal"

results = sp.search(q=playlist_name, type='playlist')

# Extrae la URI de la playlist
if results['playlists']['items']:
    # Obtén la URI de la primera playlist encontrada
    playlist_uri = results['playlists']['items'][0]['uri']
    print(f'URI de la playlist "{playlist_name}": {playlist_uri}')
else:
    print(f'No se encontraron resultados para la playlist "{playlist_name}"')


# Obtiene la información de la playlist
playlist_info = sp.playlist(playlist_uri)

ms_playlist = 0
# Recorre las canciones de la playlist
for track in playlist_info['tracks']['items']:
    track_duration_ms = track['track']['duration_ms']
    ms_playlist += track_duration_ms


# Obtiene la duración del track en segundos
duration_seconds = ms_playlist / 1000

print(f'Duración de {playlist_name} en segundos: {duration_seconds}')
