import { Fragment } from 'react'


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

  if (Object.values(object).length) {
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

  return (
    <div>
      Empty list...
    </div>
  )
}
