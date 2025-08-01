# YouTube Music a Spotify 🎵

Este proyecto permite convertir automáticamente una playlist de YouTube Music en una playlist equivalente en Spotify, utilizando las APIs de ambas plataformas. Incluye una interfaz web moderna desarrollada con React y un backend en Flask.

## 🛠️ ¿Qué hace?

- Extrae los títulos de las canciones desde una playlist pública de YouTube Music  
- Busca cada canción en Spotify usando coincidencia aproximada  
- Crea una nueva playlist en tu cuenta de Spotify con las canciones encontradas  
- Interfaz web amigable para una experiencia de usuario intuitiva

## ⚙️ Tecnologías utilizadas

### 🎨 Frontend:
- **React**: Interfaz de usuario moderna y reactiva
- **React Router**: Navegación entre páginas
- **Vite**: Herramienta de build rápida para desarrollo

### 🔧 Backend:
- **Flask**: Framework web ligero para Python
- **Flask-CORS**: Manejo de CORS para comunicación frontend-backend

### 📡 APIs:
- **Spotify Web API**: Para autenticación, búsqueda y creación de playlists
- **YouTube Data API v3**: Para extraer los títulos de videos desde una playlist pública

### 🧰 Librerías y herramientas:
- **Spotipy**: Cliente Python para interactuar con la API de Spotify
- **Google API Python Client**: Para conectarse a la API de YouTube
- **RapidFuzz**: Para comparar títulos con fuzzy matching y mejorar la precisión en la búsqueda
- **python-dotenv**: Para gestionar variables de entorno desde un archivo .env

## 🚀 Instalación y configuración

### 1. Cloná el repositorio:
```bash
git clone https://github.com/JuanEsc17/yt-2-spotify.git
cd yt-2-spotify
```

### 2. Configurá el Backend:
```bash
cd backend
pip install -r requirements.txt
```

### 3. Configurá el Frontend:
```bash
cd frontend
npm install
```

### 4. Configurá tus credenciales:
Crea un archivo `.env` en la carpeta `backend/`:
```env
API_KEY=tu_youtube_api_key
SPOTIFY_CLIENT_ID=tu_spotify_client_id
SPOTIFY_CLIENT_SECRET=tu_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://127.0.0.1:5000/callback
SCOPE=playlist-modify-public
```

### 5. Configurá Spotify Developer Dashboard:
1. Ve a [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Crea una aplicación
3. En "Redirect URIs", agrega: `http://127.0.0.1:5000/callback`
4. Copia el Client ID y Client Secret al archivo `.env`

### 6. Configurá YouTube Data API:
1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un proyecto y habilita YouTube Data API v3
3. Crea una clave de API y agrégala al archivo `.env`

## 🎯 Uso de la aplicación

### Desarrollo (Frontend y Backend separados):

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Accede a: `http://127.0.0.1:5173`

### Producción (Frontend compilado en Backend):

1. **Compila el frontend:**
```bash
cd frontend
npm run build
```

2. **Ejecuta solo el backend:**
```bash
cd backend
python app.py
```

Accede a: `http://127.0.0.1:5000`

## 📋 Requisitos

- **Cuenta de Spotify** (para crear playlists)
- **API key de YouTube Data API v3** (para leer playlists)
- **Python 3.8+**
- **Node.js 16+** (para React)

## ⚠️ Notas importantes

- ✅ Funciona solo con playlists **públicas** de YouTube Music
- ⚠️ Algunas canciones pueden no encontrarse por diferencias en los nombres
- 🔒 Nunca compartas tus credenciales de API públicamente
- 📝 Asegúrate de agregar `.env` a tu `.gitignore`

## 📁 Estructura del proyecto

```
yt-2-spotify/
├── backend/
│   ├── app.py              # Aplicación Flask principal
│   ├── requirements.txt    # Dependencias de Python
│   ├── .env               # Variables de entorno (no incluir en git)
│   └── src/
│       ├── spotify_utils.py    # Funciones de Spotify
│       ├── youtube_utils.py    # Funciones de YouTube
│       └── utils.py           # Utilidades generales
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Componente principal
│   │   ├── main.jsx          # Punto de entrada
│   │   └── pages/
│   │       ├── Home.jsx       # Página de inicio
│   │       ├── Callback.jsx   # Callback de Spotify
│   │       └── CreatePlaylist.jsx  # Formulario de creación
│   ├── package.json          # Dependencias de Node.js
│   ├── vite.config.js       # Configuración de Vite
│   └── index.html           # Template HTML
├── README.md
└── .gitignore
```

## 🔄 Flujo de la aplicación

1. **Inicio**: Usuario hace clic en "Connect to Spotify"
2. **Autenticación**: Redirige a Spotify para autorizar la aplicación
3. **Callback**: Spotify devuelve el código de autorización
4. **Formulario**: Usuario ingresa URL de YouTube y detalles de playlist
5. **Procesamiento**: 
   - Extrae canciones de YouTube
   - Busca cada canción en Spotify
   - Crea nueva playlist en Spotify
   - Agrega canciones encontradas
6. **Resultado**: Muestra resumen con canciones agregadas y no encontradas

## 👨‍💻 Autor

**Juan Escudero**  
[GitHub](https://github.com/JuanEsc17) | [LinkedIn](https://www.linkedin.com/in/juan-escudero-ab6428255/)

---

⭐ ¡Si te gusta este proyecto, dale una estrella en GitHub!
