import requests
#from bs4 import BeautifulSoup
import re
url = "https://www.murraystate.edu/academics/CollegesDepartments/CollegeOfBusiness/Programs/CSIS/Faculty.aspx"
# get the page of interest from the web
response = requests.get(url)
if response.status_code == 200:
  page_content = response.text
else:
  print(f'Error: Could not retrieve the web page. Status code: {response.status_code}')
  exit()

#soup = BeautifulSoup(page_content, 'html.parser')
#print(soup)
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
found_emails = re.findall(email_pattern, page_content)
print(found_emails)