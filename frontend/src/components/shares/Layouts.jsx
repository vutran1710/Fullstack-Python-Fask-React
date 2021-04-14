import cx from 'classnames'


export const LimitedContainer = ({ className, children }) => {
  const cls = `limited-container ${className || ''}`
  return (
    <div className={cls}>
      {children}
    </div>
  )
}


export const Block = ({ float, fullHeight, children }) => {
  const cls = cx('block', {  float, fullHeight })
  return (
    <div className={cls}>
      {children}
    </div>
  )
}


export const Row = ({ children }) => {
  return (
    <div className="row">
      {children}
    </div>
  )
}
