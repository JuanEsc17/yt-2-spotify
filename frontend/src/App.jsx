import './App.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Home } from "./pages/Home"
import { Callback } from "./pages/Callback"
import { CreatePlaylist } from './pages/CreatePlaylist'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/callback" element={<Callback />} />
        <Route path="/createPlaylist" element={<CreatePlaylist/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App
