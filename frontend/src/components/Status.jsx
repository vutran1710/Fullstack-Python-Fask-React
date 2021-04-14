import cx from 'classnames'

export const Status = ({ status }) => {
  const cls = cx('status', {
    checking: status === 'WAIT',
    finish: status === 'FINISH',
  })

  return (
    <div className={cls}>
      {!status && (
	<div>
	  <span>No active check</span>
	</div>
      )}
      {status === 'WAIT' && (
	<div>
	  <span>Checking...</span>
	</div>
      )}
      {status === 'FINISH' && (
	<div>
	  <span>Checking Finish!</span>
	</div>
      )}
    </div>
  )
}
