def average(*args):
  return f'{sum(args) / len(args)}'
  #return sum(args) / len(args)
print('with 2 arguments', average(5, 10))
print('with 4 arguments', average(5, 10, 15, 20))
#print('no argument',average())
grades = [88, 75, 96, 55, 83]
print('with a list', average(*grades)) #The * operator, when applied to an iterable argument in a function call, unpacks its elements
print('with a single value', average(12))
#Modify the function so that it wouldn't break if no arguments were passed
# hint: use the len(args) function to check if the number of arguments > 0
