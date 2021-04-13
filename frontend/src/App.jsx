import { pick } from 'rambda'
import { Header, DataLink, Reporter, Button } from './components'
import { LimitedContainer } from './components/shares'
import { useAppStore } from './states'


const App = () => {
  const {
    pendingFile,
    needCheckFile,
    checkingStatus,
  } = useAppStore(pick('pendingFile,needCheckFile,checkingStatus'))

  const {
    checkStatusIntervally,
    generateButtonClick,
    getReportData,
  } = useAppStore(pick('checkStatusIntervally,generateButtonClick,getReportData'))

  const shouldCheckStatus = pendingFile
	&& pendingFile === needCheckFile
	&& !checkingStatus

  if (shouldCheckStatus) checkStatusIntervally()

  const canGetReport = pendingFile && !needCheckFile

  const report = useAppStore(s => s.dataReport[s.latestFile])
  const fileInfo = useAppStore(s => s.fileInfo[s.latestFile || s.pendingFile])

  return (
    <div className="App">
      <Header />
      <LimitedContainer>
	<div>
	  <Button title="Generate" handler={generateButtonClick} />
	</div>
	<div>
	  <DataLink fileInfo={fileInfo} />
	</div>
	<div>
	  <Button
	    title="Report"
	    handler={getReportData}
	    disabled={!canGetReport}
	  />
	</div>
	<div>
	  <Reporter data={report} />
	</div>
      </LimitedContainer>
    </div>
  )
}

export default App
