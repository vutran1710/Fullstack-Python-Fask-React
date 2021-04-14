import { List } from './shares'


const ReportRow = ({ dataKey, dataValue }) => (
  <li className="report-row">
    <div className="report-row--key">{dataKey}</div>
    <div className="report-row--value">{dataValue}</div>
  </li>
)

export const Reporter = ({ data }) => (
  <div className="reporter">
    <ul>
      <List object={data} component={ReportRow} />
    </ul>
  </div>
)
