def bark(prompt):
  return f'Woof! {prompt}'
functions = [bark, str.lower, str.capitalize]
print(functions)
print(functions[0]('hey you'))

while True:
    menu_string = """
    ***Solomon Inc****
    1. Enter new customer data
    2. Review product inventory
    3. Create a sale record
    4. Update customer payment
    5. End
    Enter your choice [1-5]: """
    print(menu_string)
    user_choice = input()
    if user_choice == '5':
        break
    


