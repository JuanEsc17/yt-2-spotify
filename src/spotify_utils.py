# This file is part of the Spotify Utils package.
from rapidfuzz import fuzz, process
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from src.utils import generar_variantes, limpiar_titulo

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope=os.getenv("scope")
))

# Función para buscar una canción en Spotify (ya no la uso)
def buscar_cancion(titulo):
    """
    Busca una canción en Spotify por su título.
    Args:
        titulo (str): Título de la canción a buscar.
    Returns:
        dict: Información de la canción encontrada, incluyendo nombre, artista y URI.
    """
    if not titulo:
        print("❌ Título de la canción no proporcionado.")
        return None
    resultado = sp.search(q=titulo, type="track", limit=1)
    items = resultado.get("tracks", {}).get("items", [])
    if items:
        track = items[0]
        return {
            "nombre": track["name"],
            "artista": track["artists"][0]["name"],
            "uri": track["uri"]
        }
    return None

def buscar_cancion_mejorada(titulo_original):
    """
    Busca una canción en Spotify utilizando un título original, limpiándolo primero para mejorar la búsqueda.
    Args:
        titulo_original (str): Título original de la canción a buscar.
    Returns:
        dict: Información de la canción encontrada, incluyendo nombre, artista, URI y score de coincidencia.
    """
    variantes = generar_variantes(titulo_original)
    mejor_candidato = None

    for variante in variantes:
        titulo_limpio = limpiar_titulo(variante)
        resultados = sp.search(q=titulo_limpio, type="track", limit=3)

        for item in resultados.get("tracks", {}).get("items", []):
            nombre_spotify = f"{item['name']} - {item['artists'][0]['name']}".lower()
            score = fuzz.partial_ratio(titulo_limpio, nombre_spotify)
            if not mejor_candidato or score > mejor_candidato["score"]:
                mejor_candidato = {
                    "nombre": item["name"],
                    "artista": item["artists"][0]["name"],
                    "uri": item["uri"],
                    "score": score
                }

    if mejor_candidato and mejor_candidato["score"] >= 80:
        return mejor_candidato
    return None

def crear_playlist(nombre="Migracion YouTube Music", descripcion="Playlist migrada desde YouTube Music"):
    """
    Crea una nueva playlist en Spotify.
    Args:
        nombre (str): Nombre de la playlist a crear.
        descripcion (str): Descripción de la playlist (opcional).
    Returns:
        str: ID de la playlist creada.
    """
    usuario = sp.current_user()["id"]
    playlist = sp.user_playlist_create(
        user=usuario,
        name=nombre,
        public=True,
        description=descripcion
    )
    return playlist["id"]

def agregar_canciones_a_playlist(playlist_id, canciones):
    """
    Agrega canciones a una playlist existente en Spotify.
    Args:
        playlist_id (str): ID de la playlist a la que se agregarán las canciones.
        canciones (list): Lista de diccionarios con información de las canciones a agregar.
    Returns:
        None
    """
    uris = [cancion["uri"] for cancion in canciones if "uri" in cancion]

    # Spotify permite agregar hasta 100 canciones a la vez
    for i in range(0, len(uris), 100):
        sp.user_playlist_add_items(
            playlist_id,
            uris[i:i + 100]
        )