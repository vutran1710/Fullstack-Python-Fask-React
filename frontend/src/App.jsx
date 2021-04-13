import { Header, DataLink, Reporter, Button } from './components'
import { LimitedContainer } from './components/shares'
import './App.css'

const App = () => (
  <div className="App">
    <Header />
    <LimitedContainer>
      <div>
	<Button title="Generate" />
      </div>
      <div>
	<DataLink />
      </div>
      <div>
	<Button title="Report" />
      </div>
      <div>
	<Reporter />
      </div>
    </LimitedContainer>
  </div>
)

export default App
