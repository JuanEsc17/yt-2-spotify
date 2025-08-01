from src.spotify_utils import agregar_canciones_a_playlist, buscar_cancion_mejorada, crear_playlist
from src.youtube_utils import extract_playlist_id, obtener_videos_de_playlist
from flask import Flask, request, jsonify, send_from_directory
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='./dist')
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/create-playlist', methods=['POST'])
def create_playlist_api():
    try:
        data = request.json
        youtube_url = data.get('youtube_url')
        playlist_name = data.get('playlist_name', 'Migracion Youtube a Spotify')
        playlist_description = data.get('playlist_description', 'Playlist creada desde Youtube a Spotify')
        spotify_code = data.get('spotify_code')

        playlist_id = extract_playlist_id(youtube_url)
    
        if not playlist_id:
            return {"error": "No se pudo extraer el ID de la playlist."}

        canciones_youtube = obtener_videos_de_playlist(playlist_id)
        
        if not canciones_youtube:
            return {"error": "No se encontraron canciones en la playlist de YouTube Music."}

        canciones_encontradas = []
        no_encontradas = []
        
        for titulo in canciones_youtube:
            cancion = buscar_cancion_mejorada(titulo)
            if cancion:
                canciones_encontradas.append(cancion)
            else:
                no_encontradas.append(titulo)

        nombre_playlist = "Nueva Playlist"
        descripcion_playlist = "Playlist creada desde YouTube Music"

        playlist_id = crear_playlist(nombre_playlist, descripcion_playlist)
        agregar_canciones_a_playlist(playlist_id, canciones_encontradas)


        return jsonify({
            'success': True,
            'playlist_name': playlist_name,
            'songs_added': len(canciones_encontradas),  # Ejemplo
            'not_found': no_encontradas  # Ejemplo
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)