const clientId = "d85d4c47f34e4b948d4b600f35f8ac56";
const redirectUri = "http://127.0.0.1:5000/callback"; // o tu URL real
const scope = "playlist-modify-public playlist-modify-private";
const authEndpoint = "https://accounts.spotify.com/authorize";

const loginUrl = `${authEndpoint}?client_id=${clientId}&response_type=code&redirect_uri=${encodeURIComponent(redirectUri)}&scope=${encodeURIComponent(scope)}`;

const LoginButton = () => {
    return(
        <a href={loginUrl} >
            <button>Connect to Spotify</button>
        </a>
    ) 
}

export const Home = () => {
    return (
        <div style={{ 
            textAlign: 'center', 
            padding: '50px',
            fontFamily: 'Arial, sans-serif'
        }}>
            <h1>Youtube Music to Spotify</h1>
            <p>Convierte tus playlists de Youtube Music a Spotify</p>
            <LoginButton/>
        </div>
    )
}