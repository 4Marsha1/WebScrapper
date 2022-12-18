from bs4 import BeautifulSoup
import requests

WIKIPEDIA_URL = 'https://en.wikipedia.org'

print('Search for?')
query = input('>').replace(" ", "_")
print('Fetching results...')

def fetch_results(): 
    html_text = requests.get(f'{WIKIPEDIA_URL}/wiki/{query}').text
    soup = BeautifulSoup(html_text, 'lxml')

    table = soup.find('table', class_='infobox').tbody
    items = table.find_all('tr')
    data = []
    for item in items:
        if item.th: 
            key = item.th.text
            if item.td:
                value=item.td.text
                anchors = item.find_all('a')
                link=""
                for a in anchors: 
                    link += WIKIPEDIA_URL + a['href']+ ' '
                data.append({'key': key.strip(), 'value': value.strip(),'link': link.strip()})

    with open(f'data/{query}.txt', 'w') as f: 
        for row in data:
            f.write(f'{row["key"]}: {row["value"]} ({row["link"]})\n')

if __name__ == '__main__': 
    fetch_results()