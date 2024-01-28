# HACK NIGHTS EPISODI IV: API

## Introducción
El 17 de noviembre de 2023 se celebró en la FIB el cuarto episodio de _HackNights_ de la temporada 2023.

Nos hicieron una **workshop de API's** y me inspiré en ella para trabajar con una.

Los programas proporcionados utilizan la biblioteca Spotipy, que es un cliente Python para la API de Spotify.

### Requisitos
- Python 3.x
- Biblioteca Spotipy 

Se puede instalar mediante `pip install spotipy`.

### Configuración
Antes de ejecutar el programa, es necesario configurar las **credenciales de cliente de Spotify** en el archivo. Puedes obtener estas credenciales registrando tu aplicación en el [Panel de Desarrolladores de Spotify](https://developer.spotify.com/).

```
client_id = "TU_CLIENT_ID"
client_secret = "TU_CLIENT_SECRET"
```
### Ejecución
Para ejecutar cualquiera de los dos prorgramas, desde la terminal escribir `python3 <nombre_programa>.py`

### Nota
Este programa utiliza la API de Spotify, por lo que **necesita acceso a Internet** para realizar las solicitudes a la plataforma. Asegúrate de tener una conexión activa a Internet mientras ejecutas el programa.

## albumNames.py

Este programa utiliza la biblioteca Spotipy para buscar un artista en Spotify y devolver los **nombres de los álbumes** asociados con ese artista.

Para escoger el artista se debe modificar `artist_name = "NOMBRE_ARTISTA"`.

## secondsPlaylist.py

Este programa utiliza la biblioteca Spotipy para buscar una playlist en Spotify y calcular la **duración total de la playlist en segundos**.

Para escoger la playlist se debe modificar `playlist_name = "NOMBRE_PLAYLIST"`.