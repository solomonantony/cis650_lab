## Slicing
# To generate a list with some of the items from a source list, use slicing
# Slicing involves using square brackets and one of more colons within

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers[2:6]) # get entries from item index 2 to item index 6, excluding 6
print(numbers[:6]) # Starting from 0, go up to item 6
numbers[6:] # starting from 6, all items after that
print(numbers[::2]) #Get every second item
print(numbers[0:-1])
print(numbers[::-1]) #starting from 0 go -1 index at a time
numbers[0:3] = ['two', 'three', 'five'] #replace the first
#print each result to ensure it works as commented
print(numbers[3])

