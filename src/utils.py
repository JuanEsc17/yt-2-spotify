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

    # Quitar todo entre paréntesis, corchetes y llaves
    titulo = re.sub(r"\(.*?\)|\[.*?\]|\{.*?\}", "", titulo)

    # Eliminar emojis y símbolos no alfabéticos (excepto letras, números, espacios)
    titulo = re.sub(r"[^\w\s]", "", titulo)

    # Eliminar palabras comunes no musicales
    palabras_irrelevantes = [
        "official", "video", "videoclip", "versión", "version", "feat", "ft", "audio",
        "musica", "music", "letra", "lyrics", "serie", "from", "album", "eurovision",
        "remix", "hd", "video oficial", "videoclip oficial"
    ]
    for palabra in palabras_irrelevantes:
        titulo = titulo.replace(palabra, "")

    # Espacios múltiples → uno solo
    titulo = re.sub(r"\s+", " ", titulo)

    return titulo.strip()

