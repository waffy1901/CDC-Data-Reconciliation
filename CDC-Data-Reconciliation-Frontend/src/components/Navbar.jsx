import { NavLink } from "react-router-dom"

export default function Navbar() {
  return (
    <div className='w-full p-5 bg-slate-500'>
      <div className='flex flex-row justify-start gap-6 items-center text-xl'>
        <NavLink
          to='/'
          className={({ isActive }) => (isActive ? "text-slate-100 font-bold" : "font-bold text-slate-800")}
        >
          Home
        </NavLink>
        <NavLink
          to='/settings'
          className={({ isActive }) => (isActive ? "text-slate-100 font-bold" : "font-bold text-slate-800")}
        >
          Settings
        </NavLink>
      </div>
    </div>
  )
}
