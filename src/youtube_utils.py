from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import re

# Extraer ID de la playlist a partir del link
def extract_playlist_id(playlist_link):
    """
    Extrae el ID de la playlist de YouTube Music a partir del enlace proporcionado.
    Args:
        playlist_link (str): Enlace de la playlist de YouTube Music.
    Returns:
        str: ID de la playlist si se encuentra, None en caso contrario.
    """
    match = re.search(r"(?:list=)([a-zA-Z0-9_-]+)", playlist_link)
    return match.group(1) if match else None

# Obtener los videos de la playlist
def obtener_videos_de_playlist(playlist_id):
    """
    Obtiene los títulos de los videos de una playlist de YouTube Music.
    Args:
        playlist_id (str): ID de la playlist de YouTube Music.
    Returns:
        list: Lista de títulos de los videos en la playlist.
    """
    youtube = build('youtube', 'v3', developerKey=os.getenv("API_KEY"))
    videos = []
    next_page_token = None
    while True:
        respuesta = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in respuesta['items']:
            if item['snippet']['title'] == 'Private video' or item['snippet']['title'] == 'Deleted video':
                continue
            titulo = item['snippet']['title']
            videos.append(titulo)
        
        next_page_token = respuesta.get('nextPageToken')
        if not next_page_token:
            break

    return videos