c = [-45, 6, 0, 72, 1543]
c += [10]
print(c)
letters1 = list('sp am') #unpack the string into a list
print(letters1)
print(letters1+['a','b']) # appends two items to letters1

letters1 + list("Python") #unpacks 'Python' and appends to letters1
print(letters1*3) # appends a copy of letters1 to letters1
letters1.append('a1') #appends 'a1' to letters
letters1.insert(0,123) #insert 123 at 0
print(c + c)
c.extend(['xx', 'yy']) #extends the list by two items
#print the result of each line above to verify the result
