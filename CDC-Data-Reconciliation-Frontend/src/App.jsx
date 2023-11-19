import { Routes, Route } from "react-router-dom"
import Home from "./pages/Home.jsx"
import Settings from "./pages/Settings.jsx"
import Navbar from "./components/Navbar.jsx"

export default function App() {
  return (
    <div className='flex flex-col w-screen h-screen'>
      <Navbar />
      <div className='flex-1 h-full bg-slate-100'>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/settings' element={<Settings />} />
        </Routes>
      </div>
    </div>
  )
}
