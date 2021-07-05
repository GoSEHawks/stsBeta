

import requests
from bs4 import BeautifulSoup
import re

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
    
    
    
    # there may be more elements you don't want, such as "style", etc.
]

for t in text: # filter out the data with our blacklist
    if t.parent.name not in blacklist:
        output += '{} '.format(t)
        
# out put a clear clean and filterd data to our terminal.
print(output)


