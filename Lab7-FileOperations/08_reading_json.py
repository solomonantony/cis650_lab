import json
path = 'Lab7-FileOperations/'
with open(path+"contact.json", 'r') as example:
    example_json = json.load(example)
print('all the data ==', example_json)
print('just first name ===', example_json['firstName'])
print('just the keys ===', example_json.keys())

