import { IfElse} from './shares'


const DownloadBox = ({ fileInfo }) => (
  <div className="data-link__download">
    <div>
      <span>Download file:</span>
      <span>
	<a download href={fileInfo.url}>{fileInfo.name}</a>
      </span>
    </div>
  </div>
)

const EmptyBox = () => (
  <div className="data-link__empty">
    No file available for download
  </div>
)

export const DataLink = ({ fileInfo }) => (
  <div className="data-link">
    <IfElse check={fileInfo && fileInfo.url}>
      <DownloadBox fileInfo={fileInfo} />
      <EmptyBox />
    </IfElse>
  </div>
)
