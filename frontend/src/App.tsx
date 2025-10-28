import { NavLink, Outlet } from 'react-router-dom'
import './App.css'

function App() {
  return (
    <div className="app-root">
      <header className="app-header">
        <nav className="nav">
          <div className="brand">TaiLOR</div>
          <NavLink to="/" end className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}>
            Upload
          </NavLink>
          <NavLink to="/queue" className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}>
            Processing Queue
          </NavLink>
          <NavLink to="/results" className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}>
            Results
          </NavLink>
          <div className="spacer" />
          <span className="status-dot online">Backend Connected</span>
        </nav>
      </header>
      <main className="app-main">
        <Outlet />
      </main>
      <footer className="app-footer">
        <small>© {new Date().getFullYear()} TaiLOR</small>
      </footer>
    </div>
  )
}

export default App
