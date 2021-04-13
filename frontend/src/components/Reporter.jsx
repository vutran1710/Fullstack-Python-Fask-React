import { List } from './shares'


const ReportRow = ({ dataKey, dataValue }) => (
  <li className="report-row">
    <div>
      <span>{dataKey}</span>
      <span>{dataValue}</span>
    </div>
  </li>
)

export const Reporter = ({ data }) => (
  <div className="reporter">
    <ul>
      <List object={data} component={ReportRow} />
    </ul>
  </div>
)
