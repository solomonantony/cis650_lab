list1 = ['a', 'a', 'c', 'b']
list2 = [1,2,5,7]
dict1 = dict(zip(list1, list2))
print(dict1)
for k in dict1:  #when we don't know  the key labels
  print(type(k))
  print(k, dict1[k])

for key, value in dict1.items(): #when we don't know  the key labels
  print('key:', key, 'value: ', value)
   