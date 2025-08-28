## List operations: Removing from a list


c = [-45, 6, 0, 72, 1543]
c.pop(1)  #removes the item at index 1; list is shorter now
letters1.remove('y') #finds and removes first occurrence of 'y'
del c[0]  #deletes the item at 0 position
c = [-45, 6, 0, 72, 1543]
del c[0:2] #Removes items 0 and 1
c = [-45, 6, 0, 72, 1543]
c.remove(72) #removes the item and resizes the list
c.clear() #empties the list
#print the value c after each operation to make sure you understand it
