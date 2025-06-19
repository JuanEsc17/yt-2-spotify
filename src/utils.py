import re

def generar_variantes(titulo):
    """
    Genera variantes del título de una canción para mejorar la búsqueda en Spotify.
    Args:
        titulo (str): Título de la canción original.
    Returns:
        list: Lista de variantes del título.
    """
    variantes = [titulo]
    if " - " in titulo:
        partes = titulo.split(" - ")
        if len(partes) == 2:
            invertido = f"{partes[1]} - {partes[0]}"
            variantes.append(invertido)
    return variantes

def limpiar_titulo(titulo):
    """
    Limpia el título de una canción eliminando caracteres especiales, espacios innecesarios y palabras
    como 'Video oficial' y etc...
    Args:
        titulo (str): Título de la canción a limpiar.
    Returns:
        str: Título limpio.
    """
    titulo = titulo.lower()
    titulo = re.sub(r'\(.*?\)', '', titulo)   # Quita cosas entre paréntesis
    titulo = re.sub(r'\[.*?\]', '', titulo)   # Quita cosas entre corchetes
    titulo = re.sub(r'official|video|audio|hd|lyrics|letra|oficial|ft|prod|by|x|visualizer', '', titulo) # Quita palabras comunes
    titulo = re.sub(r'[^a-zA-Z0-9\s]', '', titulo)  # Quita símbolos raros
    return titulo.strip()

