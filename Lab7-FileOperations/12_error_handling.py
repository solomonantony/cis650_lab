import os
def printdir(dir):
    try:
        filenames = os.listdir(dir)
        for filename in filenames:
            print('file name: ',filename) 

    except FileNotFoundError:  #if we know the error message
        print('Incorrect file path')
    else:
        print('File path was good')

printdir('C:/Users/santony/Document/')

