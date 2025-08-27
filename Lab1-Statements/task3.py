first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

if len(first_name)>0 and len(last_name)>0:
    print('Hello, ', first_name, last_name)
else:
    print('Both entries must be non-blank')

if len(first_name)<=0 or len(last_name)<=0:
    print('Both entries must be non-blank')
else:
    print('Hello', first_name, last_name)
