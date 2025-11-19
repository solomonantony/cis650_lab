import requests
from bs4 import BeautifulSoup
url = 'https://www.nfl.com/stats/player-stats/'
#url = "https://murraystatenews.org/"
#url = 'http://python.org/'
# get the page of interest from the web
response = requests.get(url)
if response.status_code == 200:
  page_content = response.text
else:
  print(f'Error: Could not retrieve the web page. Status code: {response.status_code}')
  exit()
print(type(page_content))
print(page_content)
