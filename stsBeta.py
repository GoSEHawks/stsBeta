
import re
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.google.com/finance?tab=ne' # the site we are scrapeing
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser') # the data we get from the scrape
text = soup.find_all(text=True)
#test_container = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'body',
    'font',
    'html{}',
    'style',
    'add_circle_outline'
    # there may be more elements you don't want, such as "style", etc.
]

for t in text: # filter out the data with our blacklist
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

# out put a clear clean and filterd data to our te
out1 = (output.split())
with open('snp500.csv') as f:
 csvf = csv.reader(f)
 ticker = []
 name = []
 for row in csvf:
  ticker.append(row[0])
  name.append(row[1])
match = {}
for word in out1:
 result = word in ticker
 if result == True:
  match[word] = result
print(match)


