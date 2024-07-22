import pandas as pd
import requests as req
import bs4

print(f'Pandas version: {pd.__version__}')
url = 'https://www.duckduckgo.com'
response = req.get(url)
print(response.status_code)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

for x in soup.find_all():
    print(x.getText())
    print(soup.prettify())
    print('--------')

with open('nba_all_elo.csv', 'wb') as f:
    f.write(response.content)

dir()

nba = pd.read_csv('nba_all_elo.csv')
type(nba)
len(nba)
nba.head()
