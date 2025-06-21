from src.spotify_utils import agregar_canciones_a_playlist, buscar_cancion_mejorada, crear_playlist
from src.utils import limpiar_titulo
from src.youtube_utils import extract_playlist_id, obtener_videos_de_playlist


# Ejemplo de uso
if __name__ == "__main__":
    link = input("Pegá el link de la playlist de YouTube Music: ")
    playlist_id = extract_playlist_id(link)
    
    if playlist_id:
        canciones_youtube = obtener_videos_de_playlist(playlist_id)
        print("\n🎵 Canciones encontradas:")
        for i, c in enumerate(canciones_youtube, 1):
            print(f"{i}. {c}")
    else:
        print("❌ No se pudo extraer el ID de la playlist.")

    print("\n🎯 Buscando canciones en Spotify...\n")
    canciones_encontradas = []
    no_encontradas = []
    for titulo in canciones_youtube:
        cancion = buscar_cancion_mejorada(titulo)
        if cancion:
            print(f"✔️ Encontrada: {cancion['nombre']} - {cancion['artista']}")
            canciones_encontradas.append(cancion)
        else:
            print(f"❌ No se encontró: {titulo}")
            no_encontradas.append(titulo)

    if no_encontradas:
        print("\n❗ Canciones no encontradas:")
        for titulo in no_encontradas:
            print(f"- {titulo}")
    
    nombre_playlist = input("Ingrese el nombre de la nueva playlist (o deje vacío para usar el predeterminado): ")
    descripcion_playlist = input("Ingrese la descripción de la nueva playlist (o deje vacío para usar el predeterminado): ")

    playlist_id = crear_playlist(nombre_playlist, descripcion_playlist)
    agregar_canciones_a_playlist(playlist_id, canciones_encontradas)

    print(f"Playlist '{nombre_playlist}' creada")