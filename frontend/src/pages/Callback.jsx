import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export function Callback() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get("code");

    if (code) {
      // Enviar el código al backend
      localStorage.setItem("spotify_token", code)
      setLoading(false)
      navigate("/createPlaylist")
    }
      else{
        setError('No se recibio el codigo de autorizacion')
        setLoading(false)
      }
  }, [navigate]);

  if (loading){
    return <div>Autenticando con Spotify</div>
  }
  if (error) {
    return <div>Error: {error}</div>
  }

  return null
}

export default Callback;
