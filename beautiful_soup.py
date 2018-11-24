# Beautifull Soup

'''
pip install beautifulsoup4

pip install lxml
lub
pip install html5lib

pip install requests
'''

from bs4 import BeautifulSoup
import requests

'''
FILE:
with open('html file name') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())

match = soup.title.text
lub soup.div itd

soup.find('div', class_='footer')['src']
soup.find('div', id='footer')
print(match) - tytul strony


for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
'''

source = requests.get('http://example.com/').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())


