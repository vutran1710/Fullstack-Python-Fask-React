import { IfElse} from './shares'


const DownloadBox = ({ fileInfo }) => (
  <div className="data-link--download">
    <a download href={fileInfo.url}>
      {fileInfo.name}
    </a>
  </div>
)

const EmptyBox = () => (
  <div>
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
