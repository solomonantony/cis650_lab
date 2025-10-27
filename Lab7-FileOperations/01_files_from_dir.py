import os
def printdir(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    print('file name: ',filename)  
print('Current working directory is :', os.getcwd())
input('Press enter to continue...')
printdir(os.getcwd())
