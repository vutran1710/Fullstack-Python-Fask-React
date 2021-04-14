import { pick } from 'rambda'
import {
  Header,
  DataLink,
  Reporter,
  Button,
  Explain,
  Status,
} from './components'
import {
  LimitedContainer,
  Block,
  Row,
} from './components/shares'
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

  const disableDataLink = !fileInfo
	|| needCheckFile === fileInfo.name

  const statusValue = useAppStore(s => {
    if (!pendingFile) return undefined
    if (s.checkingStatus) return 'WAIT'
    return 'FINISH'
  })

  return (
    <div className="App p2">
      <LimitedContainer className="control-box">
	<Block float fullHeight>
	  <Header />
	  <Row>
	    <Explain
	      text="Generate data"
	      note="(int, real, string, alpha-numeric)"
	    />
	    <Button title="Generate" handler={generateButtonClick} />
	  </Row>
	  <div>
	    <DataLink
	      fileInfo={fileInfo}
	      disable={disableDataLink}
	    />
	  </div>
	  <Row>
	    <Explain
	      text="Get report for current file"
	      note="(number of each objects)"
	    />
	    <Button
	      title="Report"
	      handler={getReportData}
	      disabled={!canGetReport}
	    />
	  </Row>
	  <div>
	    <Reporter data={report} />
	  </div>
	  <Status status={statusValue} />
	</Block>
      </LimitedContainer>
    </div>
  )
}

export default App
