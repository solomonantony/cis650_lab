

def remember(x):  #define a function
  if hasattr(remember,'author'):
    return f'Hi {x} Authored by {remember.author}'
  else:
    return f'Hi {x}'

# you know what this would do
print(remember('joe'))

i = remember  # assign it to an object
i.author = 'solomon' # attach an attribute for later use
print(i('Dan'))  #recall the value


  