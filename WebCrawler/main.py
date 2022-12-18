from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://en.wikipedia.org/wiki/Tom_Cruise').text
soup = BeautifulSoup(html_text, 'lxml')

anchors = soup.find('div', {'id': 'bodyContent'}).find_all('a')
for anchor in anchors:
    if 'href' in anchor.attrs: 
        print(f"{anchor['href']}\n")