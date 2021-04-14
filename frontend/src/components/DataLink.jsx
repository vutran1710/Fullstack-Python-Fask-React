import cx from 'classnames'
import { IfElse} from './shares'


const DownloadBox = ({ fileInfo }) => (
  <div className="data-link__download">
    <div className="data-link-download__label">
      File available
    </div>
    <div className="data-link-download__link">
      <a download href={fileInfo.url}>{fileInfo.name}</a>
    </div>
  </div>
)

const EmptyBox = () => (
  <div className="data-link__empty">
    No file available for download
  </div>
)

export const DataLink = ({ fileInfo, disable }) => {
  const cls = cx('data-link', { disable })
  return (
    <div className={cls}>
      <IfElse check={!disable && fileInfo && fileInfo.url}>
	<DownloadBox fileInfo={fileInfo} />
	<EmptyBox />
      </IfElse>
    </div>
  )
}
