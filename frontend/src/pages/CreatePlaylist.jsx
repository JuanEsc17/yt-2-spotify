import { useState } from "react"

export const CreatePlaylist = () => {
    const [youtubeUrl, setYoutubeUrl] = useState('')
    const [playlistName, setPlaylistName] = useState('')
    const [playlistDescription, setPlaylistDescription] = useState('')
    const [loading, setLoading] = useState(false)
    const [result, setResult] = useState(null)
    const [error, setError] = useState(null)

    const handleSubmit = async (e) => {
        e.preventDefault()
        setLoading(true)
        setError(null)

        try {
            const spotifyCode = localStorage.getItem('spotify_code')
            const response = await fetch('http://127.0.0.1:5000/api/create-playlist', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    youtube_url: youtubeUrl,
                    playlist_name: playlistName || 'Migración YouTube Music',
                    playlist_description: playlistDescription || 'Playlist migrada desde YouTube Music',
                    spotify_code: spotifyCode
                })
            })
            const data = await response.json()

            if (response.ok){
                setResult(data)
            }else{
                setError(data.error || 'Error al crear la playlist')
            }
        }
        catch {
            setError('Error de conexion con el servidor')
        }
        finally{
            setLoading(false)
        }
    }

    return (
    <div>
        <h2>Crear Playlist en Spotify</h2>
        <form onSubmit={handleSubmit} >
            <div>
                <label>
                    URL de Youtube Music:
                </label>
                <input type="url"
                        value={youtubeUrl}
                        onChange={(e) => setYoutubeUrl(e.target.value)}
                        placeholder="https://www.youtube.com/playlist?list=..."
                        required
                />
            </div>
            <div style={{ marginBottom: '15px' }}>
                    <label>
                        Nombre de la playlist:
                        <input
                            type="text"
                            value={playlistName}
                            onChange={(e) => setPlaylistName(e.target.value)}
                            placeholder="Migración YouTube Music"
                            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
                        />
                    </label>
                </div>

                <div style={{ marginBottom: '15px' }}>
                    <label>
                        Descripción:
                        <input
                            type="text"
                            value={playlistDescription}
                            onChange={(e) => setPlaylistDescription(e.target.value)}
                            placeholder="Playlist migrada desde YouTube Music"
                            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
                        />
                    </label>
                </div>

                <button 
                    type="submit" 
                    disabled={loading}
                    style={{
                        backgroundColor: '#1db954',
                        color: 'white',
                        padding: '10px 20px',
                        border: 'none',
                        borderRadius: '5px',
                        cursor: loading ? 'not-allowed' : 'pointer'
                    }}
                >
                    {loading ? 'Creando...' : 'Crear Playlist'}
                </button>
            </form>

            {error && (
                <div style={{ marginTop: '20px', color: 'red' }}>
                    Error: {error}
                </div>
            )}

            {result && (
                <div style={{ marginTop: '20px', color: 'green' }}>
                    <h3>¡Playlist creada exitosamente!</h3>
                    <p>Nombre: {result.playlist_name}</p>
                    <p>Canciones agregadas: {result.songs_added}</p>
                    {result.not_found && result.not_found.length > 0 && (
                        <div>
                            <h4>Canciones no encontradas:</h4>
                            <ul>
                                {result.not_found.map((song, index) => (
                                    <li key={index}>{song}</li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            )}
        </div>
    )
}