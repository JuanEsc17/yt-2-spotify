# This file is part of the Spotify Utils package.
from rapidfuzz import fuzz, process
import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from src.utils import generar_variantes, limpiar_titulo

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=config.SPOTIFY_CLIENT_ID,
    client_secret=config.SPOTIFY_CLIENT_SECRET,
    redirect_uri=config.SPOTIFY_REDIRECT_URI,
    scope=config.scope
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