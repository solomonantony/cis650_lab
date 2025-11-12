import requests
import pandas as pd
url = "https://www.nfl.com/stats/player-stats/"
# get the page of interest from the web
response = requests.get(url)
if response.status_code == 200:
  page_content = response.text
else:
  print(f'Error: Could not retrieve the web page. Status code: {response.status_code}')
  exit()
tables = pd.read_html(url)
print(tables[0])
player_stats_df = tables[0]
