import logo from './logo.svg'
import { DataLink } from './components'
import './App.css'

const App = () => (
  <div className="App">
    <header className="App-header">
      <img src={logo} className="App-logo" alt="logo" />
      <p>
	omnilytics
      </p>
    </header>
    <div>
      <DataLink />
    </div>
  </div>
)

export default App
