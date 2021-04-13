export const IfElse = ({ check, children, ...rest }) => {
  const Component = check ? children[0] : children[1]
  return typeof Component === 'object' ? Component : <Component />
}
