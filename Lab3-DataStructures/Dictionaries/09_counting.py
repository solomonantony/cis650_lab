words = """
A dictionary is an unordered collection which stores key–value pairs that map immutable keys to values, just as a conventional dictionary maps words to definitions.
Dictionaries can contain objects of any types; and they support nesting
fetched by key (instead of position as in list). You create dictionaries with literals and access items by key. uses Key-Value pairs
Each key can have one associated value A A A and and
In contrast with lists that sequentially number each item (the index), dictionaries allow you to name each item
"""
words_dict = dict()
for character in words:
    if character not in words_dict:
        print(f'{character} added')
        words_dict[character] = 1
    else:
        words_dict[character] = words_dict[character] + 1
print(words_dict)
#Modify this code so that punctuations are skipped
