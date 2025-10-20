import os
def printdir(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    print('file name: ',filename)  
printdir('C:/Users/santony/Document/')
#passing an incorrect path to the function leads to a runtime error on line 3
