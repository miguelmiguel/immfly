def exception_message(e):
  return ", ".join(map(str,e.args)) if len(e.args) > 0 else 'Unknown Error'

def detailed_exception_message(e):
  exception_args = ", ".join(map(str,e.args)) if len(e.args) > 0 else 'Unknown Error'
  return f"An exception of type '{type(e).__name__}' occurred. '{exception_args}'"
