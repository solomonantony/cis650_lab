"""
Slicing is done by specifying the index of the start and end positions separated by a : inside brackets[]
If the end position is after the start position, the characters in between are returned
"""
alphabets = "abcdefghijklmnopqrstuvwxyz"
start = int(input("Enter a start position: "))
stop = int(input("Enter a stop position: "))
print(alphabets[start:stop])
