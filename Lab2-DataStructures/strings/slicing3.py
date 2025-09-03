"""
In addition to the start and stop, we can specify the step also to skip a number of characters
If stop > start, and step = 1, it will return all the characters betwee start and stop
If start < stop and step <0, it will return the characters in reverse order
"""

alphabets = "abcdefghijklmnopqrstuvwxyz"
start = int(input("Enter a start position: "))
stop = int(input("Enter a stop position: "))
step = int(input("Enter step number: "))
print(alphabets[start:stop:step])
