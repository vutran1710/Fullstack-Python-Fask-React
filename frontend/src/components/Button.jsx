export const Button = ({ title, handler }) => (
  <div className="btn">
    <button onClick={handler}>
      {title}
    </button>
  </div>
)
