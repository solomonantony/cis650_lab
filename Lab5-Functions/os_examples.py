import os
username = os.environ.get('USER') or os.environ.get('USERNAME')
print(f"Username: {username}")
