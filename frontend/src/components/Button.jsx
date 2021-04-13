export const Button = ({ title, handler, ...rest }) => (
  <div className="btn">
    <button onClick={handler} {...rest} >
      {title}
    </button>
  </div>
)
