import os
def printdir(dir):
    try:
        filenames = os.listdir(dir)
        for filename in filenames:
            print('file name: ',filename)
    except Exception as e:
        print(e)  #prints the message of that error 
    else:
        print('File path was good')

printdir('C:/Users/santony/Document/')

