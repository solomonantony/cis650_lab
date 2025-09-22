def bark(prompt):
  return f'Woof! {prompt}'
functions = [bark, str.lower, str.capitalize]
print(functions)
print(functions[0]('hey you'))
