def squares(x):
  for i in range(x):
      print('From def ', i)
      yield i ** 2

print(squares(5))
for i in squares(5):
  input('Press Enter to continue...')
  print(f'i = {i}')
  
  