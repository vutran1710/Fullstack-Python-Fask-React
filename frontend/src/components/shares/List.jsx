import { Fragment } from 'react'
import { Empty } from './Empty'


export const List = ({ object, items, component: Component }) => {
  const shouldRenderList = items && Array.isArray(items)

  if (shouldRenderList) {
    return (
      <Fragment>
	{items.map((item, idx) => (
	  <Component
	    item={item}
	    index={idx}
	    key={item.key || idx}
	  />
	))}
      </Fragment>
    )
  }

  const shouldRenderObject = typeof object === 'object' && Object.values(object).length

  if (shouldRenderObject) {
    return (
      <Fragment>
	{Object.keys(object).map((dataKey, idx) => (
	  <Component
	    dataKey={dataKey}
	    dataValue={object[dataKey]}
	    key={dataKey}
	    index={idx}
	  />
	))}
      </Fragment>
    )
  }

  return <Empty />
}
