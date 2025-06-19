# YouTube Music a Spotify 🎵

Este proyecto permite convertir automáticamente una playlist de YouTube Music en una playlist equivalente en Spotify, utilizando las APIs de ambas plataformas.

## 🛠️ ¿Qué hace?

- Extrae los títulos de las canciones desde una playlist pública de YouTube Music
- Busca cada canción en Spotify usando coincidencia aproximada
- Crea una nueva playlist en tu cuenta de Spotify con las canciones encontradas

## 🚀 Cómo usar

1. Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/ytmusic-to-spotify.git
cd ytmusic-to-spotify
```

2. Instalá las dependencias:

``` bash
pip install -r requirements.txt
```

3. Configurá tus credenciales en un archivo config.py:

```bash
SPOTIFY_CLIENT_ID=tu_client_id
SPOTIFY_CLIENT_SECRET=tu_client_secret
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8000/callback
YOUTUBE_API_KEY=tu_api_key
```

4. Ejecutá el script principal:

``` bash
python app.py
```

### 📋 Requisitos
- Cuenta de Spotify
- API key de YouTube Data API v3
- Python 3.8+

### ⚠️ Notas
- Funciona solo con playlists públicas de YouTube Music
- Algunas canciones pueden no encontrarse por diferencias de nombre

### Autor
Juan Escudero
